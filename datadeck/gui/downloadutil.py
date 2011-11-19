__author__ = "dgraziotin"
"""
Contains useful utilities called by the GUI for doing GUI things.
"""
import os
import shutil
import wx
import datadeck.operations
import datadeck.settings

class DownloadUtil(object):

    def __init__(self, wxframe):
        self.wxframe = wxframe

    def CheckPackageOverwrite(self, download_dir, package):
        package_path = download_dir + os.sep + package.name
        if os.path.exists(package_path):
            message = "Overwrite " + package.name + "?"
            box = wx.MessageDialog(self.wxframe, message, "Overwrite?", wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
            overwrite = box.ShowModal()
            if overwrite == wx.ID_YES:
                shutil.rmtree(package_path, ignore_errors=True)
                return True
            else:
                return False
        else:
            return True

    def DownloadDirDialog(self, path=None):
        """
        Create a DirDialog for choosing the directory in which we save the Package
        """
        dialog = wx.DirDialog(self.wxframe, "Choose a Download Directory", datadeck.settings.Settings.datadeck_default_path())
        if dialog.ShowModal() == wx.ID_OK:
            download_dir = dialog.GetPath()
            return download_dir
        else:
            return None
