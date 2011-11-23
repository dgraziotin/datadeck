"""
This module holds GUI utilities for handling/representing Packages
"""
import wx
import os
import os.path
import shutil
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

    def GetSelected(self, index=-1):
        package_index = self.m_wxlistctrl.GetNextSelected(index)

        if package_index == -1:
            return None

        package_selected = self.Get(package_index)

        return package_selected

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
        self.m_wxlistctrl.SetColumnWidth(0, wx.LIST_AUTOSIZE_USEHEADER)
        self.m_wxlistctrl.SetColumnWidth(1, wx.LIST_AUTOSIZE_USEHEADER)
        self.m_wxlistctrl.SetColumnWidth(2, wx.LIST_AUTOSIZE_USEHEADER)

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

class Library(PackageList):
    """
    A PackageList for local installed packages
    """
    def __init__(self, wxlistctrl):
        PackageList.__init__(self, wxlistctrl)
        self.Refresh()

    def PackagesDirs(self):
        library_path = datadeck.settings.Settings.library_path()
        packages_dirs = [file for file in os.listdir(library_path) if os.path.isdir(os.path.join(library_path,file))]
        return packages_dirs

    def PackagesInLibrary(self, packages_dirs):
        library_path = datadeck.settings.Settings.library_path()
        packages_in_library = []
        for package_dir in packages_dirs:
            try:
                packages_in_library.append(dpm.lib.load(os.path.join(library_path,package_dir)))
            except IOError:
                pass    #just ignore dirs that do not contain packages
        return packages_in_library

    def Refresh(self):
        self.Clear()
        packages_dirs = self.PackagesDirs()
        packages_in_library = self.PackagesInLibrary(packages_dirs)

        for package in packages_in_library:
            self.m_packages.append(package)
            self._AddWxListrCtrl(package)

        self.AutoSize()

    def Remove(self, package):
        shutil.rmtree(package.installed_path, ignore_errors=True)
        self.AutoSize()


    def _AddWxListrCtrl(self, package):
        name = package.metadata['name'] if package.metadata['name'] else "N/A"
        notes = package.metadata['notes'] if package.metadata['notes'] else "N/A"
        notes = notes[:30].replace("\n", " ").replace("\r", " ")
        license = package.metadata['license'] if package.metadata['license'] else "N/A"

        index = self.Index()

        self.m_wxlistctrl.InsertStringItem(index, name)
        self.m_wxlistctrl.SetStringItem(index, 1, notes)
        self.m_wxlistctrl.SetStringItem(index, 2, license)


    def AutoSize(self):
        if not self.m_packages:
            self.m_wxlistctrl.SetColumnWidth(0, wx.LIST_AUTOSIZE_USEHEADER)
            self.m_wxlistctrl.SetColumnWidth(1, wx.LIST_AUTOSIZE_USEHEADER)
            self.m_wxlistctrl.SetColumnWidth(2, wx.LIST_AUTOSIZE_USEHEADER)
        else:
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

    def Validate(self, package):
        try:
            return validator.PackageValidator.validate(package)
        except validator.PackageNonValid, e:
            wx.MessageBox(str(e), caption="Validation Error", style=wx.OK)
            return False

    def Create(self, package, path):
        if self.Validate(package):
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

