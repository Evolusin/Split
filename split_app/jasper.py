# -*- coding: utf-8 -*-
import os
from pyreportjasper import PyReportJasper
from platform import python_version


def compiling():
    REPORTS_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports')
    input_file = os.path.join(REPORTS_DIR, 'Blank_A4.jrxml')
    output_file = os.path.join(REPORTS_DIR, 'report')
    conn = {
        # 'driver': 'sqlite',
        # 'username': '',
        # 'password': '',
        'jdbc_url': 'jdbc:sqlite:C:/Users/Komputer/Desktop/Programowanie/Split/db.sqlite3',
        # 'database': '',
        'jdbc_driver': 'sqlite',
        'jdbc_dir': 'C:/Users/Komputer/JaspersoftWorkspace/MyReports/'
    }
    pyreportjasper = PyReportJasper()
    pyreportjasper.config(
        input_file,
        output_file,
        db_connection=conn,
        output_formats=["pdf", "rtf"],
        parameters={'python_version': python_version()},
        locale='en_US'
    )
    pyreportjasper.process_report()


compiling()
