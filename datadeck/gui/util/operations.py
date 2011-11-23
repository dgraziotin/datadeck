import os
import threading
import datadeck.operations

class OperationsUtil(object):
    """
    Utility methods to handle datadeck.operations things from the GUI
    """
    def __init__(self, wxframe):
        self.m_wxframe = wxframe
        self.m_killing_operations = False

    def OnOperationMessageReceived(self, operation_message):
            """
            Handler for Operation Messages. Detect the type of the Message received and take care of it.
            According to the status of the Message, inform the user and update the GUI.
            See operations.py
            """
            operation_type_str = operation_message.type.__name__
            if operation_message.status == datadeck.operations.OPERATION_STATUS_ID["error"] and self.m_killing_operations:
                self.m_killing_operations = False
                print operation_type_str + " Killed"
                return
            elif operation_message.status == datadeck.operations.OPERATION_STATUS_ID[
                                             "error"] and not self.m_killing_operations and operation_message.data:
                print operation_type_str + " ERROR: " + operation_message.data
            elif operation_message.status == datadeck.operations.OPERATION_STATUS_ID["started"]:
                print operation_type_str + " Started"
            elif operation_message.status == datadeck.operations.OPERATION_STATUS_ID["finished"]:
                print operation_type_str + " Finished"
                if operation_message.type == datadeck.operations.SearchOperation:
                    self.m_wxframe.CleanSearchResults()
                    results = operation_message.data
                    if results:
                        print "Results found."
                        for package in results:
                            self.m_wxframe.InsertSearchResultsList(package)
                    else:
                        print "No Results."
                if operation_message.type == datadeck.operations.InitAndSaveOperation:
                    package = operation_message.data
                    print "Package " + package.name + " successfully created at " + package.installed_path
                    self.m_wxframe.RefreshLibrary()
                if operation_message.type == datadeck.operations.DownloadOperation:
                    package = operation_message.data
                    print "Package " + package.name + " successfully downloaded at " + os.path.join(package.installed_path,
                        package.name)
                    self.m_wxframe.RefreshLibrary()
            else:
                pass

    def KillOperations(self):
        """
        Kills any active thread that is a datadeck.operation
        """
        for thread in  threading.enumerate():
            # check if the first super class is an Operation
            if thread.__class__.mro()[1] == datadeck.operations.Operation:
                self.m_killing_operations = True
                while thread.isAlive():
                    thread.RaiseException(datadeck.operations.KillOperationException)