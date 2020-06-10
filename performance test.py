from __future__ import print_function

import sys
#import ctypes
import time
from datetime import datetime
#import pdb
import os
import win32api
import six
import logging

sys.path.append(".")
import pywinauto
from pywinauto import actionlogger  # noqa: E402
from pywinauto.timings import wait_until  # noqa: E402
from pywinauto import mouse  # noqa: E402
from pywinauto.application import Application  # noqa E402
from pywinauto.controls.hwndwrapper import HwndWrapper  # noqa E402
from pywinauto.controls.hwndwrapper import InvalidWindowHandle  # noqa E402
from pywinauto.controls.hwndwrapper import get_dialog_props_from_handle  # noqa E402
from pywinauto.findwindows import ElementNotFoundError  # noqa E402
from pywinauto.sysinfo import is_x64_Python  # noqa E402
from pywinauto.sysinfo import is_x64_OS  # noqa E402
from pywinauto.timings import Timings  # noqa E402
from pywinauto import clipboard  # noqa E402
from pywinauto.base_wrapper import ElementNotEnabled  # noqa E402
from pywinauto.base_wrapper import ElementNotVisible  # noqa E402
from pywinauto import findbestmatch  # noqa E402
from pywinauto import keyboard  # noqa E402
from timeit import default_timer as timer

import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

controlspy_folder = os.path.join(
    os.path.dirname(__file__), r".\apps\controlspy0998")
controlspy_folder_32 = controlspy_folder
mfc_samples_folder = os.path.join(
    os.path.dirname(__file__), r".\apps\MFC_samples")
mfc_samples_folder_32 = mfc_samples_folder
benchmark_folder = os.path.join(
    os.path.dirname(__file__), r".\apps\Benchmark")
if is_x64_Python():
    mfc_samples_folder = os.path.join(mfc_samples_folder, 'x64')
winforms_folder = os.path.join(
    os.path.dirname(__file__), r".\apps\WinForms_samples")
winforms_folder_32 = winforms_folder

Timings.fast()
units = 801
timings = {}

col_count = 1
seed = 0

#result = open('result.txt', 'w')

for mode in range(1, 2):
    i = 800
    while i < units:
        i = int(i)
        print('Start benchmark with {} units, mode {}'.format(str(i), str(mode)))
        #print('Start benchmark with {} units, mode {}'.format(str(i), str(mode)), file=result)
        app_start = timer()
        app = pywinauto.Application(backend='uia').start(cmd_line=os.path.join(benchmark_folder, 'Benchmark.exe') + ' ' + str(mode) + ' ' + str(i) + ' ' + str(col_count) + ' ' + str(seed))
        app.Dialog.wait('ready', timeout=3600)
        app_ready = timer()
        print('Benchmark ready {}'.format(str(app_ready - app_start)))
        dlg = app.Dialog
        #dlg.dump_tree()
        print("")
        print('Click!')
        median_value = 0.0
        for j in range(5):
            find_start = timer()
            button = dlg.hWvgX5BS.window_text()
            #edit = dlg.Edit2.window_text()
            #edit = dlg.jolYCYuREdit.window_text()
            find_ready = timer()
            median_value += find_ready - find_start
        median_value /= 5
        print('hWvgX5BS is matched {}'.format(str(median_value)))
        #print('Edit2 is matched {}'.format(str(median_value)))


        app.kill()
        i += 5 * np.log(i)