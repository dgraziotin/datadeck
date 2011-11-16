__author__ = 'dgraziotin'
"""
General GUI module. it contains the base class for DataDeck GUIs, that should not be instantiated.
"""
import wx
import wx.xrc
import shutil
import datadeck
import dpm.config
import os
import dpm.lib
import threading
import datadeck.operations
import datadeck.settings as settings

class GUI(object):
    """
    Generic GUI class, holds the common shared properties and methods.
    Don't instantiate it, please.
    """

    def __init__(self, xml, frame_name, panel_name="panel"):
        """
        Constructor of our "abstract" class.
        DataDeck windows have one frame and one panel, so they must be passed as arguments.
        The xml XRC file must be passed, too.
        Shared objects such as the status bar and the menu bar are created here.
        """
        self.m_xml = xml

        self.m_frame = xml.LoadFrame(None, frame_name)

        self.m_panel = self.GetWidget(panel_name)
        self.m_menubar = self.m_frame.GetMenuBar()

        self.Bind(wx.EVT_MENU, self.OnMenuClickExit, 'menu_exit')
        self.Bind(wx.EVT_MENU, self.OnMenuAboutClick, 'menu_about')
        self.Bind(wx.EVT_MENU, self.OnMenuSettingsClick, 'menu_settings')

        self.m_frame.SetSize(wx.Size(600, 625))
        self.m_frame.Centre()
        self.m_frame.Show()

        self.CheckConfig()

    def OnMenuAboutClick(self, event):
        """
        Creates the About window.
        """
        about_frame = self.m_xml.LoadFrame(None, "AboutFrame")
        datadeck_label = self.GetWidget('datadeck_label', about_frame)
        license_text = self.GetWidget('license_text', about_frame)

        label = "DataDeck v%s" % datadeck.__version__
        datadeck_label.SetLabel(label)

        license = datadeck.__license_full__
        license_text.AppendText(license)

        about_frame.SetSize(wx.Size(500, 400))
        about_frame.Centre()
        about_frame.Show()

    def Show(self, show):
        self.m_frame.Show(show)
        
    def OnMenuClickExit(self, event):
        self.KillOperations()
        self.m_frame.Close()

    def OnMenuSettingsClick(self, event):
        import settingsgui
        settingsgui.SettingsGUI(self.m_xml)
        


    def DownloadDirDialog(self, path=None):
        """
        Create a DirDialog for choosing the directory in which we save the Package
        """
        dialog = wx.DirDialog(self.m_frame, "Choose a Download Directory", settings.Settings.datadeck_default_path())
        if dialog.ShowModal() == wx.ID_OK:
            download_dir = dialog.GetPath()
            return download_dir
        else:
            return None

    def CheckPackageOverwrite(self, download_dir, package):
        package_path = download_dir + os.sep + package.name
        if os.path.exists(package_path):
            message = "Overwrite " + package.name + "?"
            box = wx.MessageDialog(self.m_frame, message, "Overwrite?",wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
            overwrite = box.ShowModal()
            if overwrite == wx.ID_YES:
                shutil.rmtree(package_path, ignore_errors=True)
                return True
            else:
                return False
        else:
            return True


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

    def KillOperations(self):
        for thread in  threading.enumerate():
            # check if the first super class is an Operation
            if thread.__class__.mro()[1] == datadeck.operations.Operation:
                while thread.isAlive():
                    thread.RaiseException(datadeck.operations.KillOperationException)

    def CheckConfig(self):
        #TODO: remove it when dpm 0.10 is officially released
        configuration = dpm.CONFIG
        if configuration.get("index:ckan","ckan.url").find('ckan.net') > -1:
            configuration.set("index:ckan","ckan.url","http://thedatahub.org/api/")
            configuration.write(open(dpm.config.default_config_path,'w'))

            configuration_path = dpm.config.default_config_path
            message = ("A dpm configuration file has been created on %s\n"+
                        "Please restart the program.") %(configuration_path)
            box = wx.MessageDialog(self.m_frame, message, "dpm Configuration",wx.OK)
            box.ShowModal()
            box.Destroy()
            self.m_frame.Close()
        import ConfigParser
        default_path = ""
        try:
            default_path = settings.Settings.datadeck_default_path()
        except (ConfigParser.NoSectionError, ConfigParser.NoOptionError):
            settings.Settings.datadeck_default_path(os.path.expanduser('~'))
        if not default_path:
            settings.Settings.datadeck_default_path(os.path.expanduser('~'))