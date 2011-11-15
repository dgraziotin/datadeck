__author__ = 'dgraziotin'
"""
This module holds the GUI for changing dpm and DataDeck settings
"""
import wx
import wx.xrc
import dpm

import dpm.lib

import datadeck.operations as operations
import datadeck.settings as settings
import base

class SettingsGUI(base.GUI):
    def __init__(self, xml, package=None):
        base.GUI.__init__(self, xml, frame_name="SettingsFrame", panel_name="panel")

        # minimum sizea
        self.m_frame.SetSize(wx.Size(500, 500))

        self.m_save_button = self.GetWidget('save_button')
        self.Bind(wx.EVT_BUTTON, self.OnButtonSaveClick, 'save_button')

        self.m_cancel_button = self.GetWidget('cancel_button')
        self.Bind(wx.EVT_BUTTON, self.OnButtonCancelClick, 'cancel_button')

        self.m_ckan_url_text = self.GetWidget('ckan_url_text')
        self.m_ckan_api_key_text = self.GetWidget('api_key_text')

        self.m_datadeck_dir_picker = self.GetWidget('datadeck_packages_dir_picker')

        self.LoadConfig()


    def OnButtonSaveClick(self, event):
        """
        Retrieve the currently selected package in the results list and launch a DownloadOperation
        for downloading it.
        """
        ckan_url = self.m_ckan_url_text.GetValue()
        ckan_api_key = self.m_ckan_api_key_text.GetValue()
        default_path = self.m_datadeck_dir_picker.GetPath()
        settings.Settings.ckan_url(ckan_url)
        settings.Settings.ckan_api(ckan_api_key)
        settings.Settings.datadeck_default_path(default_path)
        self.m_frame.Destroy()

    def OnButtonCancelClick(self, event):
        self.m_frame.Destroy()

    def LoadConfig(self):
        self.m_ckan_url_text.SetValue(settings.Settings.ckan_url())
        self.m_ckan_api_key_text.SetValue(settings.Settings.ckan_api())
        self.m_datadeck_dir_picker.SetPath(settings.Settings.datadeck_default_path())


        
