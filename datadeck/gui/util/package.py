"""
This module holds GUI utilities for handling/representing Packages
"""
import wx
import datadeck.gui.package
import download
import validator
import datadeck.operations
import datadeck.settings
import dpm.lib

class PackageList(object):
    """
    Represents a list of Packages. It is useful for mapping GUI lists (wx.ListCtrl) for search results
    and for the Package Library. Don't use it, inherit from it.
    """
    def __init__(self, wxlistctrl):
        self.m_wxlistctrl = wxlistctrl
        self.m_packages = []

    def Index(self):
        """
        For ensuring consistency with the GUI package list, returns the current length
        of the internal package list - 1.
        This is because a package is first added to the internal list, then to the GUI list.
        Therefore, the first package added in the GUI must have index = 0, not 1.
        The second package added in the GUI must have index = 1, not 2.
        Etc.
        """
        return len(self.m_packages) - 1

    def Get(self, index):
        """
        Given an Index, returns the corresponding Package
        """
        return self.m_packages[index]

    def Add(self, package):
        """
        Adds a package in the internal results list.
        Returns the index that points to the added package.
        """
        self.m_packages.append(package)
        self._AddWxListrCtrl(package)
        return self.Index()

    def _AddWxListrCtrl(self, package):
        """
        Implement here the code for adding a package in the wx.ListCtrl
        """
        raise NotImplementedError("Inherit from this class, don't use it")


    def Clear(self):
        """
        Clears the internal list
        """
        self.m_wxlistctrl.DeleteAllItems()
        self.m_packages = []

class SearchResults(PackageList):
    """
    A PackageList for search results
    """
    def __init__(self, wxlistctrl):
        PackageList.__init__(self, wxlistctrl)

    def _AddWxListrCtrl(self, package):
        name = package.metadata['name'] if package.metadata['name'] else "N/A"
        notes = package.metadata['notes'] if package.metadata['notes'] else "N/A"
        notes = notes[:30].replace("\n", " ").replace("\r", " ")
        license = package.metadata['license'] if package.metadata['license'] else "N/A"

        index = self.Index()

        self.m_wxlistctrl.InsertStringItem(index, name)
        self.m_wxlistctrl.SetStringItem(index, 1, notes)
        self.m_wxlistctrl.SetStringItem(index, 2, license)

        self.m_wxlistctrl.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        self.m_wxlistctrl.SetColumnWidth(1, wx.LIST_AUTOSIZE)
        self.m_wxlistctrl.SetColumnWidth(2, wx.LIST_AUTOSIZE)


class PackageUtil(object):
    """
    Utilities for handling packages. The GUI instantiate it and uses it.
    """
    def __init__(self, wxparent):
        self.m_wxparent = wxparent
        self.m_download = download.DownloadUtil(self.m_wxparent)

    def Open(self, path):
        try:
            package = dpm.lib.load(path)
            return package
        except IOError:
            return None

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

