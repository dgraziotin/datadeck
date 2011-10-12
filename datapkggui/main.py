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
import sys

class MainGUI(object):
    def __init__(self, xml):
        self.xml = xml
        self.Console = console.ConsoleGUI(xml)
        self.frame_main = xml.LoadFrame(None, 'DatapkgFrame')
        self.panel_main = xrc.XRCCTRL(self.frame_main, 'notebook')

        # panel_main retrieving
        self.search_label = xrc.XRCCTRL(self.panel_main, 'search_label')
        self.search_text = xrc.XRCCTRL(self.panel_main, 'search_text')
        self.download_button = xrc.XRCCTRL(self.panel_main, 'download_button')
        self.info_button = xrc.XRCCTRL(self.panel_main, 'info_button')
        self.search_results_list = xrc.XRCCTRL(self.panel_main, 'search_results_list')
        self.search_results_list.InsertColumn(0, "Name")
        self.search_results_list.InsertColumn(1, "Short Description")
        self.search_results_list.InsertColumn(2, "License")
        self.search_results_list.InsertColumn(3, "Author")
        # panel_main bindings
        self.frame_main.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnSearchResultsListItemSelected,
                             id=xrc.XRCID('search_results_list'))
        self.frame_main.Bind(wx.EVT_BUTTON, self.OnSearchButtonClick, id=xrc.XRCID('search_button'))
        self.frame_main.Bind(wx.EVT_BUTTON, self.OnDownloadButtonClick, id=xrc.XRCID('download_button'))
        self.frame_main.Bind(wx.EVT_BUTTON, self.OnInfoButtonClick, id=xrc.XRCID('info_button'))

        self.frame_main.Show()
        self.Console.Show()

        self.disable_buttons()

        # status bar
        self.status_bar = self.frame_main.CreateStatusBar()
        
        # search results
        self.search_results = {}
        self.search_results_index = 0

    def OnSearchResultsListItemSelected( self, event ):
        selected_item = event.m_itemIndex
        package_selected = self.search_results[selected_item]
        if package_selected:
            self.enable_buttons()
            self.search_label.SetValue(package_selected.pretty_print())
        else:
            self.disable_buttons()

    def OnSearchButtonClick( self, event ):
        searched_value = self.search_text.GetValue()

        if not searched_value:
            return

        self.disable_buttons()
        self.SetStatusBarMessage("Searching for " + searched_value)

        self.search_results_list.DeleteAllItems()
        self.search_results_index = 0
        self.search_results = {}

        results = lib.search("ckan://", searched_value)
        if results:
            for package in results:
                self.InsertSearchResultsList(package)
                self.search_results_index += 1
            self.SetStatusBarMessage("")
        else:
            package = datapkg.package.Package()
            package.name = "Not Found"
            self.InsertSearchResultsList(package)
            self.SetStatusBarMessage("No results.")
            pass

    def OnDownloadButtonClick(self, event):
        package_selected_index = self.search_results_list.GetNextSelected(-1)
        if package_selected_index == -1:
            return

        package_selected = self.search_results[package_selected_index]

        if package_selected:
            download_dir = self.DownloadDialog()
            if download_dir:
                lib.download("ckan://" + package_selected.name, download_dir)


    def DownloadDialog(self):
        dialog = wx.DirDialog(self.frame_main, "Choose a Download Directory", os.getcwd())
        if dialog.ShowModal() == wx.ID_OK:
            download_dir = dialog.GetPath()
            return download_dir
        dialog.Destroy()

    def OnInfoButtonClick(self, event):
        #TODO implement a nicer graphical way to analyze a package
        pass

    def SetStatusBarMessage(self, message):
        self.status_bar.SetStatusText(message)

    def disable_buttons(self):
        self.info_button.Disable()
        self.download_button.Disable()

    def enable_buttons(self):
        #self.info_button.Enable()
        self.download_button.Enable()

    def InsertSearchResultsList(self, package):
        self.search_results[self.search_results_index] = package

        name = package.metadata['name'] if package.metadata['name'] else "N/A"
        notes = package.metadata['notes'] if package.metadata['notes'] else "N/A"
        license = package.metadata['license'] if package.metadata['license'] else "N/A"
        author = package.metadata['author'] if package.metadata['author'] else "N/A"

        self.search_results_list.InsertStringItem(self.search_results_index, name)
        self.search_results_list.SetStringItem(self.search_results_index, 1, notes.strip()[:30])
        self.search_results_list.SetStringItem(self.search_results_index, 2, license)
        self.search_results_list.SetStringItem(self.search_results_index, 3, author)

        self.search_results_list.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        self.search_results_list.SetColumnWidth(1, wx.LIST_AUTOSIZE)
        self.search_results_list.SetColumnWidth(2, wx.LIST_AUTOSIZE)
        self.search_results_list.SetColumnWidth(3, wx.LIST_AUTOSIZE)


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

