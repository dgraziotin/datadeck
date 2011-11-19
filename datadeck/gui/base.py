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
		
		self.m_menubar = wx.MenuBar( 0 )
		self.menu = wx.Menu()
		self.menu_settings = wx.MenuItem( self.menu, wx.ID_ANY, u"Settings", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu.AppendItem( self.menu_settings )
		
		self.menu_exit = wx.MenuItem( self.menu, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu.AppendItem( self.menu_exit )
		
		self.m_menubar.Append( self.menu, u"File" ) 
		
		self.about = wx.Menu()
		self.menu_about = wx.MenuItem( self.about, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.about.AppendItem( self.menu_about )
		
		self.m_menubar.Append( self.about, u"About" ) 
		
		self.SetMenuBar( self.m_menubar )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_notebook_search = wx.Panel( self.m_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_search_text = wx.TextCtrl( self.m_notebook_search, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_search_text, 4, wx.EXPAND|wx.RIGHT, 5 )
		
		self.m_search_button = wx.Button( self.m_notebook_search, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_search_button, 1, 0, 5 )
		
		self.m_info_button = wx.Button( self.m_notebook_search, wx.ID_ANY, u"Get Info", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_info_button, 1, 0, 5 )
		
		self.m_download_button = wx.Button( self.m_notebook_search, wx.ID_ANY, u"Download", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_download_button, 1, 0, 5 )
		
		bSizer2.Add( bSizer3, 0, wx.ALL|wx.EXPAND, 5 )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_notebook_search, wx.ID_ANY, u"Packages" ), wx.VERTICAL )
		
		self.m_search_results_listctrl = wx.ListCtrl( self.m_notebook_search, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		sbSizer1.Add( self.m_search_results_listctrl, 2, wx.ALL|wx.EXPAND, 5 )
		
		bSizer2.Add( sbSizer1, 3, wx.ALL|wx.EXPAND, 5 )
		
		self.m_notebook_search.SetSizer( bSizer2 )
		self.m_notebook_search.Layout()
		bSizer2.Fit( self.m_notebook_search )
		self.m_notebook.AddPage( self.m_notebook_search, u"Search", True )
		self.m_notebok_create = wx.Panel( self.m_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.name_label = wx.StaticText( self.m_notebok_create, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.name_label.Wrap( -1 )
		bSizer6.Add( self.name_label, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.name_text = wx.TextCtrl( self.m_notebok_create, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.name_text, 2, wx.ALL, 5 )
		
		bSizer5.Add( bSizer6, 1, wx.EXPAND, 5 )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.url_label = wx.StaticText( self.m_notebok_create, wx.ID_ANY, u"URL", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.url_label.Wrap( -1 )
		bSizer7.Add( self.url_label, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.url_text = wx.TextCtrl( self.m_notebok_create, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.url_text, 2, wx.ALL, 5 )
		
		bSizer5.Add( bSizer7, 1, wx.EXPAND, 5 )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.license_label = wx.StaticText( self.m_notebok_create, wx.ID_ANY, u"License", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.license_label.Wrap( -1 )
		bSizer8.Add( self.license_label, 1, wx.ALL|wx.EXPAND, 5 )
		
		license_choiceChoices = []
		self.license_choice = wx.Choice( self.m_notebok_create, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, license_choiceChoices, 0 )
		self.license_choice.SetSelection( 0 )
		bSizer8.Add( self.license_choice, 2, wx.ALL, 5 )
		
		bSizer5.Add( bSizer8, 1, wx.EXPAND, 5 )
		
		bSizer71 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.author_label = wx.StaticText( self.m_notebok_create, wx.ID_ANY, u"Author", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.author_label.Wrap( -1 )
		bSizer71.Add( self.author_label, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.author_text = wx.TextCtrl( self.m_notebok_create, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer71.Add( self.author_text, 2, wx.ALL, 5 )
		
		bSizer5.Add( bSizer71, 1, wx.EXPAND, 5 )
		
		bSizer72 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.author_email_label = wx.StaticText( self.m_notebok_create, wx.ID_ANY, u"Email", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.author_email_label.Wrap( -1 )
		bSizer72.Add( self.author_email_label, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.author_email_text = wx.TextCtrl( self.m_notebok_create, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer72.Add( self.author_email_text, 2, wx.ALL, 5 )
		
		bSizer5.Add( bSizer72, 1, wx.EXPAND, 5 )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.notes_label = wx.StaticText( self.m_notebok_create, wx.ID_ANY, u"Notes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.notes_label.Wrap( -1 )
		bSizer11.Add( self.notes_label, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.notes_text = wx.TextCtrl( self.m_notebok_create, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer11.Add( self.notes_text, 2, wx.ALL|wx.EXPAND, 5 )
		
		bSizer5.Add( bSizer11, 3, wx.EXPAND, 5 )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.tags_label = wx.StaticText( self.m_notebok_create, wx.ID_ANY, u"Tags", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tags_label.Wrap( -1 )
		bSizer9.Add( self.tags_label, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.tags_text = wx.TextCtrl( self.m_notebok_create, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tags_text.SetToolTipString( u"Separate tags with spaces, unite-words-with-dashes " )
		
		bSizer9.Add( self.tags_text, 2, wx.ALL, 5 )
		
		bSizer5.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		bSizer91 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.destination_label = wx.StaticText( self.m_notebok_create, wx.ID_ANY, u"Destination Path", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.destination_label.Wrap( -1 )
		bSizer91.Add( self.destination_label, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.destination_dirpicker = wx.DirPickerCtrl( self.m_notebok_create, wx.ID_ANY, u"/home/dgraziotin", u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer91.Add( self.destination_dirpicker, 2, wx.ALL, 5 )
		
		bSizer5.Add( bSizer91, 1, wx.EXPAND, 5 )
		
		bSizer61 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer61.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_create_button = wx.Button( self.m_notebok_create, wx.ID_ANY, u"Create Package", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer61.Add( self.m_create_button, 2, wx.ALL, 5 )
		
		bSizer5.Add( bSizer61, 1, wx.EXPAND, 5 )
		
		self.m_notebok_create.SetSizer( bSizer5 )
		self.m_notebok_create.Layout()
		bSizer5.Fit( self.m_notebok_create )
		self.m_notebook.AddPage( self.m_notebok_create, u"Create", False )
		
		bSizer1.Add( self.m_notebook, 3, wx.EXPAND |wx.ALL, 5 )
		
		self.m_console = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.m_console, wx.ID_ANY, u"Console Info" ), wx.VERTICAL )
		
		self.m_console_text = wx.TextCtrl( self.m_console, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_MULTILINE|wx.TE_READONLY )
		self.m_console_text.SetBackgroundColour( wx.Colour( 246, 246, 245 ) )
		
		sbSizer3.Add( self.m_console_text, 3, wx.ALL|wx.EXPAND, 5 )
		
		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_console_clear_button = wx.Button( self.m_console, wx.ID_ANY, u"Clear Console", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_console_clear_button, 1, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.m_operations_kill_button = wx.Button( self.m_console, wx.ID_ANY, u"Kill Operations", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_operations_kill_button, 0, wx.ALL, 5 )
		
		sbSizer3.Add( bSizer13, 1, wx.EXPAND, 5 )
		
		self.m_console.SetSizer( sbSizer3 )
		self.m_console.Layout()
		sbSizer3.Fit( self.m_console )
		bSizer1.Add( self.m_console, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.SetSizer( bSizer1 )
		self.Layout()
		bSizer1.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.OnMenuSettingsClick, id = self.menu_settings.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuExitClick, id = self.menu_exit.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuAboutClick, id = self.menu_about.GetId() )
		self.m_search_text.Bind( wx.EVT_KEY_DOWN, self.OnSearchTextKeyDown )
		self.m_search_button.Bind( wx.EVT_BUTTON, self.OnButtonSearchClick )
		self.m_info_button.Bind( wx.EVT_BUTTON, self.OnButtonInfoClick )
		self.m_download_button.Bind( wx.EVT_BUTTON, self.OnButtonDownloadClick )
		self.m_search_results_listctrl.Bind( wx.EVT_LIST_ITEM_SELECTED, self.OnSearchResultsListItemSelected )
		self.name_text.Bind( wx.EVT_KILL_FOCUS, self.OnNameTextKillFocus )
		self.m_create_button.Bind( wx.EVT_BUTTON, self.OnButtonCreateClick )
		self.m_console_clear_button.Bind( wx.EVT_BUTTON, self.OnConsoleClearButtonClick )
		self.m_operations_kill_button.Bind( wx.EVT_BUTTON, self.OnOperationsKillButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnMenuSettingsClick( self, event ):
		event.Skip()
	
	def OnMenuExitClick( self, event ):
		event.Skip()
	
	def OnMenuAboutClick( self, event ):
		event.Skip()
	
	def OnSearchTextKeyDown( self, event ):
		event.Skip()
	
	def OnButtonSearchClick( self, event ):
		event.Skip()
	
	def OnButtonInfoClick( self, event ):
		event.Skip()
	
	def OnButtonDownloadClick( self, event ):
		event.Skip()
	
	def OnSearchResultsListItemSelected( self, event ):
		event.Skip()
	
	def OnNameTextKillFocus( self, event ):
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
		
		self.panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer23 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self.panel, wx.ID_ANY, u"TheDataHub" ), wx.VERTICAL )
		
		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ckan_url_label = wx.StaticText( self.panel, wx.ID_ANY, u"API URL", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ckan_url_label.Wrap( -1 )
		bSizer24.Add( self.ckan_url_label, 0, wx.ALL, 5 )
		
		self.ckan_url_text = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.ckan_url_text, 2, wx.ALL, 5 )
		
		sbSizer5.Add( bSizer24, 2, wx.ALL|wx.EXPAND, 5 )
		
		bSizer241 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.api_key_label = wx.StaticText( self.panel, wx.ID_ANY, u"API Key", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.api_key_label.Wrap( -1 )
		bSizer241.Add( self.api_key_label, 0, wx.ALL, 5 )
		
		self.api_key_text = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer241.Add( self.api_key_text, 2, wx.ALL, 5 )
		
		sbSizer5.Add( bSizer241, 2, wx.ALL|wx.EXPAND, 5 )
		
		bSizer29 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText17 = wx.StaticText( self.panel, wx.ID_ANY, u"Register for an API Key", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		bSizer29.Add( self.m_staticText17, 1, wx.ALL, 5 )
		
		self.m_hyperlink5 = wx.HyperlinkCtrl( self.panel, wx.ID_ANY, u"http://thedatahub.org/user/register", u"http://thedatahub.org/user/register", wx.DefaultPosition, wx.DefaultSize, wx.HL_DEFAULT_STYLE )
		bSizer29.Add( self.m_hyperlink5, 2, wx.ALL, 5 )
		
		sbSizer5.Add( bSizer29, 1, wx.ALL, 5 )
		
		bSizer23.Add( sbSizer5, 1, wx.ALL|wx.EXPAND, 5 )
		
		sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self.panel, wx.ID_ANY, u"DataDeck" ), wx.VERTICAL )
		
		bSizer242 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.datadeck_packages_label = wx.StaticText( self.panel, wx.ID_ANY, u"Default Folder for Packages", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.datadeck_packages_label.Wrap( -1 )
		bSizer242.Add( self.datadeck_packages_label, 0, wx.ALL, 10 )
		
		self.datadeck_packages_dir_picker = wx.DirPickerCtrl( self.panel, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer242.Add( self.datadeck_packages_dir_picker, 2, wx.ALL, 5 )
		
		sbSizer6.Add( bSizer242, 1, wx.EXPAND, 5 )
		
		bSizer23.Add( sbSizer6, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer25 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.save_button = wx.Button( self.panel, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer25.Add( self.save_button, 0, wx.ALL, 5 )
		
		self.cancel_button = wx.Button( self.panel, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer25.Add( self.cancel_button, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		bSizer23.Add( bSizer25, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.panel.SetSizer( bSizer23 )
		self.panel.Layout()
		bSizer23.Fit( self.panel )
		bSizer22.Add( self.panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.SetSizer( bSizer22 )
		self.Layout()
		bSizer22.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.save_button.Bind( wx.EVT_BUTTON, self.OnButtonSaveClick )
		self.cancel_button.Bind( wx.EVT_BUTTON, self.OnButtonCancelClick )
	
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
		
		self.panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.name_label = wx.StaticText( self.panel, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.name_label.Wrap( -1 )
		bSizer6.Add( self.name_label, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.name_text = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer6.Add( self.name_text, 2, wx.ALL, 5 )
		
		bSizer5.Add( bSizer6, 1, wx.EXPAND, 5 )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.url_label = wx.StaticText( self.panel, wx.ID_ANY, u"URL", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.url_label.Wrap( -1 )
		bSizer7.Add( self.url_label, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.url_text = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer7.Add( self.url_text, 2, wx.ALL, 5 )
		
		bSizer5.Add( bSizer7, 1, wx.EXPAND, 5 )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.license_label = wx.StaticText( self.panel, wx.ID_ANY, u"License", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.license_label.Wrap( -1 )
		bSizer8.Add( self.license_label, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.license_text = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer8.Add( self.license_text, 2, wx.ALL, 5 )
		
		bSizer5.Add( bSizer8, 1, wx.EXPAND, 5 )
		
		bSizer71 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.author_label = wx.StaticText( self.panel, wx.ID_ANY, u"Author", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.author_label.Wrap( -1 )
		bSizer71.Add( self.author_label, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.author_text = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer71.Add( self.author_text, 2, wx.ALL, 5 )
		
		bSizer5.Add( bSizer71, 1, wx.EXPAND, 5 )
		
		bSizer72 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.author_email_label = wx.StaticText( self.panel, wx.ID_ANY, u"Email", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.author_email_label.Wrap( -1 )
		bSizer72.Add( self.author_email_label, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.author_email_text = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer72.Add( self.author_email_text, 2, wx.ALL, 5 )
		
		bSizer5.Add( bSizer72, 1, wx.EXPAND, 5 )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.notes_label = wx.StaticText( self.panel, wx.ID_ANY, u"Notes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.notes_label.Wrap( -1 )
		bSizer11.Add( self.notes_label, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.notes_text = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer11.Add( self.notes_text, 2, wx.ALL|wx.EXPAND, 5 )
		
		bSizer5.Add( bSizer11, 3, wx.EXPAND, 5 )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.tags_label = wx.StaticText( self.panel, wx.ID_ANY, u"Tags", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tags_label.Wrap( -1 )
		bSizer9.Add( self.tags_label, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.tags_text = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer9.Add( self.tags_text, 2, wx.ALL, 5 )
		
		bSizer5.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		self.m_close_button = wx.Button( self.panel, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_close_button, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.panel.SetSizer( bSizer5 )
		self.panel.Layout()
		bSizer5.Fit( self.panel )
		bSizer4.Add( self.panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.SetSizer( bSizer4 )
		self.Layout()
		bSizer4.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_close_button.Bind( wx.EVT_BUTTON, self.OnButtonCloseClick )
	
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
		
		self.panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		self.datadeck_label = wx.StaticText( self.panel, wx.ID_ANY, u"DataDeck", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.datadeck_label.Wrap( -1 )
		self.datadeck_label.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer14.Add( self.datadeck_label, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		bSizer161 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.website_label = wx.StaticText( self.panel, wx.ID_ANY, u"Website", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.website_label.Wrap( -1 )
		bSizer161.Add( self.website_label, 1, wx.ALL, 5 )
		
		self.website_hyperlink = wx.HyperlinkCtrl( self.panel, wx.ID_ANY, wx.EmptyString, u"http://task3.cc/projects/datadeck", wx.DefaultPosition, wx.DefaultSize, wx.HL_ALIGN_LEFT )
		bSizer161.Add( self.website_hyperlink, 5, wx.ALL, 5 )
		
		bSizer14.Add( bSizer161, 1, wx.EXPAND, 5 )
		
		bSizer1611 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bugs_label = wx.StaticText( self.panel, wx.ID_ANY, u"Bugs", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bugs_label.Wrap( -1 )
		bSizer1611.Add( self.bugs_label, 1, wx.ALL, 5 )
		
		self.bugs_hyperlink = wx.HyperlinkCtrl( self.panel, wx.ID_ANY, wx.EmptyString, u"https://github.com/dgraziotin/datadeck/issues", wx.DefaultPosition, wx.DefaultSize, wx.HL_ALIGN_LEFT )
		bSizer1611.Add( self.bugs_hyperlink, 5, wx.ALL, 5 )
		
		bSizer14.Add( bSizer1611, 1, wx.EXPAND, 5 )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.panel, wx.ID_ANY, u"License" ), wx.VERTICAL )
		
		self.license_text = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		sbSizer3.Add( self.license_text, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer14.Add( sbSizer3, 5, wx.EXPAND, 5 )
		
		self.panel.SetSizer( bSizer14 )
		self.panel.Layout()
		bSizer14.Fit( self.panel )
		bSizer16.Add( self.panel, 1, wx.EXPAND |wx.ALL, 5 )
		
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
		
		self.panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		self.datadeck_label = wx.StaticText( self.panel, wx.ID_ANY, u"DataDeck", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.datadeck_label.Wrap( -1 )
		self.datadeck_label.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer14.Add( self.datadeck_label, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		bSizer161 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.website_label = wx.StaticText( self.panel, wx.ID_ANY, u"Website", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.website_label.Wrap( -1 )
		bSizer161.Add( self.website_label, 1, wx.ALL, 5 )
		
		self.website_hyperlink = wx.HyperlinkCtrl( self.panel, wx.ID_ANY, wx.EmptyString, u"http://task3.cc/projects/datadeck", wx.DefaultPosition, wx.DefaultSize, wx.HL_ALIGN_LEFT )
		bSizer161.Add( self.website_hyperlink, 5, wx.ALL, 5 )
		
		bSizer14.Add( bSizer161, 1, wx.EXPAND, 5 )
		
		bSizer1611 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bugs_label = wx.StaticText( self.panel, wx.ID_ANY, u"Bugs", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bugs_label.Wrap( -1 )
		bSizer1611.Add( self.bugs_label, 1, wx.ALL, 5 )
		
		self.bugs_hyperlink = wx.HyperlinkCtrl( self.panel, wx.ID_ANY, wx.EmptyString, u"https://github.com/dgraziotin/datadeck/issues", wx.DefaultPosition, wx.DefaultSize, wx.HL_ALIGN_LEFT )
		bSizer1611.Add( self.bugs_hyperlink, 5, wx.ALL, 5 )
		
		bSizer14.Add( bSizer1611, 1, wx.EXPAND, 5 )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.panel, wx.ID_ANY, u"Missing dpm" ), wx.VERTICAL )
		
		self.dependencies_text = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		sbSizer3.Add( self.dependencies_text, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer14.Add( sbSizer3, 5, wx.EXPAND, 5 )
		
		self.panel.SetSizer( bSizer14 )
		self.panel.Layout()
		bSizer14.Fit( self.panel )
		bSizer16.Add( self.panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.SetSizer( bSizer16 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

