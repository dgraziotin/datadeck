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
import sys

class ConsoleGUI(object):
    def __init__(self, xml, show=False):
        self.xml = xml
        self.frame_log = xml.LoadFrame(None, 'LogFrame')
        self.panel_log = xrc.XRCCTRL(self.frame_log, 'panel')

        # panel_log retrieving
        self.console_text = xrc.XRCCTRL(self.panel_log, 'console_text')
        self.console_clear_button = xrc.XRCCTRL(self.panel_log, 'console_clear_button')
        # panel_log bindings
        self.frame_log.Bind(wx.EVT_BUTTON, self.OnConsoleClearButtonClick, id=xrc.XRCID('console_clear_button'))

        if show:
            self.frame_log.Show()

        # redirect text here
        self.redir = RedirectText(self.console_text)
        sys.stdout = self.redir
        sys.stderr = self.redir

    def Show(self):
        self.frame_log.Show()

    def OnConsoleClearButtonClick(self, event):
        self.console_text.Clear()


class RedirectText(object):
    """
    Helper object to redirect stdout and stderr to a wx.TextCtrl
    credits: http://www.blog.pythonlibrary.org/2009/01/01/wxpython-redirecting-stdout-stderr/
    """

    def __init__(self, aWxTextCtrl):
        self.out = aWxTextCtrl

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
