__author__ = "dgraziotin"
import os
import shutil
import wx
import datadeck.operations
import datadeck.settings

class DownloadUtil(object):
    """
    Utils for Downloading packages from the GUI
    """

    def __init__(self, wxframe):
        self.m_wxframe = wxframe

    def CheckPackageOverwrite(self, download_dir, package):
        """
        Given a Package and a path, it checks if the Package is already installed at download_dir.
        It asks the user to overwrite it.
        Returns True if the package must be overwritten and deletes the old package, False if the user aborts.
        Returns True if the package does not exist, and therefore can be "overwritten"
        """
        package_path = download_dir + os.sep + package.name
        if os.path.exists(package_path):
            message = "Overwrite " + package.name + "?"
            box = wx.MessageDialog(self.m_wxframe, message, "Overwrite?", wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
            overwrite = box.ShowModal()
            if overwrite == wx.ID_YES:
                shutil.rmtree(package_path, ignore_errors=True)
                return True
            else:
                return False
        else:
            return True

    def DownloadDirDialog(self, path=None, message="Choose a Download Directory"):
        """
        Create a DirDialog for choosing the directory in which we save the Package
        """
        if not path:
            path = datadeck.settings.Settings.library_path()
        dialog = wx.DirDialog(self.m_wxframe, message, path)
        if dialog.ShowModal() == wx.ID_OK:
            download_dir = dialog.GetPath()
            return download_dir
        else:
            return None
