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

    def OnConsoleClearButtonClick(self, event):
        self.m_wxframe.m_console_text.Clear()

    def OnConsoleClearButtonClick(self, event):
        self.m_wxframe.m_console_text.Clear()
