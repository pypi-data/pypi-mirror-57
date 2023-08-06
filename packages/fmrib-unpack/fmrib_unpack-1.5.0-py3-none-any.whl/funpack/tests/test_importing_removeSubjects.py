#!/usr/bin/env python
#
# test_importing_removeSubjects.py -
#
# Author: Paul McCarthy <pauldmccarthy@gmail.com>
#

import pytest

import pandas as pd
import numpy as np

import funpack.importing as importing

from . import gen_DataTable, gen_DataTableFromDataFrame


def test_removeSubjects():

    data = np.random.randint(1, 10, (10, 500))

    # Options in order of precedence:
    #
    #   - exclude:  list of subjects to *exclude*
    #   - exprs:    list of expressions specifying *inclusion*

    # pass through
    dtable = gen_DataTable(data)
    importing.removeSubjects(dtable)
    assert np.all(dtable.index == np.arange(1, 501))
    assert np.all(dtable[:, :] == data.T)

    # exclude
    dtable = gen_DataTable(data)
    importing.removeSubjects(dtable, exclude=[1, 2, 3])
    assert np.all(dtable.index ==         np.arange(4, 501))
    assert np.all(dtable[:, :] == data[:, np.arange(3, 500)].T)

    # expr
    mask     = data[0, :] > 5
    dtable = gen_DataTable(data)
    importing.removeSubjects(dtable, exprs=['v1 > 5'])
    assert np.all(dtable.index == (np.where(mask)[0] + 1))
    assert np.all(dtable[:, :] == data[:, mask].T)

    # expr + exclude
    mask     = data[0, :] > 5
    mask[:3] = 0
    dtable = gen_DataTable(data)
    importing.removeSubjects(dtable, exprs=['v1 > 5'], exclude=[1, 2, 3])
    assert np.all(dtable.index == (np.where(mask)[0] + 1))
    assert np.all(dtable[:, :] == data[:, mask].T)

    # multiple expressions
    dtable = gen_DataTable(data)
    importing.removeSubjects(dtable, exprs=['v1 > 5', 'v2 == 9'])
    mask = (data[0, :] > 5) | (data[1, :] == 9)
    assert np.all(dtable.index == np.where(mask)[0] + 1)
    assert np.all(dtable[:, :] == data[:, mask].T)


def test_removeSubjects_multiple_columns():

    def gendata():
        cols       = ['eid', '1-0.0', '1-1.0', '1-2.0', '2-0.0', '2-1.0']
        variables  = [        1,       1,       1,       2,       2]
        data       = np.random.randint(1, 10, (6, 500))
        data[0, :] = np.arange(1, 501)
        df         = pd.DataFrame({c : d for c, d in zip(cols, data)})
        df         = df.set_index('eid')
        data       = data[1:, :].T
        return gen_DataTableFromDataFrame(df, variables=variables), data

    def all(s): return s.all(axis=1)
    def any(s): return s.any(axis=1)

    # combine vars with ncolumn
    # mismatch - error
    dtable = gendata()[0]
    exprs = ['v1 > 2 && v2 < 7']
    with pytest.raises(ValueError):
        importing.removeSubjects(dtable, exprs=exprs)

    # combine columns within var
    dtable, data = gendata()
    exprs = ['all(v1 > 2) && any(v2 < 7)']
    exp = all(data[:, :3] > 2) & any(data[:, 3:] < 7)
    exp = dtable.index[exp]
    importing.removeSubjects(dtable, exprs=exprs)
    assert (dtable.index == exp).all()

    # no combining columns - should
    # default to any
    dtable, data = gendata()
    exprs = ['v1 > 6']
    exp = any(data[:, :3] > 6)
    exp = dtable.index[exp]
    importing.removeSubjects(dtable, exprs=exprs)
    assert (dtable.index == exp).all()

    # multipler expressions - ORed together
    dtable, data = gendata()
    exprs = ['v1 > 6', 'v2 < 4']
    exp = any(data[:, :3] > 6) | any(data[:, 3:] < 4)
    exp = dtable.index[exp]
    importing.removeSubjects(dtable, exprs=exprs)
    assert (dtable.index == exp).all()
