__author__ = 'dgraziotin'
"""
General GUI module. it contains the base class for datapkggui GUIs, that should not be instantiated.
"""
import wx
import wx.xrc
import datapkggui
import datapkg.config
import os
import datapkggui.lib
class GUI(object):
    """
    Generic GUI class, holds the common shared properties and methods.
    Don't instantiate it, please.
    """

    def __init__(self, xml, frame_name, panel_name="panel"):
        """
        Constructor of our "abstract" class.
        Datapkggui windows have one frame and one panel, so they must be passed as arguments.
        The xml XRC file must be passed, too.
        Shared objects such as the status bar and the menu bar are created here.
        """
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

        self.CheckConfig()

    def SetStatusBarMessage(self, message):
        self.m_status_bar.SetStatusText(message)

    def OnMenuClickAbout(self, event):
        """
        Creates the About window.
        """
        about_frame = self.m_xml.LoadFrame(None, "AboutFrame")
        about_text = self.GetWidget('about_text', about_frame)
        label = "datapkggui version %s.\n%s\nWebsite: %s\nLicense:\n%s" % (
            datapkggui.__version__, datapkggui.__description__, "http://task3.cc/projects/datapkggui",
            datapkggui.__license_full__)

        about_text.AppendText(label)
        about_frame.SetSize(wx.Size(694, 447))
        about_frame.Centre()
        about_frame.Show()

    def Show(self, show):
        self.m_frame.Show(show)

    def OnMenuClickExit(self, event):
        self.m_frame.Close()

    def DownloadDirDialog(self):
        """
        Create a DirDialog for choosing the directory in which we save the Package
        """
        dialog = wx.DirDialog(self.m_frame, "Choose a Download Directory", os.getcwd())
        if dialog.ShowModal() == wx.ID_OK:
            download_dir = dialog.GetPath()
            return download_dir
        else:
            return None

    def GetWidget(self, name, window=None):
        """
        Wrapper around wx.xrc.XRCCTRL with window = self.m_frame set as default.
        """
        if not window:
            window = self.m_frame
        return wx.xrc.XRCCTRL(window, name)

    def Bind(self, event, method, name):
        """
        Wrapper around Bind method.
        """
        self.m_frame.Bind(event, method, id=wx.xrc.XRCID(name))

    def CheckConfig(self):
        configuration = datapkg.CONFIG
        if configuration.get("index:ckan","ckan.url").find('ckan.net') > -1:
            configuration.set("index:ckan","ckan.url","http://thedatahub.org/api/")
            configuration.write(open(datapkg.config.default_config_path,'w'))

            configuration_path = datapkg.config.default_config_path
            message = ("A datapkg configuration file has been created on %s\n"+
                        "Please restart the program.") %(configuration_path)
            box = wx.MessageDialog(self.m_frame, message, "datapkg Configuration",wx.OK)
            box.ShowModal()
            box.Destroy()
            self.m_frame.Close()


        