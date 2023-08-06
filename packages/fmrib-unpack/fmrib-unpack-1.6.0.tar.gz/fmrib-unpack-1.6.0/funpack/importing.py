#!/usr/bin/env python
#
# importing.py - The data import stage
#
# Author: Paul McCarthy <pauldmccarthy@gmail.com>
#
"""This module provides the :func:`importData` function, which implements
the data importing stage of the ``funpack`` sequence
"""


import itertools             as it
import functools             as ft
import multiprocessing.dummy as mpd
import                          fnmatch
import                          logging
import                          warnings
import                          collections

import              six
import pandas    as pd
import numpy     as np

from . import       util
from . import       custom
from . import       merging
from . import       fileinfo
from . import       datatable
from . import       loadtables
from . import       expression


log = logging.getLogger(__name__)


NUM_ROWS = 10000
"""Default number of rows read at a time by :func:`loadData` - it reads the
data in chunks.
"""


MERGE_AXIS = 'variables'
"""Default merge axis when loading multiple data files - see :func:`mergeData`.
"""


MERGE_STRATEGY = 'intersection'
"""Default merge strategy when loading multiple data files - see
:func:`mergeData`.
"""

MERGE_AXIS_OPTIONS = ['0', 'rows', 'subjects',
                      '1', 'cols', 'columns', 'variables']
"""Values accepted for the ``axis`` option to the :func:`mergeData` function.
"""


MERGE_STRATEGY_OPTIONS = ['naive', 'union', 'intersection', 'inner', 'outer']
"""Values accepted for the ``strategy`` option to the :func:`mergeData`
function.
"""


def importData(datafiles,
               vartable,
               proctable,
               cattable,
               variables=None,
               colnames=None,
               categories=None,
               subjects=None,
               subjectExprs=None,
               exclude=None,
               encoding=None,
               unknownVars=None,
               trustTypes=False,
               removeUnknown=True,
               indexes=None,
               mergeAxis=None,
               mergeStrategy=None,
               loaders=None,
               lowMemory=False,
               workDir=None,
               pool=None,
               mgr=None,
               dryrun=False):
    """The data import stage.

    This function does the following:

      1. Figures out which columns to load (using the :func:`columnsToLoad`
         function).

      2. Loads the data (using :func:`loadData`),

      3. Creates and returns a :class:`DataTable`.

    :arg datafiles:         Path to the data file(s)

    :arg vartable:          The data coding table

    :arg proctable:         The processing table

    :arg cattable:          The category table

    :arg variables:         List of variable IDs to import

    :arg colnames:          List of names/glob-style wildcard patterns
                            specifying columns to import.

    :arg categories:        List of category names to import

    :arg subjects:          List of subjects to include

    :arg subjectExprs:      List of subject inclusion expressions

    :arg exclude:           List of subjects to exclude

    :arg encoding:          Character encoding(s) for data file(s). See
                            :func:`loadData`.

    :arg unknownVars:       List of :class:`.Column` objects representing
                            unknown variables

    :arg trustTypes:        If ``True``, it is assumed that columns with a
                            known data type do not contain any bad/unparseable
                            values. This improves performance, but will cause
                            an error if the assumption does not hold.

    :arg removeUnknown:     If ``True`` (the default), any variables in
                            ``datafile`` which are not in ``varfile`` are not
                            loaded. Ignored if ``variables``or ``categories``
                            are provided.

    :arg indexes:           Dict of ``{filename : index}`` mappings, specifying
                            the position of the column to use as the index.
                            Defaults to 0 (the first column).

    :arg mergeAxis:         Merging axis to use when loading multiple data
                            files - see the :func:`mergeData` function.

    :arg mergeStrategy:     Merging strategy to use when loading multiple
                            data files - see the :func:`mergeData` function.

    :arg loaders:           Dict of ``{ file : loaderName }`` mappings
                            containing custom sniffers/loaders to be used for
                            specific files. See the :mod:`.custom` module.

    :arg lowMemory:         Deprecated, has no effect.

    :arg workDir:           Deprecated, has no effect.

    :arg pool:              ``multiprocessing.Pool`` to use for parallelising
                            tasks.

    :arg mgr:               ``multiprocessing.Manager`` to use for sharing
                            state.

    :arg dryrun:            If ``True`` the data is not loaded.

    :returns:               A tuple containing:

                             - A :class:`DataTable`, which contains references
                               to the data, and the variable and procesing
                               tables.

                             - A list of :class:`.Column` objects that were not
                               loaded from each input file.
    """

    if lowMemory:
        warnings.warn('lowMemory is deprecated and has no effect.',
                      DeprecationWarning, stacklevel=2)
    if workDir is not None:
        warnings.warn('workDir is deprecated and has no effect.',
                      DeprecationWarning, stacklevel=2)

    if unknownVars is None:
        unknownVars = []

    variables = restrictVariables(cattable, variables, categories)

    # Figure out which columns to load
    cols, drop = columnsToLoad(datafiles,
                               vartable,
                               variables,
                               colnames,
                               unknownVars,
                               removeUnknown,
                               indexes=indexes,
                               sniffers=loaders)

    # Load those columns, merging
    # multiple input files.
    data, cols = loadData(datafiles,
                          vartable,
                          cols,
                          subjects=subjects,
                          subjectExprs=subjectExprs,
                          exclude=exclude,
                          encoding=encoding,
                          indexes=indexes,
                          mergeAxis=mergeAxis,
                          mergeStrategy=mergeStrategy,
                          loaders=loaders,
                          trustTypes=trustTypes,
                          pool=pool,
                          mgr=mgr,
                          dryrun=dryrun)

    # Re-order the columns according to
    # specified variables, if provided
    if variables is not None:

        # Build a list of all loaded vids -
        # this will include those loaded
        # via the colnames argument
        allvars = variables
        for c in cols[1:]:
            if c.vid not in allvars:
                allvars.insert(0, c.vid)

        # organise columns by vid
        # (skipping the index column)
        newcols = collections.defaultdict(list)
        for c in cols[1:]:
            newcols[c.vid].append(c)

        # order them by the variable list
        # (including the ID column for the
        # first file)
        cols = list(it.chain([cols[0]], *[newcols[v] for v in allvars]))

        if not dryrun:
            data = data[[c.name for c in cols[1:]]]

    dtable = datatable.DataTable(
        data, cols, vartable, proctable, cattable, pool)

    return dtable, drop


def restrictVariables(cattable, variables, categories):
    """Determines which variables should be loaded (and the order
    they should appear in the output) from the given sequences of
    ``variables`` and ``categories``.

    If neither ``variables`` nor ``categories`` are provided, ``None`` is
    returned, indicating that all variables should be loaded.

    :arg cattable:   The category table
    :arg variables:  List of variable IDs to import. May be ``None``.
    :arg categories: List of category names to import. May be ``None``.
    :returns:        Sequence of variables to load, or ``None`` if all
                     variables should be loaded.
    """

    # Build a list of all the variables we
    # want to load, from the variables and
    # categories that were passed in.
    if categories is not None:

        if variables is None:
            variables = []

        catvars   = loadtables.categoryVariables(cattable, categories)
        variables = variables + [c for c in catvars if c not in variables]

    return variables


def columnsToLoad(datafiles,
                  vartable,
                  variables,
                  colnames,
                  unknownVars,
                  removeUnknown,
                  indexes=None,
                  sniffers=None):
    """Determines which columns should be loaded from ``datafiles``.

    Peeks at the first line of the data file (assumed to contain column names),
    then uses the variable table to determine which of them should be loaded.

    :arg datafiles:     Path to data file(s)

    :arg vartable:      Variable table

    :arg variables:     List of variables to load. If provided,
                        ``removeUnknown`` is ignored.

    :arg colnames:      List of column names/glob-style wildcard patterns,
                        specifying columns to load. If provided,
                        ``removeUnknown`` is ignored.

    :arg unknownVars:   List of :class:`.Column` objects representing unknown
                        variables

    :arg removeUnknown: If ``True``, any variables in ``datafile`` which are
                        not in ``vartable`` are not loaded.

    :arg indexes:       Dict of ``{filename : index}`` mappings, specifying
                        the position of the column to use as the index.
                        Defaults to 0 (the first column).

    :arg sniffers:      Dict of ``{ file : snifferName }`` mappings containing
                        custom sniffers to be used for specific files. See the
                        :mod:`.custom` module.

    :returns:           A tuple containing:

                         - A dict of ``{ file : [Column] }`` mappings, the
                           :class:`.Column` objects to *load* from each input
                           file. The columns (including the index column) are
                           ordered as they appear in the file.

                         - A list containing the :class:`.Column` objects to
                           *ignore*.
    """

    if sniffers    is     None: sniffers      = {}
    if indexes     is     None: indexes       = {}
    if unknownVars is     None: unknownVars   = []
    if variables   is not None: removeUnknown = False
    if colnames    is not None: removeUnknown = False

    # Turn the unknonwVars list
    # into a list of variable IDs
    unknownVids = list(sorted({c.vid for c in unknownVars}))

    if isinstance(datafiles, six.string_types):
        datafiles = [datafiles]

    # We apply these cleaning steps by
    # omitting the relevant columns.
    loadFuncNames = ['remove', 'keepVisits']

    # Peek at the columns that
    # are in the input files.
    allcols = fileinfo.fileinfo(datafiles,
                                indexes=indexes,
                                sniffers=sniffers)[2]
    ncols   = len(list(it.chain(*allcols)))

    # re-organise the columns - a list of
    # columns for each variable ID. We do
    # this because, for a given VID, we
    # want to pass all columns at once to
    # the cleaning function(s) below.
    byvid = collections.defaultdict(list)
    for col in it.chain(*allcols):
        byvid[col.vid].append(col)

    # Build a full list of index
    # columns for each data file.
    indexes = [indexes.get(f, 0) for f in datafiles]

    # retrieve all cleaning steps -
    # we are only going to apply the
    # cleaning steps that will
    # determine whether or not a column
    # should be loaded
    mask    = vartable['Clean'].notna()
    cleans  = vartable['Clean'][mask]
    ppvids  = vartable.index[   mask]

    # Loop through all columns in
    # the data, and build a list of
    # the ones we want to load. The
    # end result will be an ordered
    # dict of { file : [column] }
    # mappings, and a list of columns
    # to drop.
    drop = []
    load = collections.OrderedDict([(f, []) for f in datafiles])
    for vid, cols in byvid.items():

        # index column - load it!
        # (the fileinfo function gives
        # index columns a variable ID
        # of 0).
        if vid == 0:
            for col in cols:
                load[col.datafile].append(col)
            continue

        # Variable is flagged as unknown,
        # and we have been told to ignore
        # unknown variables. Remember that
        # removeUnknown has no effect if
        # variables/column patterns have
        # been specified.
        if removeUnknown and vid in unknownVids:
            drop.extend(cols)
            continue

        # Figure out whether each
        # column should be loaded.
        # We load all columns which
        # pass either the variables
        # test or the colnames test
        # (or, if neither of those
        # options have been given,
        # all columns)
        loadflags = [(variables is None) and (colnames is None) for c in cols]

        # variable list has been specified,
        # and this vid is not in it - don't
        # load.
        if variables is not None:
            loadflags = [(vid in variables) for c in cols]

        # column names/patterns specified -
        # filter the list of columns based
        # on whether they match any of the
        # patterns specified.
        if colnames is not None:
            for i, col in enumerate(cols):
                hits = [fnmatch.fnmatch(col.name, pat) for pat in colnames]
                loadflags[i] = loadflags[i] or any(hits)

        for col, loadflag in list(zip(cols, loadflags)):
            if not loadflag:
                cols.remove(col)
                drop.append(col)

        if len(cols) == 0:
            continue

        # cleaning specified for this variable
        if vid in ppvids:

            # retrieve the cleaning functions
            # which affect whether or not a column
            # should get loaded. We remove these
            # functions from the variable table, as
            # they won't need to be called again.
            funcs = [cleans[vid].pop(n, None) for n in loadFuncNames]
            funcs = [f for f in funcs if f is not None]

            # call the functions, generate a new
            # set of columns for this variable
            newcols = cols
            for f in funcs:
                newcols = f.run(vartable, vid, newcols)

            drop.extend(list(set.difference(set(cols), set(newcols))))

            cols = newcols

        for col in cols:
            load[col.datafile].append(col)

    # Final step - the column lists for each
    # file are not necessarily ordered by
    # their position in the file. Re-order
    # them so they are.
    for fname, cols in list(load.items()):
        load[fname].sort(key=lambda c: c.index)

    log.debug('Identified %i / %i columns to be loaded',
              sum([len(c) for c in load.values()]), ncols)

    return load, drop


def loadData(datafiles,
             vartable,
             columns,
             nrows=None,
             subjects=None,
             subjectExprs=None,
             exclude=None,
             encoding=None,
             indexes=None,
             trustTypes=False,
             mergeAxis=None,
             mergeStrategy=None,
             loaders=None,
             pool=None,
             mgr=None,
             dryrun=False):
    """Load data from ``datafiles``, using :func:`mergeData` if multiple files
    are provided.

    :arg datafiles:     Path to the data file(s)

    :arg vartable:      Variable table

    :arg columns:       Dict of ``{ file : [Column] }`` mappings,
                        defining the columns to load, as returned by
                        :func:`columnsToLoad`.

    :arg nrows:         Number of rows to read at a time. Defaults to
                       :attr:`NUM_ROWS`.

    :arg subjects:      List of subjects to include.

    :arg subjectExprs:  List of subject inclusion expressions

    :arg exclude:       List of subjects to exclude

    :arg encoding:      Character encoding (or sequence of encodings, one
                        for each data file). Defaults to ``latin1``.

    :arg indexes:       Dict of ``{filename : index}`` mappings, specifying
                        the position of the column to use as the index.
                        Defaults to 0 (the first column).

    :arg trustTypes:    Assume that columns with known data type do not contain
                        any bad/unparseable values.

    :arg mergeAxis:     Merging axis to use when loading multiple data files -
                        see the :func:`mergeData` function. Defaults to
                        :attr:`MERGE_AXIS`.

    :arg mergeStrategy: Strategy for merging multiple data files - see the
                        :func:`mergeData` function. Defaults to
                        :attr:`MERGE_STRATEGY`.

    :arg loaders:       Dict of ``{ file : loaderName }`` mappings containing
                        custom loaders/sniffers to be used for specific files.
                        See the :mod:`.custom` module.

    :arg pool:          ``multiprocessing.Pool`` object for running tasks in
                        parallel.

    :arg mgr:           ``multiprocessing.Manager`` to use for sharing state.

    :arg dryrun:        If ``True``, the data is not loaded.

    :returns:           A tuple containing:

                         - A ``pandas.DataFrame`` containing the data,
                           or ``None`` if ``dryrun is True``.
                         - A list of :class:`.Column` objects representing the
                           columns that were loaded.
    """

    if mergeStrategy is None: mergeStrategy = MERGE_STRATEGY
    if mergeAxis     is None: mergeAxis     = MERGE_AXIS
    if loaders       is None: loaders       = {}
    if indexes       is None: indexes       = {}

    if isinstance(datafiles, six.string_types):
        datafiles = [datafiles]
    if encoding is None or isinstance(encoding, six.string_types):
        encoding = [encoding] * len(datafiles)

    # Get the format for each input file
    dialects, headers, names = fileinfo.fileinfo(
        datafiles, indexes, loaders)

    # load the data
    data       = []
    loadedcols = []
    for fname, fencoding, dialect, header, allcols in zip(
            datafiles, encoding, dialects, headers, names):

        toload = columns[fname]
        loader = loaders.get(fname, None)
        index  = indexes.get(fname, 0)

        if dryrun:
            fdata = None

        elif loader is not None:
            log.debug('Loading %s with custom loader %s', fname, loader)
            fdata = custom.runLoader(loader, fname)

        else:
            log.debug('Loading %s with pandas', fname)
            fdata = loadFile(fname,
                             vartable,
                             header,
                             dialect,
                             allcols,
                             toload,
                             index=index,
                             nrows=nrows,
                             subjects=subjects,
                             subjectExprs=subjectExprs,
                             exclude=exclude,
                             encoding=fencoding,
                             trustTypes=trustTypes,
                             pool=pool,
                             mgr=mgr)

        data      .append(fdata)
        loadedcols.append(toload)

    # Merge data from multiple files
    # into a single dataframe
    data, cols = merging.mergeDataFrames(
        data, loadedcols, mergeAxis, mergeStrategy, dryrun)

    # if a subject list was provided,
    # re-order the data according to
    # that list
    if (not dryrun) and subjects is not None:

        # if exclude/subjectExpr lists were
        # provided, and they overlap with
        # the subjects list, there will be
        # more IDs in the subject list than
        # the dataframe. Fix it.
        if len(data.index) != len(subjects):
            subjects = pd.Index(subjects, name=data.index.name)
            subjects = subjects.intersection(data.index, sort=False)
        data = data.loc[subjects, :]

    return data, cols


def loadFile(fname,
             vartable,
             header,
             dialect,
             allcols,
             toload,
             index=None,
             nrows=None,
             subjects=None,
             subjectExprs=None,
             exclude=None,
             encoding=None,
             trustTypes=False,
             pool=None,
             mgr=None):
    """Loads data from the specified file. The file is loaded in chunks of
    ``nrows`` rows, using the :func:`loadChunk` file.

    :arg fname:        Path to the data file

    :arg vartable:     Variable table

    :arg header:       ``True`` if the file has a header row, ``False``
                       otherwise.

    :arg dialect:      File dialect (see :func:`.fileinfo`).

    :arg allcols:      Sequence of :class:`.Column` objects describing all
                       columns in the file.

    :arg toload:       Sequence of :class:`.Column` objects describing the
                       columns that should be loaded, as generated by
                       :func:`columnsToLoad`.

    :arg index:        Column position of index column (starting from 0).
                       Defaults to 0.

    :arg nrows:        Number of rows to read at a time. Defaults to
                       attr:`NUM_ROWS`.

    :arg subjects:     List of subjects to include.

    :arg subjectExprs: List of subject inclusion expressions

    :arg exclude:      List of subjects to exclude

    :arg encoding:     Character encoding (or sequence of encodings, one
                       for each data file). Defaults to ``latin1``.

    :arg trustTypes:   Assume that columns with known data type do not contain
                       any bad/unparseable values.

    :arg pool:         ``multiprocessing.Pool`` object for running tasks in
                       parallel.

    :arg mgr:          ``multiprocessing.Manager`` to use for sharing state.

    :returns:          A ``pandas.DataFrame`` containing the data.
    """

    ownPool = pool is None
    toload  = list(toload)

    if index    is None: index    = 0
    if encoding is None: encoding = 'latin1'
    if nrows    is None: nrows    = NUM_ROWS
    if pool     is None: pool     = mpd.Pool(1)

    # The read_csv function requires the
    # index argument to be specified
    # relative to the usecols argument:
    #
    #   - https://stackoverflow.com/a/45943627
    #   - https://github.com/pandas-dev/pandas/issues/9098
    #   - https://github.com/pandas-dev/pandas/issues/2654
    #
    # So here we make index relative to
    # toload.
    index = [i for i, c in enumerate(toload) if c.index == index][0]

    # Figure out suitable data types to
    # store the data for each column.
    # pd.read_csv wants the date columns
    # to be specified separately.
    vttypes, dtypes = loadtables.columnTypes(vartable, toload)
    datecols        = [c.name for c, t in zip(toload, vttypes)
                       if t in (util.CTYPES.date, util.CTYPES.time)]

    # If we think there might be bad data
    # in the input (trustTypes is False),
    # only the types for date/time/non-numeric
    # columns are specified during load, and
    # we manually perform numeric conversion
    # after load, via the coerceToNumeric
    # function. This is to avoid pandas.read_csv
    # crashing on bad data - instead, we set bad
    # data to nan.
    if not trustTypes:
        dtypes = {n : t for n, t in dtypes.items()
                  if not np.issubdtype(t, np.number)}

    # input may or may not
    # have a header row
    if header: header = 0
    else:      header = None

    log.debug('Loading %u columns from %s: %s ...',
              len(toload) + 1, fname, [c.name for c in toload[:5]])

    # Prepare arguments to
    # the loadChunk function
    args = {'fname'        : fname,
            'vartable'     : vartable,
            'header'       : header,
            'allcols'      : allcols,
            'toload'       : toload,
            'index'        : index,
            'nrows'        : nrows,
            'subjects'     : subjects,
            'subjectExprs' : subjectExprs,
            'exclude'      : exclude,
            'encoding'     : encoding,
            'trustTypes'   : trustTypes,
            'dtypes'       : dtypes,
            'datecols'     : datecols}

    if dialect == 'whitespace':
        dlargs = {'delim_whitespace' : True}
    else:
        dlargs = {'delimiter'        : dialect.delimiter,
                  'doublequote'      : dialect.doublequote,
                  'escapechar'       : dialect.escapechar,
                  'skipinitialspace' : dialect.skipinitialspace,
                  'quotechar'        : dialect.quotechar,
                  'quoting'          : dialect.quoting,
                  'delim_whitespace' : False}

    args['dlargs'] = dlargs

    # Load chunks of rows separately,
    # so we can parallelise. We do this
    # by passing different offsets to
    # the loadChunk function.
    totalrows = util.wc(fname)
    offsets   = list(range(0, totalrows,  nrows))
    offsets   = [[i, o] for (i, o) in zip(range(len(offsets)), offsets)]

    log.debug('Loading %u rows in %u chunks', totalrows, len(offsets))

    func   = ft.partial(loadChunk, **args)
    chunks = pool.starmap(func, offsets)
    fdata  = pd.concat(chunks, axis=0)

    if ownPool:
        pool.close()
        pool.join()

    log.debug('Loaded %i rows from %s', len(fdata), fname)

    return fdata


def loadChunk(i,
              offset,
              fname,
              vartable,
              header,
              allcols,
              toload,
              index,
              nrows,
              subjects,
              subjectExprs,
              exclude,
              encoding,
              trustTypes,
              dtypes,
              datecols,
              dlargs):
    """Loads a chunk of ``nrows`` from ``fname``, starting at ``offset``.

    :arg i:            Chunk number, just used for logging.

    :arg offset:       Row number to start reading from.

    :arg fname:        Path to the data file

    :arg vartable:     Variable table

    :arg header:       ``True`` if the file has a header row, ``False``
                       otherwise.

    :arg allcols:      Sequence of :class:`.Column` objects describing all
                       columns in the file.

    :arg toload:       Sequence of :class:`.Column` objects describing the
                       columns that should be loaded, as generated by
                       :func:`columnsToLoad`.

    :arg index:        Column position of index column (starting from 0).
                       Defaults to 0.

    :arg nrows:        Number of rows to read at a time. Defaults to
                       attr:`NUM_ROWS`.

    :arg subjects:     List of subjects to include.

    :arg subjectExprs: List of subject inclusion expressions

    :arg exclude:      List of subjects to exclude

    :arg encoding:     Character encoding (or sequence of encodings, one
                       for each data file). Defaults to ``latin1``.

    :arg trustTypes:   Assume that columns with known data type do not contain
                       any bad/unparseable values.

    :arg dtypes:       A dict of ``{ column_name : dtype }`` mappings
                       containing a suitable internal data type to use for some
                       columns.

    :arg datecols:     List of column names denoting columns which should be
                       interpreted as dates/times.

    :arg dlargs:       Dict of arguments to pass through to
                       ``pandas.read_csv``.
    """

    allcolnames = [c.name for c in allcols]
    toloadnames = [c.name for c in toload]

    def shouldLoad(c):
        return c in toloadnames

    with warnings.catch_warnings():
        warnings.filterwarnings('ignore', module='pandas.io.parsers')
        warnings.filterwarnings('ignore', category=pd.errors.DtypeWarning)

        df = pd.read_csv(fname,
                         header=header,
                         names=allcolnames,
                         index_col=index,
                         dtype=dtypes,
                         usecols=shouldLoad,
                         parse_dates=datecols,
                         infer_datetime_format=True,
                         skiprows=offset,
                         nrows=nrows,
                         encoding=encoding,
                         **dlargs)
        gotrows = len(df)

        # If a subject/expression/exclude list
        # is provided, filter the rows accordingly
        df = removeSubjects(df, toload, subjects, subjectExprs, exclude)

        log.debug('Processing chunk %i (kept %i / %i rows)',
                  i + 1, len(df), gotrows)

        # If not trustTypes, we manually convert
        # each column to its correct type.
        #
        # We have to do this after load, as
        # pd.read_csv will raise an error if
        # a column that is specified as
        # numeric contains non-numeric data.
        # So we coerce data types after the
        # data has been loaded. This causes
        # non-numeric data to be set to nan.
        if not trustTypes:
            for i, c in enumerate(toload):
                if i == index:
                    continue
                df[c.name] = coerceToNumeric(vartable, df[c.name], c)

        return df


def removeSubjects(data,
                   cols,
                   subjects=None,
                   subjectExprs=None,
                   exclude=None):
    """Removes rows (subjects) from the data based on ``subjects`` to
    include, conditional ``subjectExprs``, and subjects to ``exclude``.

    :arg data:         A ``pandas.DataFrame`` instance.

    :arg allcols:      List of :class:`.Column` objects describing every column
                       in the data set.

    :arg subjects:     List of subjects to include.

    :arg subjectExprs: List of subject inclusion expressions

    :arg exclude:      List of subjects to exclude

    :returns:          A ``pandas.DataFrame``, potentially with rows removed.
    """

    if all((subjects     is None,
            subjectExprs is None,
            exclude      is None)):
        return data

    mask = None

    # ones to include, zeros to drop
    if subjects is not None:
        mask = data.index.isin(subjects)

    if subjectExprs is not None and len(subjectExprs) >= 1:
        exprmask = evaluateSubjectExpressions(data, cols, subjectExprs)
        # include rows listed in subjects
        # and which pass any expression
        if mask is not None: mask = mask & exprmask
        else:                mask = exprmask

    # exclude list overrides all of the above
    if exclude is not None:
        exclmask = data.index.isin(exclude)
        if mask is None: mask           = ~exclmask
        else:            mask[exclmask] = 0

    if mask is not None: return data[mask]
    else:                return data


def evaluateSubjectExpressions(data, allcols, subjectExprs):
    """Remove subjects (rows) from the data according to ``subjectExprs``.

    :arg data:         A ``pandas.DataFrame`` instance.

    :arg allcols:      List of :class:`.Column` objects describing every column
                       in the data set.

    :arg subjectExprs: List of strings containing expressions which identify
                       subjects to be included. Subjects for which *any*
                       expression evaluates to ``True`` will be included.

    :returns:          1D boolean ``numpy`` array containing ``True`` for
                       subjects to be included and ``False`` for subjects to
                       be excluded. Or ``None``, indicating that the
                       expressions were not evaluated (and all rows passed).
    """

    # build a {vid : [column]} mapping
    # to make life easy for the
    # evaluateSubjectExpression function
    colsbyvid = collections.defaultdict(list)
    for col in allcols:
        colsbyvid[col.vid].append(col)

    # evaluate each expression - we get
    # a numpy array for each of them
    exprmasks = []
    for i, expr in enumerate(subjectExprs):
        exprmask = evaluateSubjectExpression(data, expr, colsbyvid)
        if exprmask is not None:
            exprmasks.append(exprmask)

    # Any result which was not combined using
    # any() or all() defaults to being combined
    # with any(). For example, if "v123 >= 2"
    # is applied to columns 123-0.0, 123-1.0,
    # and 123-2.0, the final result will be
    # a 1D boolean array containing True where
    # any of the three columns were >= 2.
    for i, em in enumerate(exprmasks):
        if len(em.shape) == 2:
            exprmasks[i] = em.any(axis=1)

    # Finally, all expressions are combined in
    # the same manner - i.e. rows which passed
    # *any* of the expressions are included
    if   len(exprmasks) >  1: return ft.reduce(lambda a, b: a | b, exprmasks)
    elif len(exprmasks) == 1: return exprmasks[0]
    else:                     return None


def evaluateSubjectExpression(data, expr, cols):
    """Evaluates the given variable expression for each row in the data.

    :arg data: A ``pandas.DataFrame`` instance.

    :arg expr: String containing a variable expression

    :arg cols: Dict of ``{vid : [Column]}`` mappings

    :returns:  A boolean ``numpy`` array containing the result of evaluating
               the expression at each row, or ``None`` indicating that the
               expression was not evaluated (and every row passed).
    """

    expr = expression.Expression(expr)
    vids = expr.variables

    # Calculate the intersection of visits/
    # instances across all variables used in
    # the expression - we evaluate an
    # expression only on visits/instances
    # present for all variables in the
    # expression. All other visits/instances
    # are not considered.
    visits    = [[c.visit    for c in cols[v]] for v in vids]
    instances = [[c.instance for c in cols[v]] for v in vids]

    def intersection(a, b):
        return set(a).intersection(b)
    intersection = ft.partial(ft.reduce, intersection)

    visits    = intersection(visits)
    instances = intersection(instances)

    # Build a {vid : [column]} dict to pass
    # to the expression evaluate method
    exprcols = collections.defaultdict(list)
    for vid in vids:
        for col in cols[vid]:
            if col.visit in visits and col.instance in instances:
                exprcols[vid].append(col.name)

    if len(exprcols) == 0:
        log.debug('Ignoring expression (%s) - no associated '
                  'columns are present', str(expr))
        return None

    log.debug('Evaluating expression (%s) on columns %s',
              str(expr), list(it.chain(*exprcols.values())))

    return expr.evaluate(data, exprcols)


def coerceToNumeric(vartable, series, column):
    """Coerces the given column to numeric, if necessary.

    :arg vartable: The variable table

    :arg series:   ``pandas.Series`` containing the data to be coerced.

    :arg column:   :class:`.Column` object representing the column to coerce.

    :returns:      Coerced ``pandas.Series``
    """

    name      = column.name
    dtype     = loadtables.columnTypes(vartable, [column])[1]
    has_dtype = series.dtype
    exp_dtype = dtype.get(name, None)

    if (exp_dtype is not None)             and \
       np.issubdtype(exp_dtype, np.number) and \
       (has_dtype != exp_dtype):

        # We can't force a specific numpy
        # dtype *and* coerce bad values to
        # nan in one step. So we do it in
        # two steps: to_numeric handles
        # coercion to NaN, and astype casts
        # to the exact type.
        s = pd.to_numeric(series, errors='coerce')
        s = s.astype(exp_dtype, copy=False)

        return s

    return series
