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
units = 1500
timings = {}

i = 2
elems = 0
while i < units:
    elems += 1
    i = int(i)
    i += 5 * np.log(i)

print('elems {}'.format(elems))

x = [0 for j in range(elems)]
y = [[0 for j in range(elems)] for i in range(3)]

result = open('result.txt', 'w')

for mode in range(1, 4):
    i = 2
    per_try = {}
    idx = 0
    while i < units:
        i = int(i)
        print('Start benchmark with {} units, mode {}'.format(str(i), str(mode)))
        print('Start benchmark with {} units, mode {}'.format(str(i), str(mode)), file=result)
        app_start = timer()
        app = pywinauto.Application(backend='uia').start(cmd_line=os.path.join(benchmark_folder, 'Benchmark.exe') + ' ' + str(mode) + ' ' + str(i) + ' 1')
        app.Form1.wait('ready', timeout=3600)
        app_ready = timer()
        print('Benchmark ready {}'.format(str(app_ready - app_start)))
        dlg = app.Form1
        median_value = 0.0

        for j in range(5):
            start = timer()
            dlg.dump_tree(need_print=False, filename=result)
            end = timer()
            median_value += end - start

        median_value /= 5
        x[idx] = i
        y[mode - 1][idx] = median_value
        idx += 1
        per_try[i] = median_value
        timings[mode] = per_try

        app.kill()
        i += 5 * np.log(i)

print('X:', file = result)
print(x, file = result)
print('Y:', file = result)
print(y, file = result)

result.close()

'''

#Saved results of approximately 18 hours of measurements
# with graphics plot

x = np.array([2, 5, 13, 25, 41, 59, 79, 100, 123, 147, 171, 196, 222, 249, 276, 304, 332, 361, 390, 419, 449, 479, 509, 540, 571, 602, 634, 666, 698, 730, 762, 795, 828, 861, 894, 927, 961, 995, 1029, 1063, 1097, 1132, 1167, 1202, 1237, 1272, 1307, 1342, 1378, 1414, 1450, 1486], dtype=float)
y1 = np.array([0.47103392, 0.4750155399999999, 0.5398734000000001, 0.6163620400000006, 0.711343459999999, 0.8435540200000006, 1.0356411600000002, 1.1561647800000003, 1.3257543199999986, 1.4740754800000004, 1.7157531400000026, 1.8138902000000001, 2.199442220000003, 2.2024798599999995, 2.0436173800000006, 2.1507971600000046, 2.5610539800000027, 2.4528468799999983, 2.659853400000003, 2.7970295599999986, 2.963991199999998, 3.108035739999997, 3.306645919999994, 3.394986820000008, 3.5048116800000004, 3.7652645799999847, 3.901600719999988, 4.03017956000001, 4.19606647999999, 4.537910579999993, 4.595045459999994, 5.13427539999999, 5.053882799999997, 5.136756300000013, 5.424930080000013, 5.7003086000000165, 5.90927655999999, 5.96010140000003, 6.3592457800000375, 6.465665339999987, 6.807956619999982, 7.003065700000002, 7.276001940000015, 7.569246019999992, 7.809192399999984, 8.10496598000002, 8.29186325999999, 8.794935139999984, 8.714646459999994, 9.226827579999963, 9.256219940000028, 9.705644119999988], dtype=float)
y2 = np.array([0.4719757600000321, 0.5011504399999467, 0.6241311799999949, 0.8779230400000415, 1.4017512599999917, 2.219871860000012, 3.3414261400000216, 4.484643159999996, 6.1823422200000095, 7.997941659999969, 10.226308159999963, 12.83788583999999, 15.723223199999984, 19.29694836000008, 22.622156240000002, 26.954692860000023, 31.325562660000013, 36.59406322000014, 42.25303407999991, 48.05528991999999, 54.52239522, 61.203231779999804, 69.07523946, 76.80626911999988, 85.60975355999999, 94.52642057999984, 103.15889330000009, 113.23202942000026, 124.21496546000017, 136.00868888000022, 148.67845024, 161.7314228199999, 174.48054501999977, 181.72099385999974, 193.40810928000064, 210.15853688000024, 223.15993392000055, 241.2193722, 256.64957663999996, 277.7354454600005, 370.5558249599999, 423.2613917399991, 452.32104365999913, 471.7883509799998, 483.79196701999973, 510.0794065600006, 546.9287494799995, 561.7432448800013, 488.15891692, 518.83941604, 551.2796160400001, 578.1017771999992], dtype=float)
y3 = np.array([0.4743702000021585, 0.5174026400010916, 0.6820898199992371, 1.0132770000011078, 1.6327099200017983, 2.5151068999999553, 3.7415791599996737, 5.186988399999973, 6.9302444999993895, 9.221718920000422, 11.06113866000087, 12.084584200000972, 13.536786360001134, 14.255486939998809, 15.442005039998913, 16.77575909999723, 17.98334885999939, 19.309359960001892, 20.619291419998625, 21.86662652000232, 23.236356699999305, 24.763179699999455, 25.95951434000017, 27.376459619999515, 29.1096458, 30.514065919998394, 31.906688280000527, 34.3044848399979, 34.98214165999961, 36.613314659999745, 38.51258271999977, 40.299355079997625, 42.025579859998835, 43.77530044000014, 45.23409563999739, 49.04278244000015, 48.86199966000131, 51.15402243999997, 53.04160287999839, 54.53347959999955, 56.39854608000169, 58.57629005999915, 61.03580747999949, 63.13150658000086, 64.68702778000151, 69.0307656799996, 70.31727994000103, 72.92458936000185, 72.98800142000255, 75.67913514000247, 72.82855035999964, 75.70667073999793], dtype=float)

xi=np.linspace(np.min(x),np.max(x),100, endpoint=True)
t = np.linspace(np.min(x),np.max(x),100, endpoint=True)
rbf1 = interpolate.Rbf(x,y1)
fi1 = rbf1(xi)
rbf2 = interpolate.Rbf(x,y2)
fi2 = rbf2(xi)
rbf3 = interpolate.Rbf(x,y3)
fi3 = rbf3(xi)

fig, axs = plt.subplots(3, 1, constrained_layout=True)

axs[0].set_title('Mode 1 benchmark')
axs[0].set_xlabel('Number of elements')
axs[0].set_ylabel('Time (seconds)')
axs[0].plot(x, y1, 'bo')
axs[0].plot(xi, fi1, 'g', label="Interpolated function")
axs[0].plot(t, 0.006 * t, 'r--', label="y = 0.006t")
axs[0].legend()


axs[1].set_title('Mode 2 benchmark')
axs[1].set_xlabel('Number of elements')
axs[1].set_ylabel('Time (seconds)')
axs[1].plot(x, y2, 'bo')
axs[1].plot(xi, fi2, 'g', label="Interpolated function")
axs[1].plot(t, 0.0003 * (t ** 2), 'r--', label="y = 0.0003t^2")
axs[1].legend()


axs[2].set_title('Mode 3 benchmark')
axs[2].set_xlabel('Number of elements')
axs[2].set_ylabel('Time (seconds)')
axs[2].plot(x, y3, 'bo')
axs[2].plot(xi, fi3, 'g', label="Interpolated function")
axs[2].plot(t, 0.05 * t, 'r--', label="y = 0.05t")
axs[2].legend()


fig.suptitle('Dependence of time on the type and number of elements in the application')
plt.show()
'''

