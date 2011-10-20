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
    It calls lib.download in a separate thread for retrieving the package and its resources.
    """
    def __init__(self, linked_wxobject, package, download_dir):
        Operation.__init__(self, linked_wxobject)
        self.package = package
        self.download_dir = download_dir
        self.start()

    def run(self):
        wx.PostEvent(self.m_wxobject, OperationMessage(self.__class__, OPERATION_STATUS_ID["started"]))
        try:
            result = lib.download("ckan://" + self.package.name, self.download_dir)
        except Exception, e:
            wx.PostEvent(self.m_wxobject, OperationMessage(self.__class__, OPERATION_STATUS_ID["error"], str(e)))
            return
        wx.PostEvent(self.m_wxobject, OperationMessage(self.__class__, OPERATION_STATUS_ID["finished"]))

class SearchOperation(Operation):
    """
    Given a query, it searches in Ckan using the query. If there are no exceptions,
    it communicates to the main GUI that the the search was finished, returning the retrieved Packages
    in an OperationMessage object.
    """
    def __init__(self, linked_wxobject, query):
        self.query = query
        Operation.__init__(self, linked_wxobject)
        self.start()

    def run(self):
        wx.PostEvent(self.m_wxobject,
                     OperationMessage(self.__class__, OPERATION_STATUS_ID["started"]))
        try:
            results = lib.search("ckan://", self.query)
        except Exception, e:
            wx.PostEvent(self.m_wxobject, OperationMessage(self.__class__, OPERATION_STATUS_ID["error"], str(e)))
            return
        wx.PostEvent(self.m_wxobject, OperationMessage(self.__class__, OPERATION_STATUS_ID["finished"], results))
        