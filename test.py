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
from pywinauto.application import Application  # noqa: E402
from pywinauto.sysinfo import is_x64_Python  # noqa: E402
from pywinauto import actionlogger  # noqa: E402
from pywinauto.actionlogger import ActionLogger  # noqa: E402
from pywinauto.timings import Timings  # noqa: E402
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
timings = {}
for i in range(10, 11, 10):
    app = Application(backend='uia')
    print('Start benchmark with {} edit boxes'.format(str(i)))
    app.start(cmd_line=os.path.join(benchmark_folder, 'Benchmark.exe') + ' ' + str(i) + ' 1')
    app.Form1.wait('ready', timeout=20)
    dlg = app.Form1
    median_value = 0.0

    for j in range(1):
        start = timer()
        dlg.dump_tree(rules=[1], need_print=False)
        end = timer()
        median_value += end - start

    #print(dlg.descendants(control_type='Edit'))
    median_value /= 10
    print('time has passed {}'.format(median_value))
    timings[i] = median_value

    app.kill()

print('=====================')
print('Final result:')
print(timings)