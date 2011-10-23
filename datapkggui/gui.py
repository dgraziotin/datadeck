import wx
import wx.xrc
import datapkggui

class GUI(object):
    """
    Generic GUI class, holds the common shared properties and methods.
    Don't instantiate it, please.
    """

    def __init__(self, xml, frame_name, panel_name="panel"):
        self.m_xml = xml

        self.m_frame = xml.LoadFrame(None, frame_name)

        self.m_panel = self.GetWidget(panel_name)
        self.m_status_bar = self.m_frame.CreateStatusBar()

        self.m_menubar = self.m_frame.GetMenuBar()

        self.Bind(wx.EVT_MENU, self.OnMenuClickExit, 'menu_exit')
        self.Bind(wx.EVT_MENU, self.OnMenuClickAbout, 'menu_about')

        self.m_frame.SetSize(wx.Size(600, 625))
        self.m_frame.Centre()
        self.m_frame.Show()

    def SetStatusBarMessage(self, message):
        self.m_status_bar.SetStatusText(message)

    def OnMenuClickAbout(self, event):
        about_frame = self.m_xml.LoadFrame(None, "AboutFrame")
        about_label = self.GetWidget('about_label', about_frame)
        label = "datapkggui version %s.\n%s\nWebsite: %s\nLicense:\n%s" % (
            datapkggui.__version__, datapkggui.__description__, "http://task3.cc/projects/datapkggui",
            datapkggui.__license_full__)

        about_label.SetLabel(label)
        about_frame.SetSize(wx.Size(694, 447))
        about_frame.Centre()
        about_frame.Show()

    def OnMenuClickExit(self, event):
        self.m_frame.Close()

    def GetWidget(self, name, window=None):
        """
        Wrapper around wx.xrc.XRCCTRL with window = self.m_frame set as default
        """
        if not window:
            window = self.m_frame
        return wx.xrc.XRCCTRL(window, name)

    def Bind(self, event, method, name):
        """
        Wrapper around Bind
        """
        self.m_frame.Bind(event, method, id=wx.xrc.XRCID(name))