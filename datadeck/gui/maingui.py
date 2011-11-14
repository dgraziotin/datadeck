__author__ = 'dgraziotin'
"""
Main GUI module. Implements search and download of packages.
Calls packagegui.py for displaying information about a package.
Manages Operations (~threads, see operations.py) and their messages.
Coding standard: http://www.wxpython.org/codeguidelines.php
"""
import threading
import wx
import wx.xrc
import wx.lib.newevent
import datadeck.operations as operations
import packagegui
import shutil
import os

import base
# for handling stdout and stderr on a TextCtrl
WX_STDOUT, EVT_STDOUT = wx.lib.newevent.NewEvent()

class MainGUI(base.GUI):
    """
    The first GUI displayed when the program starts up.
    """
    def __init__(self, xml):
        """
        Loads resources from XRC file, prepares internal structures representing search results,
        binds events, prepares the Console for receiving stdout and stderr.
        """
        base.GUI.__init__(self, xml, frame_name="DataDeckFrame", panel_name="notebook")

        # search results
        self.m_search_results = {}
        self.m_search_results_index = 0
        self.m_killing_operations = False

        # Main Panel retrieving and bindings
        self.m_search_text = self.GetWidget('search_text')
        self.m_download_button = self.GetWidget('download_button')
        self.m_info_button = self.GetWidget('info_button')
        self.m_search_results_list = self.GetWidget('search_results_list')
        self.m_search_results_list.InsertColumn(0, "Name")
        self.m_search_results_list.InsertColumn(1, "Short Description")
        self.m_search_results_list.InsertColumn(2, "License")

        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnSearchResultsListItemSelected, 'search_results_list')
        self.Bind(wx.EVT_BUTTON, self.OnButtonSearchClick, 'search_button')
        self.Bind(wx.EVT_BUTTON, self.OnButtonDownloadClick, 'download_button')
        self.Bind(wx.EVT_BUTTON, self.OnButtonInfoClick, 'info_button')
        self.m_search_text.Bind(wx.EVT_KEY_DOWN, self.OnSearchTextKeyDown)

        # Console retrieving and bindings
        self.m_console_text = self.GetWidget('console_text')
        self.m_console_clear_button = self.GetWidget('console_clear_button')
        self.m_console_kill_button = self.GetWidget('console_kill_button')
        self.m_console_text_timer = wx.Timer(self.m_console_text, -1)
        self.m_console_text.Bind(EVT_STDOUT, self.OnUpdateConsole)
        self.m_console_text.Bind(wx.EVT_TIMER, self.OnProcessPendingEventsConsole)
        self.Bind(wx.EVT_BUTTON, self.OnConsoleClearButtonClick, 'console_clear_button')
        self.Bind(wx.EVT_BUTTON, self.OnConsoleKillButtonClick, 'console_kill_button')

        # Set up event handler for any worker thread results
        operations.OPERATION_MESSAGE_HANDLER(self.m_frame, self.OnOperationMessageReceived)

        # disable Download and Info buttons
        self.EnableButtons(False)

    def OnConsoleKillButtonClick(self, event):
        """
        Kill all the currently running Operations
        """
        for thread in  threading.enumerate():
            # check if the first super class is an Operation
            if thread.__class__.mro()[1] == operations.Operation:
                self.m_killing_operations = True
                while thread.isAlive():
                    thread.RaiseException(operations.KillOperationException)

    def OnUpdateConsole(self, event):
        """
        Update the Console text
        """
        value = event.text
        self.m_console_text.AppendText(value)

    def OnProcessPendingEventsConsole(self, event):
        """
        Handle pending events
        """
        self.m_console_text.ProcessPendingEvents()


    def OnOperationMessageReceived(self, operation_message):
        """
        Handler for Operation Messages. Detect the type of the Message received and take care of it.
        According to the status of the Message, inform the user and update the GUI.
        See operations.py
        """
        operation_type_str = operation_message.type.__name__

        if operation_message.status == operations.OPERATION_STATUS_ID["error"] and self.m_killing_operations:
            self.m_killing_operations = False
            self.SetStatusBarMessage(operation_type_str + " Killed")
            return
        elif operation_message.status == (operations.OPERATION_STATUS_ID["error"]
                                          and not self.m_killing_operations and operation_message.data):
            self.SetStatusBarMessage(operation_type_str + " ERROR: " + operation_message.data)
        elif operation_message.status == operations.OPERATION_STATUS_ID["started"]:
            self.SetStatusBarMessage(operation_type_str + " Started")
        elif operation_message.status == operations.OPERATION_STATUS_ID["finished"]:
            self.SetStatusBarMessage(operation_type_str + " Finished")
            if operation_message.type == operations.SearchOperation:
                self.CleanSearchResults()
                results = operation_message.data
                if results:
                    print "Results found."
                    for package in results:
                        self.InsertSearchResultsList(package)
                        self.m_search_results_index += 1
                else:
                    print "No Results."
        else:
            pass

    def OnSearchTextKeyDown(self, event):
        """
        Simulate a click on Search button when Return is pressed
        """
        key_code = event.GetKeyCode()
        if key_code == wx.WXK_RETURN:
            self.OnButtonSearchClick(event)
        event.Skip()

    def OnSearchResultsListItemSelected( self, event ):
        """
        If the user selects a package in the search result list,
        enable the Info and Download buttons, for processing it.
        """
        selected_item = event.m_itemIndex
        package_selected = self.m_search_results[selected_item]
        if package_selected:
            self.EnableButtons(True)

    def CleanSearchResults(self):
        """
        Clear both the GUI and the internal lists of packages found. Ready for a new search.
        """
        self.m_search_results_list.DeleteAllItems()
        self.m_search_results_index = 0
        self.m_search_results = {}

    def OnButtonSearchClick( self, event ):
        """
        If there is text in the search text, launch a SearchOperation.
        """
        searched_value = self.m_search_text.GetValue()

        if not searched_value:
            return

        # clean eventual previous results
        self.EnableButtons(False)
        self.CleanSearchResults()

        print "Please wait..."
        
        operations.SearchOperation(self.m_frame, searched_value)


    def OnButtonDownloadClick(self, event):
        """
        Retrieve the currently selected package in the results list and launch a DownloadOperation
        for downloading it.
        """
        #TODO block downloads if there is already one in downloading
        package_selected_index = self.m_search_results_list.GetNextSelected(-1)
        if package_selected_index == -1:
            return

        package_selected = self.m_search_results[package_selected_index]
        download_dir = self.DownloadDirDialog()
        package_path = download_dir + os.sep + package_selected.name

        overwrite_check = self.CheckPackageOverwrite(download_dir, package_selected)

        if overwrite_check:
            operations.DownloadOperation(self.m_frame, package_selected, download_dir)


    def OnButtonInfoClick(self, event):
        """
        Retrieve the currently selected package in the results list and invoke the Package GUI
        for displaying information about it.
        """
        package_selected_index = self.m_search_results_list.GetNextSelected(-1)
        if package_selected_index == -1:
            return

        package_selected = self.m_search_results[package_selected_index]

        if package_selected:
            package_info = packagegui.PackageGUI(self.m_xml, package_selected)
            package_info.Show(True)
        return

    def OnConsoleClearButtonClick(self, event):
        self.m_console_text.Clear()

    def EnableButtons(self, enable):
        """
        Could not find a better name. Take care of two buttons that user sometimes do not need to click.
        Info and Download button can not be clicked if there are no packages selected. Their respective Click events
        take care whether there is a package selected or not, but in this way we drive the user experience, letting
        him/her know what to do after a package is searched.
        """
        self.m_info_button.Enable(enable)
        self.m_download_button.Enable(enable)


    def InsertSearchResultsList(self, package):
        """
        Insert a package in both the internal list and the GUI list. self.m_search_results_index ensures us that
        the two lists will be consistent.
        """
        self.m_search_results[self.m_search_results_index] = package

        name = package.metadata['name'] if package.metadata['name'] else "N/A"
        notes = package.metadata['notes'] if package.metadata['notes'] else "N/A"
        license = package.metadata['license'] if package.metadata['license'] else "N/A"

        self.m_search_results_list.InsertStringItem(self.m_search_results_index, name)
        self.m_search_results_list.SetStringItem(self.m_search_results_index, 1,
                                                 notes[:30].replace("\n", " ").replace("\r", " "))
        self.m_search_results_list.SetStringItem(self.m_search_results_index, 2, license)

        self.m_search_results_list.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        self.m_search_results_list.SetColumnWidth(1, wx.LIST_AUTOSIZE)
        self.m_search_results_list.SetColumnWidth(2, wx.LIST_AUTOSIZE)
