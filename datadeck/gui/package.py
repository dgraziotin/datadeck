"""
This module holds the GUI for representing a Package. Currently it is used only for showing
relevant information about a Package. It will also be used for creating a Package.
"""
import dpm
import dpm.lib
import dpm.package
import base


class PackageGUI(base.InfoFrame):
    def __init__(self, parent, package=None):
        base.InfoFrame.__init__(self, parent)

        if not package:
            # we instantiate an empty package for obtaining its metadata
            # attributes
            package = dpm.package.Package()

        self.m_package = package
        self.UpdateWidgets(package)

    def UpdateWidgets(self, package):
        # sets TextCtrl values by iterating Package Metadata
        for key, value in dpm.lib.info(package)[1].iteritems():
            try:
                text_ctrl = getattr(self, "m_" + key + "_tc")
                # special case for tags list
                if key == "tags":
                    tags = value
                    if tags:
                        for tag in tags:
                            self.m_tags_tc.AppendText(tag + " ")
                # ordinary case
                else:
                    if value:
                        text_ctrl.SetValue(unicode(value))
                    else:
                        text_ctrl.SetValue(u"N/A")
            except AttributeError:
                continue

    def OnButtonCloseClick( self, event ):
        self.Destroy()