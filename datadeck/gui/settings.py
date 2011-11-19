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

class SettingsGUI(base.SettingsFrame):
    def __init__(self, parent):
        base.SettingsFrame.__init__(self, parent)
        self.LoadConfig()


    def OnButtonSaveClick(self, event):
        """
        Retrieve the currently selected package in the results list and launch a DownloadOperation
        for downloading it.
        """
        ckan_url = self.ckan_url_text.GetValue()
        ckan_api_key = self.api_key_text.GetValue()
        default_path = self.datadeck_packages_dir_picker.GetPath()
        settings.Settings.ckan_url(ckan_url)
        settings.Settings.ckan_api(ckan_api_key)
        settings.Settings.datadeck_default_path(default_path)
        self.Destroy()

    def OnButtonCancelClick(self, event):
        self.Destroy()

    def LoadConfig(self):
        self.ckan_url_text.SetValue(settings.Settings.ckan_url())
        self.api_key_text.SetValue(settings.Settings.ckan_api())
        self.datadeck_packages_dir_picker.SetPath(settings.Settings.datadeck_default_path())


        
