class SearchResults(object):
    def __init__(self, wxframe):
        self.m_wxframe = wxframe
        # search results
        self.m_results = {}
        self.m_index = 0

    def Get(self, index):
        return self.m_results[index]

    def Add(self, package):
        self.m_results[self.m_index] = package
        self.m_index += 1

    def Clear(self):
        self.m_index = 0
        self.m_results = {}
