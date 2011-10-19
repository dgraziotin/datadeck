import threading
import time
import wx
import main
import download
import lib
import os

"""
Many of the operations of this module were possible thanks to this post:
http://www.blog.pythonlibrary.org/2010/05/22/wxpython-and-threads/
"""
# Define notification event for thread completion
OPERATION_MESSAGE_ID = wx.NewId()

OPERATION_STATUS_ID = {
    "started": wx.NewId(),
    "finished": wx.NewId(),
    "error": wx.NewId(),
    "info": wx.NewId(),
    }

def OPERATION_MESSAGE(win, operation):
    """Define Result Event."""
    win.Connect(-1, -1, OPERATION_MESSAGE_ID, operation)


class OperationMessage(wx.PyEvent):
    """Simple event to carry arbitrary result data."""
    def __init__(self, type, status, data=None):
        """Init Result Event."""
        wx.PyEvent.__init__(self, )
        self.SetEventType(OPERATION_MESSAGE_ID)
        self.type = type
        self.status = status
        self.data = data


class Operation(threading.Thread):
    def __init__(self, linked_wxobject):
        threading.Thread.__init__(self)
        self.m_wxobject = linked_wxobject

    def run(self):
        raise NotImplementedError


class DownloadOperation(Operation):
    def __init__(self, linked_wxobject, package):
        self.package = package
        Operation.__init__(self, linked_wxobject)
        self.download_dir = self.DirDialog()
        self.start()

    def DirDialog(self):
        dialog = wx.DirDialog(self.m_wxobject, "Choose a Download Directory", os.getcwd())
        if dialog.ShowModal() == wx.ID_OK:
            download_dir = dialog.GetPath()
            return download_dir
        else:
            return None

    def Download(self, package):
        if self.download_dir:
            lib.download("ckan://" + package.name, self.download_dir)
            return True
        else:
            return False

    def run(self):
        wx.PostEvent(self.m_wxobject,
                     OperationMessage(self.__class__, OPERATION_STATUS_ID["started"], None))
        try:
            result = self.Download(self.package)
        except Exception, e:
            wx.PostEvent(self.m_wxobject, OperationMessage(self.__class__, OPERATION_STATUS_ID["error"], str(e)))
            return
        if result:
            wx.PostEvent(self.m_wxobject, OperationMessage(self.__class__, OPERATION_STATUS_ID["finished"], None))
        else:
            wx.PostEvent(self.m_wxobject,
                         OperationMessage(self.__class__, OPERATION_STATUS_ID["error"], None))


class SearchOperation(Operation):
    def __init__(self, linked_wxobject, query):
        self.query = query
        Operation.__init__(self, linked_wxobject)
        self.start()

    def run(self):
        wx.PostEvent(self.m_wxobject,
                     OperationMessage(self.__class__, OPERATION_STATUS_ID["started"], None))
        try:
            results = lib.search("ckan://", self.query)
        except Exception, e:
            wx.PostEvent(self.m_wxobject, OperationMessage(self.__class__, OPERATION_STATUS_ID["error"], str(e)))
            return
        wx.PostEvent(self.m_wxobject, OperationMessage(self.__class__, OPERATION_STATUS_ID["finished"], results))
        