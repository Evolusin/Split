# -*- coding: utf-8 -*-
import os
from pyreportjasper import PyReportJasper


def compiling():
    REPORTS_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports')
    input_file = os.path.join(REPORTS_DIR, 'Blank_A4.jasper')
    output_file = os.path.join(REPORTS_DIR, 'csv')
    pyreportjasper = PyReportJasper()
    pyreportjasper.compile(write_jasper=True)