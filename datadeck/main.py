__author__ = 'dgraziotin'
"""
Main Application. Implements a custom stdout/stderr listener.
Class the Main GUI.
Coding standard: http://www.wxpython.org/codeguidelines.php
"""
import sys
import wx
import wx.xrc
import pkg_resources

import datadeck.gui
class DataDeck(wx.App):
    def __init__(self, redirect=True, filename=None):
        wx.App.__init__(self, redirect, filename)

    def OnInit(self, ):
        if self.IsDpmInstalled():
            import datadeck.gui.main
            self.MainGUI = datadeck.gui.main.MainGUI()
        else:
            import datadeck.gui.base
            frame = datadeck.gui.base.DepCheckFrame(None)
            dependencies_file = pkg_resources.resource_filename('datadeck.res', 'MISSING_DPM.txt')
            frame.m_dependencies_tc.AppendText(open(dependencies_file).read())
            frame.SetSize(wx.Size(600,400))
            frame.Show()
        return True
    
    def IsDpmInstalled(self):
        try:
            import dpm
            return True
        except ImportError:
            return False


class SysOutListener:
    
    def __init__(self, wx_widget):
        self.m_wxwidget = wx_widget
        
    def write(self, string):
        sys.__stdout__.write(string)
        evt = datadeck.gui.main.WX_STDOUT(text=string)
        wx.PostEvent(self.m_wxwidget, evt)

    def flush(self):
        sys.__stdout__.flush()

def run_as_plugin():
    MainGUI = datadeck.gui.main.MainGUI()
    sysout_listener = SysOutListener(MainGUI.m_console_tc)
    sys.stdout = sysout_listener
    
def run():
    app = DataDeck(0)
    app.SetAppName("DataDeck")
    if app.IsDpmInstalled():
        sysout_listener = SysOutListener(wx.GetApp().MainGUI.m_console_tc)
        sys.stdout = sysout_listener
    app.MainLoop()

if __name__ == '__main__':
    run()

