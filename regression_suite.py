# run_suite.py
import os
import pytest

if not os.path.exists("reports"):
    os.mkdir("reports")

test_files_sequence =[
    'tests/test_login.py',
    'tests/test_inventory.py',
]

pytest.main([
    *test_files_sequence,
    '-v',
    '-m', 'regression',
    '--html=reports/regression_report.html',
    '--self-contained-html'
])
