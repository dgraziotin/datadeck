__author__ = 'dgraziotin'
"""
This module holds the GUI for representing a Package. Currently it is used only for showing
relevant information about a Package. It will also be used for creating a Package.
"""
import wx
import wx.xrc
import datapkg
import lib

class PackageGUI(object):
    def __init__(self, xml, package=None):
        self.xml = xml
        self.frame_info = xml.LoadFrame(None, 'InfoFrame')
        self.panel_frame = wx.xrc.XRCCTRL(self.frame_info, 'panel')

        # minimum size
        self.frame_info.SetSize(wx.Size(500, 500))

        if not package:
            # we instantiate an empty package for obtaining its metadata
            # attributes
            package = datapkg.package.Package()

        # frame_info retrieving
        # WARNING: this only works because we defined the Widget names with the same
        # names of those defined in datapkg.metadata.Metadata. It's a sort of Reflection.
        for key, value in lib.info(package, request_for="metadata").iteritems():
            setattr(self, key + "_text", wx.xrc.XRCCTRL(self.panel_frame, key + "_text"))

        self.UpdateWidgets(package)

    def UpdateWidgets(self, package):
        # sets TextCtrl values by iterating Package Metadata
        #TODO use the lib!
        for key, value in lib.info(package, request_for="metadata").iteritems():
            try:
                text_ctrl = getattr(self, key + "_text")
                # special case for tags list
                if key == "tags":
                    tags = value
                    if tags:
                        for tag in tags:
                            self.tags_text.AppendText(tag + " ")
                # ordinary case
                else:
                    if value:
                        text_ctrl.SetValue(unicode(value))
                    else:
                        text_ctrl.SetValue(u"N/A")
            except AttributeError:
                continue


    def Show(self):
        self.frame_info.Show()
