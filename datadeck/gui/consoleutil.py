import threading
import datadeck.operations

class ConsoleUtil(object):
    def __init__(self, wxframe):
        self.m_wxframe = wxframe

    def OnUpdateConsole(self, event):
        """
        Update the Console text
        """
        value = event.text
        self.m_wxframe.m_console_text.AppendText(value)

    def OnProcessPendingEventsConsole(self, event):
        """
        Handle pending events
        """
        self.m_wxframe.m_console_text.ProcessPendingEvents()

    def OnConsoleKillButtonClick(self, event):
        """
        Kill all the currently running Operations
        """
        for thread in  threading.enumerate():
            # check if the first super class is an Operation
            if thread.__class__.mro()[1] == datadeck.operations.Operation:
                self.m_killing_operations = True
                while thread.isAlive():
                    thread.RaiseException(datadeck.operations.KillOperationException)

    def OnConsoleClearButtonClick(self, event):
        self.m_wxframe.m_console_text.Clear()

    def OnConsoleClearButtonClick(self, event):
        self.m_wxframe.m_console_text.Clear()
