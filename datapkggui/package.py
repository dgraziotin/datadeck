__author__ = 'dgraziotin'
import wx
from wx import xrc
import datapkg
class PackageGUI(object):
    def __init__(self, xml, package=None):

        self.xml = xml
        self.frame_info = xml.LoadFrame(None, 'InfoFrame')
        self.panel_frame = xrc.XRCCTRL(self.frame_info, 'panel')

        # minimum size
        self.frame_info.SetSize(wx.Size(500, 500))

        if not package:
            # we instantiate an empty package for obtaining its metadata
            # attributes
            package = datapkg.package.Package()

        # frame_info retrieving
        # WARNING: this only works because we defined the Widget names with the same
        # names of those defined in datapkg.metadata.Metadata. It's a sort of Reflection.
        for key, value in package.metadata.iteritems():
            setattr(self, key+"_text", xrc.XRCCTRL(self.panel_frame, key+"_text") )

        self.UpdateWidgets(package)
        
    def UpdateWidgets(self, package):
        # sets TextCtrl values by iterating Package Metadata
        for key, value in package.metadata.iteritems():
            try:
                text_ctrl = getattr(self, key+"_text")
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
