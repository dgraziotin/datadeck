#TODO evaluate how much sense has this, it directly accesses MainGUI attributes.
class ConsoleUtil(object):
    """
    GUI utilities for the Console
    """
    def __init__(self, wxframe):
        self.m_wxframe = wxframe

    def OnUpdateConsole(self, event):
        """
        Update the Console text
        """
        value = event.text
        self.m_wxframe.m_console_tc.AppendText(value)

    def OnProcessPendingEventsConsole(self, event):
        """
        Handle pending events
        """
        self.m_wxframe.m_console_tc.ProcessPendingEvents()

    def OnConsoleClearButtonClick(self, event):
        self.m_wxframe.m_console_tc.Clear()

    def OnConsoleClearButtonClick(self, event):
        self.m_wxframe.m_console_tc.Clear()
