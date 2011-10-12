__author__ = 'dgraziotin'
"""
Main module holding the GUI
Coding standard: http://www.wxpython.org/codeguidelines.php
"""
import wx
from wx import xrc
import lib
import datapkg
import os
import console
import package
class MainGUI(object):
    def __init__(self, xml):
        self.m_xml = xml
        self.m_console = console.ConsoleGUI(xml)
        self.m_frame_main = xml.LoadFrame(None, 'DatapkgFrame')
        self.m_panel_main = xrc.XRCCTRL(self.m_frame_main, 'notebook')

       
        # panel_main retrieving
        self.m_search_label = xrc.XRCCTRL(self.m_panel_main, 'search_label')
        self.m_search_text = xrc.XRCCTRL(self.m_panel_main, 'search_text')
        self.m_download_button = xrc.XRCCTRL(self.m_panel_main, 'download_button')
        self.m_info_button = xrc.XRCCTRL(self.m_panel_main, 'info_button')
        self.m_search_results_list = xrc.XRCCTRL(self.m_panel_main, 'search_results_list')
        self.m_search_results_list.InsertColumn(0, "Name")
        self.m_search_results_list.InsertColumn(1, "Short Description")
        self.m_search_results_list.InsertColumn(2, "License")
        self.m_search_results_list.InsertColumn(3, "Author")
        # panel_main bindings
        self.m_frame_main.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelectedSearchResultsList,
                             id=xrc.XRCID('search_results_list'))
        self.m_frame_main.Bind(wx.EVT_BUTTON, self.OnButtonClickSearch, id=xrc.XRCID('search_button'))
        self.m_frame_main.Bind(wx.EVT_BUTTON, self.OnButtonClickDownload, id=xrc.XRCID('download_button'))
        self.m_frame_main.Bind(wx.EVT_BUTTON, self.OnButtonClickInfo, id=xrc.XRCID('info_button'))

        self.m_search_text.Bind(wx.EVT_KEY_DOWN, self.OnKeyDownSearchText)

        self.m_frame_main.Show()
        self.m_console.Show()

        self.DisableButtonInfoDownload()

        # status bar
        self.m_status_bar = self.m_frame_main.CreateStatusBar()
        
        # search results
        self.m_search_results = {}
        self.m_search_results_index = 0

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
            self.m_search_label.SetValue(package_selected.pretty_print())
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
            download_dir = self.DownloadDialog()
            if download_dir:
                lib.download("ckan://" + package_selected.name, download_dir)


    def DownloadDialog(self):
        dialog = wx.DirDialog(self.m_frame_main, "Choose a Download Directory", os.getcwd())
        if dialog.ShowModal() == wx.ID_OK:
            download_dir = dialog.GetPath()
            return download_dir
        dialog.Destroy()

    def OnButtonClickInfo(self, event):
        package_selected_index = self.m_search_results_list.GetNextSelected(-1)
        if package_selected_index == -1:
            return

        package_selected = self.m_search_results[package_selected_index]

        if package_selected:
            package_info = package.PackageGUI(self.m_xml, package_selected)
            package_info.Show()
        return

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


class Datapkg(wx.App):
    def __init__(self, redirect=True, filename=None):
        wx.App.__init__(self, redirect, filename)

    def OnInit(self, ):
        xml = xrc.XmlResource('datapkggui.xrc')
        self.MainGUI = MainGUI(xml)
        return True


if __name__ == '__main__':
    app = Datapkg(0)
    app.SetAppName("Datapkg")
    app.MainLoop()

