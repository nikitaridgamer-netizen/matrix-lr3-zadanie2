from process_project import process_project
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))


def test_delete_column():
    matrix = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
    result = process_project(matrix, 1)
    assert result == [[2.0, 3.0], [5.0, 6.0]]
