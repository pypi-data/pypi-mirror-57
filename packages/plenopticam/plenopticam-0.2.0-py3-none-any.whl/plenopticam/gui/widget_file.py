#!/usr/bin/env python

__author__ = "Christopher Hahne"
__email__ = "inbox@christopherhahne.de"
__license__ = """
    Copyright (c) 2019 Christopher Hahne <inbox@christopherhahne.de>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

import os

from plenopticam.gui.widget_path import PathWidget
from plenopticam.gui.constants import PX, PY, GENERIC_EXTS, LYT_LFP_EXTS, LYT_CAL_EXTS, ALL_EXTS

class FileWidget(tk.Frame):

    def __init__(self, parent):

        # inheritance
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.cfg = parent.cfg

        # supported file extensions
        LFP_EXTS = [('Supported files', ' '.join(LYT_LFP_EXTS+GENERIC_EXTS)),
                    ('Lytro files', ' '.join(LYT_LFP_EXTS)),
                    ('Generic image files', ' '.join(GENERIC_EXTS)),
                    ('All files', ' '.join(ALL_EXTS))]
        CAL_EXTS = [('Supported files', ' '.join(LYT_CAL_EXTS+GENERIC_EXTS)),
                    ('Lytro files', ' '.join(LYT_CAL_EXTS)),
                    ('Generic image files', ' '.join(GENERIC_EXTS)),
                    ('All files', ' '.join(ALL_EXTS))]

        # instantiate light field path widget
        tk.Label(self, text='Light field image: ').grid(row=0, column=0, sticky='W')
        self.lfp_wid = PathWidget(self, path=self.cfg.params[self.cfg.lfp_path], path_type=False, file_exts=LFP_EXTS)
        self.lfp_wid.grid(row=0, column=1, padx=PX, pady=PY)
        self.lfp_wid.bind_to(self.set_lfp_path)     # observe change in path variable

        # instantiate calibration path widget
        tk.Label(self, text='Calibration source: ').grid(row=1, column=0, sticky='W')
        self.cal_wid = PathWidget(self, path=self.cfg.params[self.cfg.cal_path], path_type=False, file_exts=CAL_EXTS)
        self.cal_wid.grid(row=1, column=1, padx=PX, pady=PY)
        self.cal_wid.bind_to(self.set_cal_path)     # observe change in path variable

        # radio button to enable change from path to file type
        self.cal_wid.path_type = os.path.isdir(self.cfg.params[self.cfg.cal_path])
        self.chk_var = tk.BooleanVar(value=bool(self.cal_wid.path_type))
        self.chk_btn = tk.Checkbutton(self, text='Pick folder', variable=self.chk_var, command=self.btn_update)
        self.chk_btn.grid(row=1, column=2, sticky='W')

        # list of button and entry widgets (collected to disable/enable widgets)
        self.btn_list = [self.lfp_wid.btn, self.cal_wid.btn, self.chk_btn, self.lfp_wid.ent, self.cal_wid.ent]

    def btn_update(self):
        # toggle path type in PathWidget for calibration
        self.cal_wid.path_type = not self.cal_wid.path_type

    def set_lfp_path(self, val):

        self.cfg.params[self.cfg.lfp_path] = val
        self.cfg.save_params()

    def set_cal_path(self, val):

        self.cfg.params[self.cfg.cal_path] = val
        self.cfg.save_params()
