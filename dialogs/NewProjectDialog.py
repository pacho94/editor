#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Beremiz, a Integrated Development Environment for
# programming IEC 61131-3 automates supporting plcopen standard and CanFestival.
# This file is based on code written for Whyteboard project.
#
# Copyright (c) 2025 by pacho94
#
# See COPYING file for copyrights details.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#


"""
This module contains classes extended from wx.Dialog used by the GUI.
"""

import os
from wx.lib.agw.hyperlink import HyperLinkCtrl
import wx

import targets
import util.paths as paths
current_dir = paths.AbsDir(__file__)

class NewProjectDialog(wx.Dialog):
    """
    A replacement About Dialog for Windows, as it uses a generic frame that
    well...sucks.
    """
    def __init__(self, parent):
        title = _("New Project")
        wx.Dialog.__init__(self, parent, title=title, style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)
        self.SetSize((480, 150))
        self.SetMinSize((480, 150))
        self.SetMaxSize((480, 640))

        if parent and parent.GetIcon():
            self.SetIcon(parent.GetIcon())

        infos_sizer = wx.FlexGridSizer(cols=2, hgap=5, rows=2, vgap=15)
        # Set to full width
        infos_sizer.SetMinSize(470, 0)
        infos_sizer.AddGrowableCol(1)
        project_name_label = wx.StaticText(self, label=_('Project Name:'))
        infos_sizer.Add(project_name_label, border=4,
                              flag=wx.ALIGN_CENTER_VERTICAL | wx.TOP)
        self.project_name = wx.TextCtrl(self)
        infos_sizer.Add(self.project_name, flag=wx.GROW)
        target_type_label = wx.StaticText(self, label=_('Target Type:'))
        infos_sizer.Add(target_type_label, border=4,
                              flag=wx.ALIGN_CENTER_VERTICAL | wx.TOP)

        self.target_type = wx.ComboBox(self, style=wx.CB_READONLY)
        # Add types
        for target_name in targets.GetTargetNames():
            self.target_type.Append(target_name)
        # Select first element
        self.target_type.SetStringSelection(targets.GetTargetNames()[0])
        infos_sizer.Add(self.target_type, flag=wx.GROW)

        ok = wx.Button(self, id=wx.ID_OK, label=_("&Ok"))
        close = wx.Button(self, id=wx.ID_CANCEL, label=_("&Close"))

        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
        btn_sizer.Add(ok, flag=wx.CENTER | wx.RIGHT, border=5)
        btn_sizer.Add(close, flag=wx.CENTER | wx.RIGHT, border=5)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(infos_sizer, flag=wx.CENTER | wx.BOTTOM, border=5)
        sizer.Add(btn_sizer, flag=wx.CENTER | wx.BOTTOM, border=5)

        container = wx.BoxSizer(wx.VERTICAL)
        container.Add(sizer, flag=wx.ALL, border=10)
        self.SetSizer(container)
        self.Layout()
        self.Fit()
        self.Centre()
        self.Show(True)
        self.SetEscapeId(close.GetId())

        close.Bind(wx.EVT_BUTTON, lambda evt: self.Destroy())

    def GetType(self):
        return self.target_type.GetStringSelection()

    def GetProjectName(self):
        return self.project_name.GetValue()