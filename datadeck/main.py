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

class DataDeck(wx.App):
    def __init__(self, redirect=True, filename=None):
        wx.App.__init__(self, redirect, filename)

    def OnInit(self, ):
        xml = wx.xrc.XmlResource(pkg_resources.resource_filename('datadeck.res', 'datadeck.xrc'))
        if self.IsDpmInstalled():
            import gui.maingui
            self.MainGUI = gui.maingui.MainGUI(xml)
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
            print "dpm installed"
            return True
        except ImportError:
            print "dpm not installed"
            return False


class SysOutListener:
    def write(self, string):
        sys.__stdout__.write(string)
        evt = gui.maingui.WX_STDOUT(text=string)
        wx.PostEvent(wx.GetApp().MainGUI.m_console_text, evt)

    def flush(self):
        sys.__stdout__.flush()
        #evt = WX_STDOUT(text="clean")
        #wx.PostEvent(wx.GetApp().MainGUI.m_console_text, evt)


def run():
    sysout_listener = SysOutListener()
    app = DataDeck(0)
    app.SetAppName("DataDeck")
    sys.stdout = sysout_listener
    #sys.stderr = sysout_listener
    app.MainLoop()

if __name__ == '__main__':
    run()

