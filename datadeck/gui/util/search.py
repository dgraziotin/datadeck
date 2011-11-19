class SearchResults(object):
    """
    Represents the internal search results list. It must be mapped with the GUI search results list (a wx.ListCtrl)
    """
    def __init__(self, wxframe):
        self.m_wxframe = wxframe
        self.m_results = []

    def Index(self):
        """
        For ensuring consistency with the GUI package list, returns the current length
        of the internal package list - 1.
        This is because a package is first added to the internal list, then to the GUI list.
        Therefore, the first package added in the GUI must have index = 0, not 1.
        The second package addded in the GUI must have index = 1, not 2.
        Etc.
        """
        return len(self.m_results) - 1

    def Get(self, index):
        """
        Given an Index, returns the corresponding Package
        """
        return self.m_results[index]

    def Add(self, package):
        """
        Adds a package in the internal results list.
        Returns the index that points to the added package.
        """
        self.m_results.append(package)
        return self.Index()

    def Clear(self):
        """
        Clears the internal list
        """
        self.m_results = []
