#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  dialogs.py
#
#  Copyright 2019 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#

import os
import wx
from domdf_wxpython_tools.validators import CharValidator


def file_dialog_multiple(parent, extension, title, filetypestring, style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT, **kwargs):
	"""
	
	:param parent:
	:type parent:
	:param extension:
	:type extension:
	:param title:
	:type title:
	:param filetypestring:
	:type filetypestring:
	:param style:
	:type style:
	:param kwargs:
	:type kwargs:
	
	:return:
	:rtype:
	"""
	
	with wx.FileDialog(
			parent, title,
			wildcard=f"{filetypestring} (*.{extension.lower()})|*.{extension.lower()};*.{extension.upper()}",
			style=style, **kwargs
	) as fileDialog:
		
		if fileDialog.ShowModal() == wx.ID_CANCEL:
			return  # the user changed their mind
		
		# print(style)
		# print(wx.FD_MULTIPLE in style)
		
		try:
			pathnames = fileDialog.GetPaths()
		except:
			pathnames = [fileDialog.GetPath()]
		
		# print(pathnames)
		
		for index, pathname in enumerate(pathnames):
			if extension != "*":
				if os.path.splitext(pathname)[-1].lower() != f".{extension}":
					pathnames[index] = pathname + f".{extension}"
		# else:
		# 	pathnames[index] = os.path.splitext(pathname)[0]
		
		return pathnames


def file_dialog(*args, **kwargs):
	"""

	:param parent:
	:type parent:
	:param extension:
	:type extension:
	:param title:
	:type title:
	:param filetypestring:
	:type filetypestring:
	:param style:
	:type style:
	:param kwargs:
	:type kwargs:

	:return:
	:rtype:
	"""
	
	paths = file_dialog_multiple(*args, **kwargs)
	
	if paths is not None:
		return paths[0]


class FloatEntryDialog(wx.TextEntryDialog):
	"""

	Based on http://wxpython-users.1045709.n5.nabble.com/Adding-Validation-to-wx-TextEntryDialog-td2371082.html
	"""
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		textctrl = self.FindWindowById(3000)
		
		textctrl.SetValidator(CharValidator("float-only"))


class IntEntryDialog(wx.TextEntryDialog):
	"""

	Based on http://wxpython-users.1045709.n5.nabble.com/Adding-Validation-to-wx-TextEntryDialog-td2371082.html
	"""
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		textctrl = self.FindWindowById(3000)
		
		textctrl.SetValidator(CharValidator("int-only"))

