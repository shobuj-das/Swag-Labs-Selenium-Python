# run_suite.py
import os
import pytest

if not os.path.exists("report"):
    os.mkdir("report")

pytest.main([
    'tests/test_login.py',
    'tests/test_inventory.py',
    '--html=report/report.html',
    '--self-contained-html'
])
