__author__ = 'dgraziotin'
"""
Main GUI module. Implements search and download of packages.
Calls packagegui.py for displaying information about a package.
Manages Operations (~threads, see operations.py) and their messages.
Coding standard: http://www.wxpython.org/codeguidelines.php
"""
import wx
import wx.xrc
import wx.lib.newevent
import datapkg
import packagegui
import operations
import os

# for handling stdout and stderr on a TextCtrl
WX_STDOUT, EVT_STDOUT = wx.lib.newevent.NewEvent()

class MainGUI(object):
    """
    The first GUI displayed when the program starts up.
    """

    def __init__(self, xml):
        """
        Loads resources from XRC file, prepares internal structures representing search results,
        binds events, prepares the Console for receiving stdout and stderr.
        """
        self.m_xml = xml
        self.m_frame_main = xml.LoadFrame(None, 'DatapkgFrame')
        self.m_panel_main = wx.xrc.XRCCTRL(self.m_frame_main, 'notebook')

        # search results
        self.m_search_results = {}
        self.m_search_results_index = 0

        # Main Panel retrieving and bindings
        self.m_search_text = wx.xrc.XRCCTRL(self.m_panel_main, 'search_text')
        self.m_download_button = wx.xrc.XRCCTRL(self.m_panel_main, 'download_button')
        self.m_info_button = wx.xrc.XRCCTRL(self.m_panel_main, 'info_button')
        self.m_search_results_list = wx.xrc.XRCCTRL(self.m_panel_main, 'search_results_list')
        self.m_search_results_list.InsertColumn(0, "Name")
        self.m_search_results_list.InsertColumn(1, "Short Description")
        self.m_search_results_list.InsertColumn(2, "License")
        self.m_search_results_list.InsertColumn(3, "Author")

        self.m_frame_main.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelectedSearchResultsList,
                               id=wx.xrc.XRCID('search_results_list'))
        self.m_frame_main.Bind(wx.EVT_BUTTON, self.OnButtonClickSearch, id=wx.xrc.XRCID('search_button'))
        self.m_frame_main.Bind(wx.EVT_BUTTON, self.OnButtonClickDownload, id=wx.xrc.XRCID('download_button'))
        self.m_frame_main.Bind(wx.EVT_BUTTON, self.OnButtonClickInfo, id=wx.xrc.XRCID('info_button'))
        self.m_search_text.Bind(wx.EVT_KEY_DOWN, self.OnKeyDownSearchText)

        # Console retrieving and bindings
        self.m_console_text = wx.xrc.XRCCTRL(self.m_panel_main, 'console_text')
        self.m_console_clear_button = wx.xrc.XRCCTRL(self.m_panel_main, 'console_clear_button')
        self.m_console_text_timer = wx.Timer(self.m_console_text, -1)

        self.m_console_text.Bind(EVT_STDOUT, self.OnUpdateConsole)
        self.m_console_text.Bind(wx.EVT_TIMER, self.OnProcessPendingEventsConsole)
        self.m_panel_main.Bind(wx.EVT_BUTTON, self.OnConsoleClearButtonClick, id=wx.xrc.XRCID('console_clear_button'))

        # status bar
        self.m_status_bar = self.m_frame_main.CreateStatusBar()

        # Set up event handler for any worker thread results
        operations.OPERATION_MESSAGE_HANDLER(self.m_frame_main, self.OnOperationMessageReceived)

        # disable Download and Info buttons
        self.EnableButtons(False)
        self.m_frame_main.SetSize(wx.Size(600, 625))
        self.m_frame_main.Show()

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
        #TODO needs refactoring
        #TODO block downloads if there is already one in downloading
        if operation_message.type == operations.DownloadOperation:
            if operation_message.status == operations.OPERATION_STATUS_ID["started"]:
                self.SetStatusBarMessage("Download Started")
            elif operation_message.status == operations.OPERATION_STATUS_ID["finished"]:
                self.SetStatusBarMessage("Download Finished")
            elif operation_message.status == operations.OPERATION_STATUS_ID["error"]:
                if operation_message.data:
                    self.SetStatusBarMessage("ERROR: " + operation_message.data)
            else:
                pass
        elif operation_message.type == operations.SearchOperation:
            if operation_message.status == operations.OPERATION_STATUS_ID["started"]:
                self.SetStatusBarMessage("Search Started")
            elif operation_message.status == operations.OPERATION_STATUS_ID["finished"]:
                self.SetStatusBarMessage("Search Finished")
                self.CleanSearchResults()
                results = operation_message.data
                if results:
                    for package in results:
                        self.InsertSearchResultsList(package)
                        self.m_search_results_index += 1
                else:
                    package = datapkg.package.Package()
                    package.name = "Not Found"
                    self.InsertSearchResultsList(package)
            elif operation_message.status == operations.OPERATION_STATUS_ID["error"]:
                self.SetStatusBarMessage("ERROR: " + operation_message.data)
            else:
                pass
        else:
            pass

    def OnKeyDownSearchText(self, event):
        """
        Simulate a click on Search button when Return is pressed
        """
        key_code = event.GetKeyCode()
        if key_code == wx.WXK_RETURN:
            self.OnButtonClickSearch(event)
        event.Skip()

    def OnItemSelectedSearchResultsList( self, event ):
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

    def OnButtonClickSearch( self, event ):
        """
        If there is text in the search text, launch a SearchOperation.
        """
        searched_value = self.m_search_text.GetValue()

        if not searched_value:
            return

        # clean eventual previous results
        self.EnableButtons(False)
        self.CleanSearchResults()

        operations.SearchOperation(self.m_frame_main, searched_value)


    def OnButtonClickDownload(self, event):
        """
        Retrieve the currently selected package in the results list and launch a DownloadOperation
        for downloading it.
        """
        package_selected_index = self.m_search_results_list.GetNextSelected(-1)
        if package_selected_index == -1:
            return

        package_selected = self.m_search_results[package_selected_index]
        download_dir = self.DownloadDirDialog()
        if package_selected and download_dir:
            operations.DownloadOperation(self.m_frame_main, package_selected, download_dir)

    def DownloadDirDialog(self):
        """
        Create a DirDialog for choosing the directory in which we save the Package
        """
        dialog = wx.DirDialog(self.m_frame_main, "Choose a Download Directory", os.getcwd())
        if dialog.ShowModal() == wx.ID_OK:
            download_dir = dialog.GetPath()
            return download_dir
        else:
            return None


    def OnButtonClickInfo(self, event):
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
            package_info.Show()
        return

    def OnConsoleClearButtonClick(self, event):
        self.m_console_text.Clear()

    def SetStatusBarMessage(self, message):
        self.m_status_bar.SetStatusText(message)

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
        author = package.metadata['author'] if package.metadata['author'] else "N/A"

        self.m_search_results_list.InsertStringItem(self.m_search_results_index, name)
        self.m_search_results_list.SetStringItem(self.m_search_results_index, 1, notes[:30].replace("\n","").replace("\r",""))
        self.m_search_results_list.SetStringItem(self.m_search_results_index, 2, license)
        self.m_search_results_list.SetStringItem(self.m_search_results_index, 3, author)

        self.m_search_results_list.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        self.m_search_results_list.SetColumnWidth(1, wx.LIST_AUTOSIZE)
        self.m_search_results_list.SetColumnWidth(2, wx.LIST_AUTOSIZE)
        self.m_search_results_list.SetColumnWidth(3, wx.LIST_AUTOSIZE)