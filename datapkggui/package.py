__author__ = 'dgraziotin'
import wx
from wx import xrc

class PackageGUI(object):
    def __init__(self, xml, package=None):
        self.xml = xml
        self.frame_info = xml.LoadFrame(None, 'InfoFrame')
        self.panel_frame = xrc.XRCCTRL(self.frame_info, 'panel')
        # frame_info retrieving
        self.title_text = xrc.XRCCTRL(self.panel_frame, 'title_text')
        self.homepage_text = xrc.XRCCTRL(self.panel_frame, 'homepage_text')
        self.license_text = xrc.XRCCTRL(self.panel_frame, 'license_text')
        self.tags_text = xrc.XRCCTRL(self.panel_frame, 'tags_text')

        if package:
            self.UpdateWidgets(package)
        #self.console_clear_button = xrc.XRCCTRL(self.panel_frame, 'console_clear_button')
        # frame_info bindings
        #self.frame_info.Bind(wx.EVT_BUTTON, self.OnConsoleClearButtonClick, id=xrc.XRCID('console_clear_button'))

    def UpdateWidgets(self, package):
        name = package.metadata['name'] if package.metadata['name'] else "N/A"
        homepage = package.metadata['url'] if package.metadata['url'] else "N/A"
        license = package.metadata['license'] if package.metadata['license'] else "N/A"
        tags = package.metadata['tags'] if package.metadata['tags'] else ["N/A"]
        author = package.metadata['author'] if package.metadata['author'] else "N/A"
        notes = package.metadata['notes'] if package.metadata['notes'] else "N/A"

        self.title_text.SetValue(name)
        self.homepage_text.SetValue(homepage)
        self.license_text.SetValue(license)
        for tag in tags:
            self.tags_text.AppendText(tag + " ")
        
    def Show(self):
        self.frame_info.Show()
