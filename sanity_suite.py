# run_suite.py
import os
import pytest

if not os.path.exists("reports"):
    os.mkdir("reports")


pytest.main([
    '-v',
    '-m', 'sanity',
    '--html=reports/sanity_report.html',
    '--self-contained-html'
])
