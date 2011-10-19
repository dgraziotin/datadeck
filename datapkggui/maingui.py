__author__ = 'dgraziotin'
"""
Main GUI module
Coding standard: http://www.wxpython.org/codeguidelines.php
"""
import wx
import wx.xrc
import wx.lib.newevent
import lib
import datapkg
import package
import operations


WX_STDOUT, EVT_STDOUT= wx.lib.newevent.NewEvent()

class MainGUI(object):

    def __init__(self, xml):
        self.m_xml = xml
        self.m_frame_main = xml.LoadFrame(None, 'DatapkgFrame')
        self.m_panel_main = wx.xrc.XRCCTRL(self.m_frame_main, 'notebook')

        self.m_frame_main.SetSize(wx.Size(600, 625))
        # panel_log retrieving
        self.m_console_text = wx.xrc.XRCCTRL(self.m_panel_main, 'console_text')
        self.m_console_clear_button = wx.xrc.XRCCTRL(self.m_panel_main, 'console_clear_button')
        self.m_console_text_timer = wx.Timer(self.m_console_text, -1)

        self.m_console_text.Bind(EVT_STDOUT, self.OnUpdateOutputWindow)
        self.m_console_text.Bind(wx.EVT_TIMER, self.OnProcessPendingOutputWindowEvents)


        # panel_log bindings
        self.m_panel_main.Bind(wx.EVT_BUTTON, self.OnConsoleClearButtonClick, id=wx.xrc.XRCID('console_clear_button'))

        # panel_main retrieving
        self.m_search_text = wx.xrc.XRCCTRL(self.m_panel_main, 'search_text')
        self.m_download_button = wx.xrc.XRCCTRL(self.m_panel_main, 'download_button')
        self.m_info_button = wx.xrc.XRCCTRL(self.m_panel_main, 'info_button')
        self.m_search_results_list = wx.xrc.XRCCTRL(self.m_panel_main, 'search_results_list')
        self.m_search_results_list.InsertColumn(0, "Name")
        self.m_search_results_list.InsertColumn(1, "Short Description")
        self.m_search_results_list.InsertColumn(2, "License")
        self.m_search_results_list.InsertColumn(3, "Author")
        # panel_main bindings
        self.m_frame_main.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelectedSearchResultsList,
                             id=wx.xrc.XRCID('search_results_list'))
        self.m_frame_main.Bind(wx.EVT_BUTTON, self.OnButtonClickSearch, id=wx.xrc.XRCID('search_button'))
        self.m_frame_main.Bind(wx.EVT_BUTTON, self.OnButtonClickDownload, id=wx.xrc.XRCID('download_button'))
        self.m_frame_main.Bind(wx.EVT_BUTTON, self.OnButtonClickInfo, id=wx.xrc.XRCID('info_button'))

        self.m_search_text.Bind(wx.EVT_KEY_DOWN, self.OnKeyDownSearchText)

        self.m_frame_main.Show()

        self.DisableButtonInfoDownload()

        # status bar
        self.m_status_bar = self.m_frame_main.CreateStatusBar()

        # search results
        self.m_search_results = {}
        self.m_search_results_index = 0

        # Set up event handler for any worker thread results
        operations.OPERATION_MESSAGE(self.m_frame_main, self.OnOperationMessageReceived)

    def OnUpdateOutputWindow(self, event):
        value = event.text
        self.m_console_text.SetValue(value)

    def OnProcessPendingOutputWindowEvents(self, event):
         self.m_console_text.ProcessPendingEvents()


    def OnOperationMessageReceived(self, operation_message):
        #TODO needs refactoring
        #TODO handle buttons 
        if operation_message.type == operations.DownloadOperation:
            if operation_message.status == operations.OPERATION_STATUS_ID["started"]:
                self.SetStatusBarMessage("Download Started")
            elif operation_message.status == operations.OPERATION_STATUS_ID["finished"]:
                self.SetStatusBarMessage("Download Finished")
            elif operation_message.status == operations.OPERATION_STATUS_ID["error"]:
                self.SetStatusBarMessage("ERROR: " + operation_message.data)
            else:
                pass
        elif operation_message.type == operations.SearchOperation:
            if operation_message.status == operations.OPERATION_STATUS_ID["started"]:
                self.SetStatusBarMessage("Search Started")
            elif operation_message.status == operations.OPERATION_STATUS_ID["finished"]:
                self.SetStatusBarMessage("Search Finished")
            elif operation_message.status == operations.OPERATION_STATUS_ID["error"]:
                self.SetStatusBarMessage("ERROR: " + operation_message.data)
            else:
                pass
        else:
            pass

    def OnKeyDownSearchText(self, event):
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_RETURN:
            self.OnButtonClickSearch(event)
        event.Skip()

    def OnItemSelectedSearchResultsList( self, event ):
        selected_item = event.m_itemIndex
        package_selected = self.m_search_results[selected_item]
        if package_selected:
            self.EnableButtonInfoDownload()
        else:
            self.DisableButtonInfoDownload()

    def OnButtonClickSearch( self, event ):
        searched_value = self.m_search_text.GetValue()

        if not searched_value:
            return

        self.DisableButtonInfoDownload()
        self.SetStatusBarMessage("Searching for " + searched_value)

        self.m_search_results_list.DeleteAllItems()
        self.m_search_results_index = 0
        self.m_search_results = {}

        results = lib.search("ckan://", searched_value)
        if results:
            for package in results:
                self.InsertSearchResultsList(package)
                self.m_search_results_index += 1
            self.SetStatusBarMessage("")
        else:
            package = datapkg.package.Package()
            package.name = "Not Found"
            self.InsertSearchResultsList(package)
            self.SetStatusBarMessage("No results.")


    def OnButtonClickDownload(self, event):
        package_selected_index = self.m_search_results_list.GetNextSelected(-1)
        if package_selected_index == -1:
            return

        package_selected = self.m_search_results[package_selected_index]

        if package_selected:
            operations.DownloadOperation(self.m_frame_main, package_selected)


    def OnButtonClickInfo(self, event):
        package_selected_index = self.m_search_results_list.GetNextSelected(-1)
        if package_selected_index == -1:
            return

        package_selected = self.m_search_results[package_selected_index]

        if package_selected:
            package_info = package.PackageGUI(self.m_xml, package_selected)
            package_info.Show()
        return

    def OnConsoleClearButtonClick(self, event):
        self.m_console_text.Clear()

    def SetStatusBarMessage(self, message):
        self.m_status_bar.SetStatusText(message)

    def DisableButtonInfoDownload(self):
        self.m_info_button.Disable()
        self.m_download_button.Disable()

    def EnableButtonInfoDownload(self):
        self.m_info_button.Enable()
        self.m_download_button.Enable()

    def InsertSearchResultsList(self, package):
        self.m_search_results[self.m_search_results_index] = package

        name = package.metadata['name'] if package.metadata['name'] else "N/A"
        notes = package.metadata['notes'] if package.metadata['notes'] else "N/A"
        license = package.metadata['license'] if package.metadata['license'] else "N/A"
        author = package.metadata['author'] if package.metadata['author'] else "N/A"

        self.m_search_results_list.InsertStringItem(self.m_search_results_index, name)
        self.m_search_results_list.SetStringItem(self.m_search_results_index, 1, notes.strip()[:30])
        self.m_search_results_list.SetStringItem(self.m_search_results_index, 2, license)
        self.m_search_results_list.SetStringItem(self.m_search_results_index, 3, author)

        self.m_search_results_list.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        self.m_search_results_list.SetColumnWidth(1, wx.LIST_AUTOSIZE)
        self.m_search_results_list.SetColumnWidth(2, wx.LIST_AUTOSIZE)
        self.m_search_results_list.SetColumnWidth(3, wx.LIST_AUTOSIZE)