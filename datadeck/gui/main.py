__author__ = 'dgraziotin'
"""
Main GUI module. Implements search and download of packages.
Calls packagegui.py for displaying information about a package.
Manages Operations (~threads, see operations.py) and their messages.
Coding standard: http://www.wxpython.org/codeguidelines.php
"""
import os
import wx
import wx.xrc
import wx.lib.newevent
import dpm.package
import datadeck
import datadeck.settings
import datadeck.operations

import util.console
import util.operations
import util.download
import util.package
import util.validator

import base
import settings


# for handling stdout and stderr on a TextCtrl
WX_STDOUT, EVT_STDOUT = wx.lib.newevent.NewEvent()

class MainGUI(base.DataDeckFrame):
    """
    The first GUI displayed when the program starts up.
    """

    def __init__(self):
        """
        Loads resources from XRC file, prepares internal structures representing search results,2
        """
        base.DataDeckFrame.__init__(self, None)

        self.CheckConfig()

        self.m_notebook_n_tabs = {
            "library" : 0,
            "search" : 1,
            "create" : 2,
        }

        #not handled well in autogenerated code, so they will be set here.

        self.m_search_lc.InsertColumn(0, "Name")
        self.m_search_lc.InsertColumn(1, "Short Description")
        self.m_search_lc.InsertColumn(2, "License")

        self.m_library_lc.InsertColumn(0, "Name")
        self.m_library_lc.InsertColumn(1, "Short Description")
        self.m_library_lc.InsertColumn(2, "License")

        self.m_uconsole = util.console.ConsoleUtil(self)
        self.m_uoperations = util.operations.OperationsUtil(self)
        self.m_udownload = util.download.DownloadUtil(self)
        self.m_upackage = util.package.PackageUtil(self)
        self.m_usearch_results = util.package.SearchResults(self.m_search_lc)
        self.m_ulibrary = util.package.Library(self.m_library_lc)

        self.m_console_tc_timer = wx.Timer(self.m_console_tc, -1)
        self.m_console_tc.Bind(EVT_STDOUT, self.OnUpdateConsole)
        self.m_console_tc.Bind(wx.EVT_TIMER, self.OnProcessPendingEventsConsole)

        self.m_create_license_c.AppendItems(self.m_upackage.Licenses())

        # Set up event handler for any worker thread results
        datadeck.operations.OPERATION_MESSAGE_HANDLER(self, self.OnOperationMessageReceived)

        # disable Download and Info buttons
        self.EnableSearchResultsButtons(False)
        self.SetSize(wx.Size(600, 650))
        self.Show(True)

    # <menu>
    def OnMenuNewClick( self, event ):
        self.m_create_name_tc.Clear()
        self.m_create_url_tc.Clear()
        self.m_create_license_c.Clear()
        self.m_create_author_tc.Clear()
        self.m_create_author_email_tc.Clear()
        self.m_create_notes_tc.Clear()
        self.m_create_tags_tc.Clear()
        self.m_notebook_n.ChangeSelection(self.m_notebook_n_tabs["create"])

    def OnMenuOpenClick( self, event ):
        open_path = self.m_udownload.DownloadDirDialog(message="Select a Package folder")
        if not open_path:
            return
        package = self.m_upackage.Open(open_path)
        if not package:
            return
        self.PopulatePackageCreation(package)
        self.m_notebook_n.ChangeSelection(self.m_notebook_n_tabs["create"])

    def OnMenuSettingsClick(self, event):
        settings.SettingsGUI(self).Show()

    def OnMenuExitClick(self, event):
        self.m_uoperations.KillOperations()
        self.Close()


    def OnMenuAboutClick(self, event):
        """
        Creates the About window.
        """
        about_frame = base.AboutFrame(self)
        label = "DataDeck v%s" % datadeck.__version__

        about_frame.m_datadeck_st.SetLabel(label)

        license = datadeck.__license_full__
        about_frame.m_license_tc.AppendText(license)

        about_frame.SetSize(wx.Size(500, 400))
        about_frame.Centre()
        about_frame.Show()
    # </menu>

    # <library>
    def OnLibraryListItemSelected( self, event ):
        self.EnableLibraryButtons(True)

    def OnLibraryListItemDeselected( self, event ):
        self.EnableLibraryButtons(False)

    def EnableLibraryButtons(self, enable):
        self.m_library_info_b.Enable(enable)
        self.m_library_edit_b.Enable(enable)
        self.m_library_delete_b.Enable(enable)

    def OnButtonLibraryInfoClick( self, event ):
        selected_package = self.m_ulibrary.GetSelected()
        if selected_package:
            self.m_upackage.Info(selected_package)

    def OnButtonLibraryEditClick( self, event ):
        selected_package = self.m_ulibrary.GetSelected()
        if not selected_package:
            return
        self.PopulatePackageCreation(selected_package)
        self.m_notebook_n.ChangeSelection(self.m_notebook_n_tabs["create"])

    def OnButtonLibraryDeleteClick( self, event ):
        package = self.m_ulibrary.GetSelected()
        message = "Are you sure you want to delete\nPackage " + package.name + "\ninstalled at " + package.installed_path + "?"
        box = wx.MessageDialog(self, message, "Delete?", wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        overwrite = box.ShowModal()
        if overwrite == wx.ID_YES:
            self.m_ulibrary.Remove(package)
            self.m_ulibrary.Refresh()

    def OnButtonRefreshClick( self, event ):
        self.RefreshLibrary()

    def RefreshLibrary(self):
        self.m_ulibrary.Refresh()
    # </library>

    # <search>
    def OnSearchResultsListItemSelected( self, event ):
        self.EnableSearchResultsButtons(True)

    def OnSearchResultsListItemDeselected( self, event ):
        self.EnableSearchResultsButtons(False)

    def EnableSearchResultsButtons(self, enable):
        """
        Could not find a better name. Take care of two buttons that user sometimes do not need to click.
        Info and Download button can not be clicked if there are no packages selected. Their respective Click events
        take care whether there is a package selected or not, but in this way we drive the user experience, letting
        him/her know what to do after a package is searched.
        """
        self.m_search_info_b.Enable(enable)
        self.m_search_download_b.Enable(enable)


    def OnSearchTextKeyDown(self, event):
        """
        Simulate a click on Search button when Return is pressed
        """
        key_code = event.GetKeyCode()
        if key_code == wx.WXK_RETURN:
            self.OnButtonSearchClick(event)
        event.Skip()

    def OnButtonSearchClick( self, event ):
        """
        If there is text in the search text, launch a SearchOperation.
        """
        searched_value = self.m_search_tc.GetValue()

        if not searched_value:
            return

        # clean eventual previous results
        self.EnableSearchResultsButtons(False)
        self.CleanSearchResults()

        datadeck.operations.SearchOperation(self, searched_value)
        print "Please wait..."

    def OnButtonDownloadClick(self, event):
        """
        Retrieve the currently selected package in the results list and launch a DownloadOperation
        for downloading it.
        """
        selected_package = self.m_usearch_results.GetSelected()
        if not selected_package:
            return
        self.m_upackage.Download(selected_package)


    def OnButtonInfoClick(self, event):
        """
        Retrieve the currently selected package in the results list and invoke the Package GUI
        for displaying information about it.
        """
        selected_package = self.m_usearch_results.GetSelected()
        if selected_package:
            self.m_upackage.Info(selected_package)

    def CleanSearchResults(self):
        self.m_usearch_results.Clear()


    def InsertSearchResultsList(self, package):
        """
        Insert a package in both the internal list and the GUI list. self.m_search_results_index ensures us that
        the two lists will be consistent.
        """
        self.m_usearch_results.Add(package)
    # </search>

    # <create>
    def PopulatePackageCreation(self, package):
        self.m_create_name_tc.SetValue(package.name)
        self.m_create_url_tc.SetValue(package.url)
        self.m_create_license_c.SetSelection(datadeck.settings.Settings.licenses(package.license))
        self.m_create_author_tc.SetValue(package.author)
        self.m_create_author_email_tc.SetValue(package.author_email)
        self.m_create_notes_tc.SetValue(package.notes)
        tags = ""
        for tag in package.tags:
            tags += tag + " "
        tags = tags.rstrip()
        self.m_create_tags_tc.SetValue(tags)


    # Save or Create a Package
    def OnButtonCreateClick( self, event ):
        package = dpm.package.Package()
        package.name = self.m_create_name_tc.GetValue()
        package.title = package.name
        package.url = self.m_create_url_tc.GetValue()
        package.license = self.m_upackage.Licenses(self.m_create_license_c.GetSelection())
        package.author = self.m_create_author_tc.GetValue()
        package.author_email = self.m_create_author_email_tc.GetValue()
        package.notes = self.m_create_notes_tc.GetValue()
        tags = self.m_create_tags_tc.GetValue()
        tags = tags.rstrip()
        package.tags = tags.split(" ")
        path = datadeck.settings.Settings.datadeck_default_path()

        if not self.m_upackage.Validate(package):
            print "no valid"
            return

        overwrite_check = self.m_udownload.CheckPackageOverwrite(path, package)

        if overwrite_check:
            self.m_upackage.Create(package, path)
    # </create>

        # <console>
    def OnUpdateConsole(self, event):
        """
        Update the Console text
        """
        self.m_uconsole.OnUpdateConsole(event)

    def OnProcessPendingEventsConsole(self, event):
        """
        Handle pending events
        """
        self.m_uconsole.OnProcessPendingEventsConsole(event)

    def OnConsoleClearButtonClick(self, event):
        self.m_uconsole.OnConsoleClearButtonClick(event)
        # </console>


    # <operations>
    def OnOperationMessageReceived(self, operation_message):
        """
        Handler for Operation Messages. Detect the type of the Message received and take care of it.
        According to the status of the Message, inform the user and update the GUI.
        See operations.py
        """
        self.m_uoperations.OnOperationMessageReceived(operation_message)

    def OnOperationsKillButtonClick( self, event ):
        """
        Kill all the currently running Operations
        """
        self.m_uoperations.KillOperations()
        # </operations>



    # <misc>
    def CheckConfig(self):
        #TODO: remove it when dpm 0.10 is officially released
        configuration = dpm.CONFIG
        if configuration.get("index:ckan", "ckan.url").find('ckan.net') > -1:
            configuration.set("index:ckan", "ckan.url", "http://thedatahub.org/api/")
            configuration.write(open(dpm.config.default_config_path, 'w'))

            configuration_path = dpm.config.default_config_path
            message = ("A dpm configuration file has been created on %s\n" +
                       "Please restart the program.") % configuration_path
            box = wx.MessageDialog(self, message, "dpm Configuration", wx.OK)
            box.ShowModal()
            box.Destroy()
            self.Close()
        import ConfigParser

        default_path = ""
        try:
            default_path = datadeck.settings.Settings.datadeck_default_path()
        except (ConfigParser.NoSectionError, ConfigParser.NoOptionError):
            datadeck.settings.Settings.datadeck_default_path(os.path.expanduser('~'))
        if not default_path:
            datadeck.settings.Settings.datadeck_default_path(os.path.expanduser('~'))
    # </misc>
