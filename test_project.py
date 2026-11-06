import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from process_project import process_project  # noqa: E402

def test_delete_column():
    matrix = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
    result = process_project(matrix, 1)
    assert result == [[2.0, 3.0], [5.0, 6.0]]
    