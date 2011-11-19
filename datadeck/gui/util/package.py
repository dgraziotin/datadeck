import os.path
import wx
import datadeck.gui.package
import download
import validator
import datadeck.operations
import datadeck.settings

class PackageUtil(object):
    def __init__(self, wxparent):
        self.m_wxparent = wxparent
        self.m_download = download.DownloadUtil(self.m_wxparent)

    def Info(self, package):
        if not package:
            return
        package_info = datadeck.gui.package.PackageGUI(self.m_wxparent, package)
        package_info.SetSize(wx.Size(500, 500))
        package_info.Center()
        package_info.Show(True)

    def Create(self, package, path):
        try:
            validator.PackageValidator.validate(package)
        except validator.PackageNonValid, e:
            wx.MessageBox(str(e), caption="Validation Error", style=wx.OK)
            return
        datadeck.operations.InitAndSaveOperation(self.m_wxparent, package, path)

    def Download(self, package):
        download_dir = self.m_download.DownloadDirDialog()
        if not download_dir:
            return

        overwrite_check = self.m_download.CheckPackageOverwrite(download_dir, package)

        if overwrite_check:
            datadeck.operations.DownloadOperation(self.m_wxparent, package, download_dir)

    def AlreadyExists(self, path, name):
        return validator.PackageValidator.already_existing(path, name)

    def Licenses(self, key=None):
        return datadeck.settings.Settings.licenses(key)

