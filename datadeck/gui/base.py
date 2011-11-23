# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Oct 12 2011)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx

###########################################################################
## Class DataDeckFrame
###########################################################################

class DataDeckFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"DataDeck", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.m_menu_mb = wx.MenuBar( 0 )
		self.m_file_m = wx.Menu()
		self.m_file_new_mi = wx.MenuItem( self.m_file_m, wx.ID_ANY, u"New Package", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_file_m.AppendItem( self.m_file_new_mi )
		
		self.m_file_open_mi = wx.MenuItem( self.m_file_m, wx.ID_ANY, u"Open", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_file_m.AppendItem( self.m_file_open_mi )
		
		self.m_file_settings_mi = wx.MenuItem( self.m_file_m, wx.ID_ANY, u"Settings", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_file_m.AppendItem( self.m_file_settings_mi )
		
		self.m_file_exit_mi = wx.MenuItem( self.m_file_m, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_file_m.AppendItem( self.m_file_exit_mi )
		
		self.m_menu_mb.Append( self.m_file_m, u"File" ) 
		
		self.m_about_m = wx.Menu()
		self.m_about_about_mi = wx.MenuItem( self.m_about_m, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_about_m.AppendItem( self.m_about_about_mi )
		
		self.m_menu_mb.Append( self.m_about_m, u"About" ) 
		
		self.SetMenuBar( self.m_menu_mb )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebook_n = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_notebook_library_p = wx.Panel( self.m_notebook_n, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer21 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer31 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_library_info_b = wx.Button( self.m_notebook_library_p, wx.ID_ANY, u"Info", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_library_info_b.Enable( False )
		
		bSizer31.Add( self.m_library_info_b, 1, 0, 5 )
		
		self.m_library_edit_b = wx.Button( self.m_notebook_library_p, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_library_edit_b.Enable( False )
		
		bSizer31.Add( self.m_library_edit_b, 1, 0, 5 )
		
		self.m_library_delete_b = wx.Button( self.m_notebook_library_p, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_library_delete_b.Enable( False )
		
		bSizer31.Add( self.m_library_delete_b, 1, 0, 5 )
		
		bSizer21.Add( bSizer31, 0, wx.ALL|wx.EXPAND, 5 )
		
		sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( self.m_notebook_library_p, wx.ID_ANY, u"Local Packages" ), wx.VERTICAL )
		
		self.m_library_lc = wx.ListCtrl( self.m_notebook_library_p, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		sbSizer11.Add( self.m_library_lc, 2, wx.ALL|wx.EXPAND, 5 )
		
		self.m_library_refresh_b = wx.Button( self.m_notebook_library_p, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer11.Add( self.m_library_refresh_b, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer21.Add( sbSizer11, 5, wx.ALL|wx.EXPAND, 5 )
		
		self.m_notebook_library_p.SetSizer( bSizer21 )
		self.m_notebook_library_p.Layout()
		bSizer21.Fit( self.m_notebook_library_p )
		self.m_notebook_n.AddPage( self.m_notebook_library_p, u"Library", True )
		self.m_notebook_search_p = wx.Panel( self.m_notebook_n, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_search_tc = wx.TextCtrl( self.m_notebook_search_p, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_search_tc, 4, wx.EXPAND|wx.RIGHT, 5 )
		
		self.m_search_b = wx.Button( self.m_notebook_search_p, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_search_b, 1, 0, 5 )
		
		self.m_search_info_b = wx.Button( self.m_notebook_search_p, wx.ID_ANY, u"Info", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_search_info_b.Enable( False )
		
		bSizer3.Add( self.m_search_info_b, 1, 0, 5 )
		
		self.m_search_download_b = wx.Button( self.m_notebook_search_p, wx.ID_ANY, u"Download", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_search_download_b.Enable( False )
		
		bSizer3.Add( self.m_search_download_b, 1, 0, 5 )
		
		bSizer2.Add( bSizer3, 0, wx.ALL|wx.EXPAND, 5 )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_notebook_search_p, wx.ID_ANY, u"Search Results" ), wx.VERTICAL )
		
		self.m_search_lc = wx.ListCtrl( self.m_notebook_search_p, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		sbSizer1.Add( self.m_search_lc, 2, wx.ALL|wx.EXPAND, 5 )
		
		bSizer2.Add( sbSizer1, 3, wx.ALL|wx.EXPAND, 5 )
		
		self.m_notebook_search_p.SetSizer( bSizer2 )
		self.m_notebook_search_p.Layout()
		bSizer2.Fit( self.m_notebook_search_p )
		self.m_notebook_n.AddPage( self.m_notebook_search_p, u"Search", False )
		self.m_notebok_create_p = wx.Panel( self.m_notebook_n, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_create_name_st = wx.StaticText( self.m_notebok_create_p, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_create_name_st.Wrap( -1 )
		bSizer6.Add( self.m_create_name_st, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_create_name_tc = wx.TextCtrl( self.m_notebok_create_p, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_create_name_tc, 2, wx.ALL, 5 )
		
		bSizer5.Add( bSizer6, 1, wx.EXPAND, 5 )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_create_url_st = wx.StaticText( self.m_notebok_create_p, wx.ID_ANY, u"URL", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_create_url_st.Wrap( -1 )
		bSizer7.Add( self.m_create_url_st, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_create_url_tc = wx.TextCtrl( self.m_notebok_create_p, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_create_url_tc, 2, wx.ALL, 5 )
		
		bSizer5.Add( bSizer7, 1, wx.EXPAND, 5 )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_create_license_st = wx.StaticText( self.m_notebok_create_p, wx.ID_ANY, u"License", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_create_license_st.Wrap( -1 )
		bSizer8.Add( self.m_create_license_st, 1, wx.ALL|wx.EXPAND, 5 )
		
		m_create_license_cChoices = []
		self.m_create_license_c = wx.Choice( self.m_notebok_create_p, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_create_license_cChoices, 0 )
		self.m_create_license_c.SetSelection( 0 )
		bSizer8.Add( self.m_create_license_c, 2, wx.ALL, 5 )
		
		bSizer5.Add( bSizer8, 1, wx.EXPAND, 5 )
		
		bSizer71 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_create_author_st = wx.StaticText( self.m_notebok_create_p, wx.ID_ANY, u"Author", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_create_author_st.Wrap( -1 )
		bSizer71.Add( self.m_create_author_st, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_create_author_tc = wx.TextCtrl( self.m_notebok_create_p, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer71.Add( self.m_create_author_tc, 2, wx.ALL, 5 )
		
		bSizer5.Add( bSizer71, 1, wx.EXPAND, 5 )
		
		bSizer72 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_create_author_email_st = wx.StaticText( self.m_notebok_create_p, wx.ID_ANY, u"Email", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_create_author_email_st.Wrap( -1 )
		bSizer72.Add( self.m_create_author_email_st, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_create_author_email_tc = wx.TextCtrl( self.m_notebok_create_p, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer72.Add( self.m_create_author_email_tc, 2, wx.ALL, 5 )
		
		bSizer5.Add( bSizer72, 1, wx.EXPAND, 5 )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_create_notes_st = wx.StaticText( self.m_notebok_create_p, wx.ID_ANY, u"Notes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_create_notes_st.Wrap( -1 )
		bSizer11.Add( self.m_create_notes_st, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_create_notes_tc = wx.TextCtrl( self.m_notebok_create_p, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer11.Add( self.m_create_notes_tc, 2, wx.ALL|wx.EXPAND, 5 )
		
		bSizer5.Add( bSizer11, 3, wx.EXPAND, 5 )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_create_tags_st = wx.StaticText( self.m_notebok_create_p, wx.ID_ANY, u"Tags", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_create_tags_st.Wrap( -1 )
		bSizer9.Add( self.m_create_tags_st, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_create_tags_tc = wx.TextCtrl( self.m_notebok_create_p, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_create_tags_tc.SetToolTipString( u"Separate tags with spaces, unite-words-with-dashes " )
		
		bSizer9.Add( self.m_create_tags_tc, 2, wx.ALL, 5 )
		
		bSizer5.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		bSizer61 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer61.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_create_save_b = wx.Button( self.m_notebok_create_p, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer61.Add( self.m_create_save_b, 2, wx.ALL, 5 )
		
		bSizer5.Add( bSizer61, 1, wx.EXPAND, 5 )
		
		self.m_notebok_create_p.SetSizer( bSizer5 )
		self.m_notebok_create_p.Layout()
		bSizer5.Fit( self.m_notebok_create_p )
		self.m_notebook_n.AddPage( self.m_notebok_create_p, u"Create", False )
		
		bSizer1.Add( self.m_notebook_n, 3, wx.EXPAND |wx.ALL, 5 )
		
		self.m_console_p = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.m_console_p, wx.ID_ANY, u"Console Info" ), wx.VERTICAL )
		
		self.m_console_tc = wx.TextCtrl( self.m_console_p, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_MULTILINE|wx.TE_READONLY )
		self.m_console_tc.SetBackgroundColour( wx.Colour( 246, 246, 245 ) )
		
		sbSizer3.Add( self.m_console_tc, 3, wx.ALL|wx.EXPAND, 5 )
		
		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_console_clear_b = wx.Button( self.m_console_p, wx.ID_ANY, u"Clear Console", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_console_clear_b, 1, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.m_console_killoperations_b = wx.Button( self.m_console_p, wx.ID_ANY, u"Kill Operations", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_console_killoperations_b, 0, wx.ALL, 5 )
		
		sbSizer3.Add( bSizer13, 1, wx.EXPAND, 5 )
		
		self.m_console_p.SetSizer( sbSizer3 )
		self.m_console_p.Layout()
		sbSizer3.Fit( self.m_console_p )
		bSizer1.Add( self.m_console_p, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.SetSizer( bSizer1 )
		self.Layout()
		bSizer1.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.OnMenuNewClick, id = self.m_file_new_mi.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuOpenClick, id = self.m_file_open_mi.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSettingsClick, id = self.m_file_settings_mi.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuExitClick, id = self.m_file_exit_mi.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuAboutClick, id = self.m_about_about_mi.GetId() )
		self.m_notebook_n.Bind( wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnNotebookPageChanged )
		self.m_library_info_b.Bind( wx.EVT_BUTTON, self.OnButtonLibraryInfoClick )
		self.m_library_edit_b.Bind( wx.EVT_BUTTON, self.OnButtonLibraryEditClick )
		self.m_library_delete_b.Bind( wx.EVT_BUTTON, self.OnButtonLibraryDeleteClick )
		self.m_library_lc.Bind( wx.EVT_LIST_ITEM_DESELECTED, self.OnLibraryListItemDeselected )
		self.m_library_lc.Bind( wx.EVT_LIST_ITEM_SELECTED, self.OnLibraryListItemSelected )
		self.m_library_refresh_b.Bind( wx.EVT_BUTTON, self.OnButtonRefreshClick )
		self.m_search_tc.Bind( wx.EVT_KEY_DOWN, self.OnSearchTextKeyDown )
		self.m_search_b.Bind( wx.EVT_BUTTON, self.OnButtonSearchClick )
		self.m_search_info_b.Bind( wx.EVT_BUTTON, self.OnButtonInfoClick )
		self.m_search_download_b.Bind( wx.EVT_BUTTON, self.OnButtonDownloadClick )
		self.m_search_lc.Bind( wx.EVT_LIST_ITEM_DESELECTED, self.OnSearchResultsListItemDeselected )
		self.m_search_lc.Bind( wx.EVT_LIST_ITEM_SELECTED, self.OnSearchResultsListItemSelected )
		self.m_create_save_b.Bind( wx.EVT_BUTTON, self.OnButtonCreateClick )
		self.m_console_clear_b.Bind( wx.EVT_BUTTON, self.OnConsoleClearButtonClick )
		self.m_console_killoperations_b.Bind( wx.EVT_BUTTON, self.OnOperationsKillButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnMenuNewClick( self, event ):
		event.Skip()
	
	def OnMenuOpenClick( self, event ):
		event.Skip()
	
	def OnMenuSettingsClick( self, event ):
		event.Skip()
	
	def OnMenuExitClick( self, event ):
		event.Skip()
	
	def OnMenuAboutClick( self, event ):
		event.Skip()
	
	def OnNotebookPageChanged( self, event ):
		event.Skip()
	
	def OnButtonLibraryInfoClick( self, event ):
		event.Skip()
	
	def OnButtonLibraryEditClick( self, event ):
		event.Skip()
	
	def OnButtonLibraryDeleteClick( self, event ):
		event.Skip()
	
	def OnLibraryListItemDeselected( self, event ):
		event.Skip()
	
	def OnLibraryListItemSelected( self, event ):
		event.Skip()
	
	def OnButtonRefreshClick( self, event ):
		event.Skip()
	
	def OnSearchTextKeyDown( self, event ):
		event.Skip()
	
	def OnButtonSearchClick( self, event ):
		event.Skip()
	
	def OnButtonInfoClick( self, event ):
		event.Skip()
	
	def OnButtonDownloadClick( self, event ):
		event.Skip()
	
	def OnSearchResultsListItemDeselected( self, event ):
		event.Skip()
	
	def OnSearchResultsListItemSelected( self, event ):
		event.Skip()
	
	def OnButtonCreateClick( self, event ):
		event.Skip()
	
	def OnConsoleClearButtonClick( self, event ):
		event.Skip()
	
	def OnOperationsKillButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class SettingsFrame
###########################################################################

class SettingsFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Settings", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer22 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer23 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel, wx.ID_ANY, u"TheDataHub" ), wx.VERTICAL )
		
		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_ckan_url_st = wx.StaticText( self.m_panel, wx.ID_ANY, u"API URL", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ckan_url_st.Wrap( -1 )
		bSizer24.Add( self.m_ckan_url_st, 0, wx.ALL, 5 )
		
		self.m_ckan_url_tc = wx.TextCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.m_ckan_url_tc, 2, wx.ALL, 5 )
		
		sbSizer5.Add( bSizer24, 2, wx.ALL|wx.EXPAND, 5 )
		
		bSizer241 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_api_key_st = wx.StaticText( self.m_panel, wx.ID_ANY, u"API Key", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_api_key_st.Wrap( -1 )
		bSizer241.Add( self.m_api_key_st, 0, wx.ALL, 5 )
		
		self.m_api_key_tc = wx.TextCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer241.Add( self.m_api_key_tc, 2, wx.ALL, 5 )
		
		sbSizer5.Add( bSizer241, 2, wx.ALL|wx.EXPAND, 5 )
		
		bSizer29 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText17 = wx.StaticText( self.m_panel, wx.ID_ANY, u"Register for an API Key", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		bSizer29.Add( self.m_staticText17, 1, wx.ALL, 5 )
		
		self.m_hyperlink5 = wx.HyperlinkCtrl( self.m_panel, wx.ID_ANY, u"http://thedatahub.org/user/register", u"http://thedatahub.org/user/register", wx.DefaultPosition, wx.DefaultSize, wx.HL_DEFAULT_STYLE )
		bSizer29.Add( self.m_hyperlink5, 2, wx.ALL, 5 )
		
		sbSizer5.Add( bSizer29, 1, wx.ALL, 5 )
		
		bSizer23.Add( sbSizer5, 1, wx.ALL|wx.EXPAND, 5 )
		
		sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel, wx.ID_ANY, u"DataDeck" ), wx.VERTICAL )
		
		bSizer242 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_datadeck_library_st = wx.StaticText( self.m_panel, wx.ID_ANY, u"Packages Library", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_datadeck_library_st.Wrap( -1 )
		bSizer242.Add( self.m_datadeck_library_st, 0, wx.ALL, 10 )
		
		self.m_datadeck_library_dp = wx.DirPickerCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer242.Add( self.m_datadeck_library_dp, 2, wx.ALL, 5 )
		
		sbSizer6.Add( bSizer242, 1, wx.EXPAND, 5 )
		
		bSizer23.Add( sbSizer6, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer25 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_save_b = wx.Button( self.m_panel, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer25.Add( self.m_save_b, 0, wx.ALL, 5 )
		
		self.m_cancel_b = wx.Button( self.m_panel, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer25.Add( self.m_cancel_b, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		bSizer23.Add( bSizer25, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.m_panel.SetSizer( bSizer23 )
		self.m_panel.Layout()
		bSizer23.Fit( self.m_panel )
		bSizer22.Add( self.m_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.SetSizer( bSizer22 )
		self.Layout()
		bSizer22.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_save_b.Bind( wx.EVT_BUTTON, self.OnButtonSaveClick )
		self.m_cancel_b.Bind( wx.EVT_BUTTON, self.OnButtonCancelClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnButtonSaveClick( self, event ):
		event.Skip()
	
	def OnButtonCancelClick( self, event ):
		event.Skip()
	

###########################################################################
## Class InfoFrame
###########################################################################

class InfoFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Package", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_name_st = wx.StaticText( self.m_panel, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_name_st.Wrap( -1 )
		bSizer6.Add( self.m_name_st, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_name_tc = wx.TextCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer6.Add( self.m_name_tc, 2, wx.ALL, 5 )
		
		bSizer5.Add( bSizer6, 1, wx.EXPAND, 5 )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_url_st = wx.StaticText( self.m_panel, wx.ID_ANY, u"URL", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_url_st.Wrap( -1 )
		bSizer7.Add( self.m_url_st, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_url_tc = wx.TextCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer7.Add( self.m_url_tc, 2, wx.ALL, 5 )
		
		bSizer5.Add( bSizer7, 1, wx.EXPAND, 5 )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_license_st = wx.StaticText( self.m_panel, wx.ID_ANY, u"License", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_license_st.Wrap( -1 )
		bSizer8.Add( self.m_license_st, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_license_tc = wx.TextCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer8.Add( self.m_license_tc, 2, wx.ALL, 5 )
		
		bSizer5.Add( bSizer8, 1, wx.EXPAND, 5 )
		
		bSizer71 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_author_st = wx.StaticText( self.m_panel, wx.ID_ANY, u"Author", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_author_st.Wrap( -1 )
		bSizer71.Add( self.m_author_st, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_author_tc = wx.TextCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer71.Add( self.m_author_tc, 2, wx.ALL, 5 )
		
		bSizer5.Add( bSizer71, 1, wx.EXPAND, 5 )
		
		bSizer72 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_author_email_st = wx.StaticText( self.m_panel, wx.ID_ANY, u"Email", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_author_email_st.Wrap( -1 )
		bSizer72.Add( self.m_author_email_st, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_author_email_tc = wx.TextCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer72.Add( self.m_author_email_tc, 2, wx.ALL, 5 )
		
		bSizer5.Add( bSizer72, 1, wx.EXPAND, 5 )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_notes_st = wx.StaticText( self.m_panel, wx.ID_ANY, u"Notes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_notes_st.Wrap( -1 )
		bSizer11.Add( self.m_notes_st, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_notes_tc = wx.TextCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer11.Add( self.m_notes_tc, 2, wx.ALL|wx.EXPAND, 5 )
		
		bSizer5.Add( bSizer11, 3, wx.EXPAND, 5 )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_tags_st = wx.StaticText( self.m_panel, wx.ID_ANY, u"Tags", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_tags_st.Wrap( -1 )
		bSizer9.Add( self.m_tags_st, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_tags_tc = wx.TextCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer9.Add( self.m_tags_tc, 2, wx.ALL, 5 )
		
		bSizer5.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		self.m_close_b = wx.Button( self.m_panel, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_close_b, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_panel.SetSizer( bSizer5 )
		self.m_panel.Layout()
		bSizer5.Fit( self.m_panel )
		bSizer4.Add( self.m_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.SetSizer( bSizer4 )
		self.Layout()
		bSizer4.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_close_b.Bind( wx.EVT_BUTTON, self.OnButtonCloseClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnButtonCloseClick( self, event ):
		event.Skip()
	

###########################################################################
## Class AboutFrame
###########################################################################

class AboutFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"About", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.RESIZE_BORDER|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer16 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_datadeck_st = wx.StaticText( self.m_panel, wx.ID_ANY, u"DataDeck", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_datadeck_st.Wrap( -1 )
		self.m_datadeck_st.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer14.Add( self.m_datadeck_st, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		bSizer161 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_website_st = wx.StaticText( self.m_panel, wx.ID_ANY, u"Website", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_website_st.Wrap( -1 )
		bSizer161.Add( self.m_website_st, 1, wx.ALL, 5 )
		
		self.m_website_hl = wx.HyperlinkCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, u"http://task3.cc/projects/datadeck", wx.DefaultPosition, wx.DefaultSize, wx.HL_ALIGN_LEFT )
		bSizer161.Add( self.m_website_hl, 5, wx.ALL, 5 )
		
		bSizer14.Add( bSizer161, 1, wx.EXPAND, 5 )
		
		bSizer1611 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bugs_st = wx.StaticText( self.m_panel, wx.ID_ANY, u"Bugs", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_bugs_st.Wrap( -1 )
		bSizer1611.Add( self.m_bugs_st, 1, wx.ALL, 5 )
		
		self.m_bugs_hl = wx.HyperlinkCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, u"https://github.com/dgraziotin/datadeck/issues", wx.DefaultPosition, wx.DefaultSize, wx.HL_ALIGN_LEFT )
		bSizer1611.Add( self.m_bugs_hl, 5, wx.ALL, 5 )
		
		bSizer14.Add( bSizer1611, 1, wx.EXPAND, 5 )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel, wx.ID_ANY, u"License" ), wx.VERTICAL )
		
		self.m_license_tc = wx.TextCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		sbSizer3.Add( self.m_license_tc, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer14.Add( sbSizer3, 5, wx.EXPAND, 5 )
		
		self.m_panel.SetSizer( bSizer14 )
		self.m_panel.Layout()
		bSizer14.Fit( self.m_panel )
		bSizer16.Add( self.m_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.SetSizer( bSizer16 )
		self.Layout()
		bSizer16.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class DepCheckFrame
###########################################################################

class DepCheckFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Dependencies", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer16 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_datadeck_st = wx.StaticText( self.m_panel, wx.ID_ANY, u"DataDeck", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_datadeck_st.Wrap( -1 )
		self.m_datadeck_st.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer14.Add( self.m_datadeck_st, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		bSizer161 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_website_st = wx.StaticText( self.m_panel, wx.ID_ANY, u"Website", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_website_st.Wrap( -1 )
		bSizer161.Add( self.m_website_st, 1, wx.ALL, 5 )
		
		self.m_website_hl = wx.HyperlinkCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, u"http://task3.cc/projects/datadeck", wx.DefaultPosition, wx.DefaultSize, wx.HL_ALIGN_LEFT )
		bSizer161.Add( self.m_website_hl, 5, wx.ALL, 5 )
		
		bSizer14.Add( bSizer161, 1, wx.EXPAND, 5 )
		
		bSizer1611 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bugs_st = wx.StaticText( self.m_panel, wx.ID_ANY, u"Bugs", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_bugs_st.Wrap( -1 )
		bSizer1611.Add( self.m_bugs_st, 1, wx.ALL, 5 )
		
		self.m_bugs_hl = wx.HyperlinkCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, u"https://github.com/dgraziotin/datadeck/issues", wx.DefaultPosition, wx.DefaultSize, wx.HL_ALIGN_LEFT )
		bSizer1611.Add( self.m_bugs_hl, 5, wx.ALL, 5 )
		
		bSizer14.Add( bSizer1611, 1, wx.EXPAND, 5 )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel, wx.ID_ANY, u"Missing dpm" ), wx.VERTICAL )
		
		self.m_dependencies_tc = wx.TextCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		sbSizer3.Add( self.m_dependencies_tc, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer14.Add( sbSizer3, 5, wx.EXPAND, 5 )
		
		self.m_panel.SetSizer( bSizer14 )
		self.m_panel.Layout()
		bSizer14.Fit( self.m_panel )
		bSizer16.Add( self.m_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.SetSizer( bSizer16 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

