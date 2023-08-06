#!/usr/bin/env python
#
# test_datatable.py -
#
# Author: Paul McCarthy <pauldmccarthy@gmail.com>
#

import multiprocessing as mp

import numpy as np

from . import gen_DataTable


def _parallel_task(dtable, factor):
    for col in dtable.allColumns[1:]:
        flag = 'mul {}'.format(factor)
        dtable[:, col.name] = dtable[:, col.name] * factor
        dtable.addFlag(col, flag)

        if factor % 2: col.metadata = flag
        else:          col.metadata = None
    return dtable


def test_subtable_merge_columns():

    data      = np.random.randint(1, 10, (10, 4))
    dtable    = gen_DataTable(data)
    cols      = dtable.allColumns[1:]
    subtables = [dtable.subtable([c]) for c in cols]
    factors   = np.arange(1, len(subtables) + 1)

    for col, fac in zip(cols, factors):
        dtable.addFlag(col, 'origflag')
        col.metadata = 'origmeta'

    with mp.Pool(8) as pool:
        subtables = pool.starmap(_parallel_task, zip(subtables, factors))

    for st in subtables:
        dtable.merge(st)

    for i, (col, fac) in enumerate(zip(dtable.allColumns[1:], factors)):
        expflag = 'mul {}'.format(fac)
        expdata = data[i, :] * fac

        assert np.all(dtable[:, col.name] == expdata)
        assert dtable.getFlags(col) == set(('origflag', expflag))
        if fac % 2: assert col.metadata == expflag
        else:       assert col.metadata == 'origmeta'


def test_subtable_merge_rows():

    data      = np.random.randint(1, 10, (4, 100))
    dtable    = gen_DataTable(data)
    chunks    = [dtable.index[i:i + 10] for i in range(0, 100, 10)]
    subtables = [dtable.subtable(rows=c) for c in chunks]
    factors   = np.arange(1, len(subtables) + 1)

    for col in dtable.allColumns[1:]:
        dtable.addFlag(col, 'origflag')

    with mp.Pool(8) as pool:
        subtables = pool.starmap(_parallel_task, zip(subtables, factors))

    for st in subtables:
        dtable.merge(st)

    expflags = set(['origflag'] + ['mul {}'.format(f) for f in factors])

    for col in dtable.allColumns[1:]:
        assert dtable.getFlags(col) == expflags

    for i, (chunk, fac) in enumerate(zip(chunks, factors)):
        expdata = data[:, chunk - 1] * fac

        print('chunk', i, expdata.shape, 'from', data.shape)
        print('compare with', dtable[chunk, :].shape)
        print(dtable[chunk, :])
        print(expdata.T)

        assert np.all(dtable[chunk, :] == expdata.T)
