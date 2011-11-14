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
        xml = wx.xrc.XmlResource(pkg_resources.resource_filename('datadeck.res', 'datadeck.xrc'))
        if self.IsDpmInstalled():
            import datadeck.gui.maingui
            self.MainGUI = datadeck.gui.maingui.MainGUI(xml)
        else:
            frame = xml.LoadFrame(None, 'DepCheckFrame')
            dependencies_test = wx.xrc.XRCCTRL(frame, 'dependencies_text')
            dependencies_file = pkg_resources.resource_filename('datadeck.res', 'MISSING_DPM.txt')
            dependencies_test.AppendText(open(dependencies_file).read())
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
        evt = datadeck.gui.maingui.WX_STDOUT(text=string)
        wx.PostEvent(self.m_wxwidget, evt)

    def flush(self):
        sys.__stdout__.flush()
        #evt = WX_STDOUT(text="clean")
        #wx.PostEvent(wx.GetApp().MainGUI.m_console_text, evt)

def run_as_plugin():
    xml = wx.xrc.XmlResource(pkg_resources.resource_filename('datadeck.res', 'datadeck.xrc'))
    MainGUI = datadeck.gui.maingui.MainGUI(xml)
    sysout_listener = SysOutListener(MainGUI.m_console_text)
    sys.stdout = sysout_listener
    
def run():
    app = DataDeck(0)
    app.SetAppName("DataDeck")
    sysout_listener = SysOutListener(wx.GetApp().MainGUI.m_console_text)
    sys.stdout = sysout_listener
    app.MainLoop()

if __name__ == '__main__':
    run()

