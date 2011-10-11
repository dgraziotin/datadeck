__author__ = 'dgraziotin'
import wx
from wx import xrc
import lib
import datapkg
import os
import sys

class MainFrame(object):

    def __init__(self, xml):
        self.xml = xml
        self.frame = xml.LoadFrame(None,'DatapkgFrame')
        self.panel = xrc.XRCCTRL(self.frame, 'notebook')
        self.search_list = xrc.XRCCTRL(self.panel, 'search_list')
        self.search_label= xrc.XRCCTRL(self.panel, 'search_label')
        self.search_text = xrc.XRCCTRL(self.panel, 'search_text')
        self.console_text = xrc.XRCCTRL(self.panel, 'console_text')
        self.download_button = xrc.XRCCTRL(self.panel, 'download_button')
        self.info_button = xrc.XRCCTRL(self.panel, 'info_button')


        self.console_clear_button = xrc.XRCCTRL(self.panel, 'console_clear_button')
        self.frame.Bind(wx.EVT_LISTBOX, self.package_clicked, id=xrc.XRCID('search_list'))
        self.frame.Bind(wx.EVT_BUTTON, self.search, id=xrc.XRCID('search_button'))
        self.frame.Bind(wx.EVT_BUTTON, self.download, id=xrc.XRCID('download_button'))
        self.frame.Bind(wx.EVT_BUTTON, self.info, id=xrc.XRCID('info_button'))
        self.frame.Bind(wx.EVT_BUTTON, self.clear_console, id=xrc.XRCID('console_clear_button'))
        self.frame.Show()

        self.disable_buttons()

        # status bar
        self.status_bar = self.frame.CreateStatusBar()
        

        # redirect text here
        self.redir = RedirectText(self.console_text)
        sys.stdout = self.redir
        sys.stderr = self.redir

    def package_clicked( self, event ):
        package_selected = self.search_list.GetClientData(self.search_list.GetSelection())
        if package_selected:
            self.enable_buttons()
            self.search_label.SetValue(package_selected.pretty_print())
        else:
            self.disable_buttons()

    def search( self, event ):
        searched_value = self.search_text.GetValue()
        if not searched_value:
            return
        self.disable_buttons()
        self.status_bar_message("Searching for "+searched_value)
        self.search_list.Clear()
        self.search_label.SetValue("Info:")
        results = lib.search("ckan://", searched_value)
        if results:
            for package in results:
                self.search_list.Append(package.name, package)
            self.status_bar_message("")
        else:
            package = datapkg.package.Package()
            package.name = "Not Found"
            self.search_list.Append(package.name, package)
            self.status_bar_message("No results.")
            pass

    def download(self, event):
        package_selected = self.search_list.GetClientData(self.search_list.GetSelection())
        if package_selected:
            download_dir = self.download_dialog()
            if download_dir:
                lib.download("ckan://"+package_selected.name, download_dir)
                

    def download_dialog(self):
        dialog = wx.DirDialog(self.frame, "Choose a Download Directory",os.getcwd())
        if dialog.ShowModal() == wx.ID_OK:
            download_dir = dialog.GetPath()
            return download_dir
        dialog.Destroy()

    def info(self, event):
        #TODO implement a nicer graphical way to analyze a package
        pass

    def clear_console(self, event):
        self.console_text.Clear()

    def status_bar_message(self, message):
        self.status_bar.SetStatusText(message)

    def disable_buttons(self):
        self.info_button.Disable()
        self.download_button.Disable()

    def enable_buttons(self):
        #self.info_button.Enable()
        self.download_button.Enable()

class RedirectText(object):
    # credits: http://www.blog.pythonlibrary.org/2009/01/01/wxpython-redirecting-stdout-stderr/
    def __init__(self,aWxTextCtrl):
        self.out=aWxTextCtrl

    def write(self, string):
        self.out.WriteText(string)

    def flush(self):
        pass



class DatapkgGUI(wx.App):

    def __init__(self, redirect=True, filename=None):
        wx.App.__init__(self, redirect, filename)

    def OnInit(self, ):
        xml = xrc.XmlResource('datapkggui.xrc')
        self.MainFrame = MainFrame(xml)
        return True


if __name__ == '__main__':
    app = DatapkgGUI(0)
    app.SetAppName("Datapkg")
    app.MainLoop()

