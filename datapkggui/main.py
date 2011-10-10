__author__ = 'dgraziotin'
import wx
from wx import xrc
import lib
import datapkg

class MainFrame(object):

    def __init__(self, xml):
        self.xml = xml
        self.frame = xml.LoadFrame(None,'DatapkgFrame')
        self.panel = xrc.XRCCTRL(self.frame, 'notebook')
        self.search_list = xrc.XRCCTRL(self.panel, 'search_list')
        self.search_label= xrc.XRCCTRL(self.panel, 'search_label')
        self.search_text = xrc.XRCCTRL(self.panel, 'search_text')
        self.frame.Bind(wx.EVT_LISTBOX, self.package_clicked, id=xrc.XRCID('search_list'))
        self.frame.Bind(wx.EVT_BUTTON, self.search, id=xrc.XRCID('search_button'))
        self.frame.Show()

    def package_clicked( self, event ):
        package_selected = self.search_list.GetClientData(self.search_list.GetSelection())
        self.search_label.SetValue(package_selected.pretty_print())

    def search( self, event ):
        searched_value = self.search_text.GetValue()
        if not searched_value:
            return
        self.search_list.Clear()
        self.search_label.SetValue("Info:")
        results = lib.search("ckan://", searched_value)
        if results:
            for package in results:
                self.search_list.Append(package.name, package)
        else:
            package = datapkg.package.Package()
            package.name = "Not Found"
            self.search_list.Append(package.name, package)
            pass




class DatapkgGUI(wx.App):

    def OnInit(self):
        xml = xrc.XmlResource('datapkggui.xrc')
        self.MainFrame = MainFrame(xml)
        return True


if __name__ == '__main__':
    app = DatapkgGUI(0)
    app.SetAppName("Datapkg")
    app.MainLoop()

