__author__ = 'dgraziotin'
"""
Module holding the Download utilities
Coding standard: http://www.wxpython.org/codeguidelines.php
"""

import lib
import wx
import os

class Download(object):
    @staticmethod
    def DirDialog(parent):
        dialog = wx.DirDialog(parent, "Choose a Download Directory", os.getcwd())
        if dialog.ShowModal() == wx.ID_OK:
            download_dir = dialog.GetPath()
            return download_dir
        dialog.Destroy()

    @staticmethod
    def Download(parent, package):
        download_dir = Download.DirDialog(parent)
        if download_dir:
            lib.download("ckan://" + package.name, download_dir)
            return True
        else:
            return False