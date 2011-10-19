__author__ = 'dgraziotin'
"""
Module holding all the operations of Datapkg. Operations are extended Python Threads that communicate to the GUI
through special objects called Operation Messages.
Many of the steps of this module were possible thanks to this post:
http://www.blog.pythonlibrary.org/2010/05/22/wxpython-and-threads/
"""
import os
import threading
import wx
import lib

# Define notification event for thread completion
OPERATION_MESSAGE_ID = wx.NewId()

# Possible status of an Operation
OPERATION_STATUS_ID = {
    "started": wx.NewId(),
    "finished": wx.NewId(),
    "error": wx.NewId(),
    "info": wx.NewId(),
}

def OPERATION_MESSAGE_HANDLER(frame, method):
    frame.Connect(-1, -1, OPERATION_MESSAGE_ID, method)


class OperationMessage(wx.PyEvent):
    """
    An Event that is used as data format for communication from threads to the GUI.
    An OperationMessage has a type (e.g. SearchOperation), a status (e.g. "finished") and some data (e.g. Packages)
    """
    def __init__(self, type, status, data=None):
        wx.PyEvent.__init__(self)
        self.SetEventType(OPERATION_MESSAGE_ID)
        self.type = type
        self.status = status
        self.data = data


class Operation(threading.Thread):
    """
    Base class defining an operation. The constructor is only responsible for linking a wx object (e.g. a Frame)
    that will be signaled.
    """
    def __init__(self, linked_wxobject):
        threading.Thread.__init__(self)
        self.m_wxobject = linked_wxobject

    def run(self):
        raise NotImplementedError


class DownloadOperation(Operation):
    """
    Hybrid thread. It creates a DirDialog in the main thread for selecting a download directory.
    Then, calls lib.download in a separate thread for retrieving the package.
    """
    def __init__(self, linked_wxobject, package):
        Operation.__init__(self, linked_wxobject)
        self.package = package
        self.download_dir = self.DirDialog()
        self.start()

    #TODO: maybe we should move it to maingui.py and add a download_dir parameter to Download()
    def DirDialog(self):
        dialog = wx.DirDialog(self.m_wxobject, "Choose a Download Directory", os.getcwd())
        if dialog.ShowModal() == wx.ID_OK:
            download_dir = dialog.GetPath()
            return download_dir
        else:
            return None

    def Download(self, package):
        if self.download_dir:
            wx.PostEvent(self.m_wxobject,
                         OperationMessage(self.__class__, OPERATION_STATUS_ID["started"], None))
            lib.download("ckan://" + package.name, self.download_dir)
            return True
        else:
            return False

    def run(self):
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
        