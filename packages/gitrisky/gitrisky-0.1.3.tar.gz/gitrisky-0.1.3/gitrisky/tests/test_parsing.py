import mock

import numpy as np
import pandas as pd

from gitrisky.parsing import get_labels


@mock.patch('gitrisky.parsing.get_features')
@mock.patch('gitrisky.parsing.get_bugfix_commits')
@mock.patch('gitrisky.parsing.link_fixes_to_bugs')
def test_get_labels(m_link_fixes, m_get_bugfix, m_get_features):

    m_get_features.return_value = pd.DataFrame([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]],
        index=['a', 'b', 'c'])

    # test case where we find bug fix commits
    m_link_fixes.return_value = ['b', 'c']

    labels = get_labels()

    assert np.array_equal(labels, [0, 1, 1])
