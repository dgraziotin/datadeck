__author__ = 'dgraziotin'
"""
This module holds the GUI for representing a Package. Currently it is used only for showing
relevant information about a Package. It will also be used for creating a Package.
"""
import wx
import wx.xrc
import dpm

try:
    import dpm.lib as lib
except ImportError:
    import datadeck.lib as lib

import datadeck.operations as operations
import base


class PackageGUI(base.GUI):
    def __init__(self, xml, package=None):
        base.GUI.__init__(self, xml, frame_name="InfoFrame", panel_name="panel")

        # minimum size
        self.m_frame.SetSize(wx.Size(500, 500))

        self.m_download_button = self.GetWidget('download_button')
        self.Bind(wx.EVT_BUTTON, self.OnButtonDownloadClick, 'download_button')

        if not package:
            # we instantiate an empty package for obtaining its metadata
            # attributes
            package = dpm.package.Package()

        self.m_package = package

        # frame_info retrieving
        # WARNING: this only works because we defined the Widget names with the same
        # names of those defined in dpm.metadata.Metadata. It's a sort of Reflection.
        for key, value in lib.info(package, request_for="metadata").iteritems():
            setattr(self, key + "_text", wx.xrc.XRCCTRL(self.m_frame, key + "_text"))

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

    def OnButtonDownloadClick(self, event):
        """
        Retrieve the currently selected package in the results list and launch a DownloadOperation
        for downloading it.
        """
        download_dir = self.DownloadDirDialog()
        if self.m_package and download_dir:
            operations.DownloadOperation(self.m_frame, self.m_package, download_dir)
            self.Show(False)
