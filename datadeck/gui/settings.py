"""
This module holds the GUI for changing dpm and DataDeck settings
"""
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
        ckan_url = self.m_ckan_url_tc.GetValue()
        ckan_api_key = self.m_api_key_tc.GetValue()
        default_path = self.m_datadeck_library_dp.GetPath()
        settings.Settings.ckan_url(ckan_url)
        settings.Settings.ckan_api(ckan_api_key)
        settings.Settings.library_path(default_path)
        self.Destroy()

    def OnButtonCancelClick(self, event):
        self.Destroy()

    def LoadConfig(self):
        self.m_ckan_url_tc.SetValue(settings.Settings.ckan_url())
        self.m_api_key_tc.SetValue(settings.Settings.ckan_api())
        self.m_datadeck_library_dp.SetPath(settings.Settings.library_path())


        
