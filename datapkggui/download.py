__author__ = 'dgraziotin'
"""
Module holding the Download utilities
Coding standard: http://www.wxpython.org/codeguidelines.php
"""
class Download(object):
    def DownloadDialog(self):
        dialog = wx.DirDialog(self.m_frame_main, "Choose a Download Directory", os.getcwd())
        if dialog.ShowModal() == wx.ID_OK:
            download_dir = dialog.GetPath()
            return download_dir
        dialog.Destroy()