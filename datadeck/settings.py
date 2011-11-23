import dpm.lib

class Settings(object):
    _ckan_section = 'index:ckan'
    _ckan_url_option = 'ckan.url'
    _ckan_api_key_option = 'ckan.api_key'
    _datadeck_section = 'datadeck'
    _datadeck_library_path_option = 'library_path'

    _licenses = [u'Non-OKD Compliant::Creative Commons Non-Commercial (Any)',
                 u'Non-OKD Compliant::Crown Copyright',
                 u'Non-OKD Compliant::Non-Commercial Other',
                 u'Non-OKD Compliant::Other',
                 u'OKD Compliant::Creative Commons Attribution',
                 u'OKD Compliant::Creative Commons Attribution-ShareAlike',
                 u'OKD Compliant::Creative Commons CCZero',
                 u'OKD Compliant::GNU Free Documentation License (GFDL)',
                 u'OKD Compliant::Higher Education Statistics Agency Copyright with data.gov.uk rights',
                 u'OKD Compliant::Local Authority Copyright with data.gov.uk rights',
                 u'OKD Compliant::Open Data Commons Open Database License (ODbL)',
                 u'OKD Compliant::Open Data Commons Public Domain Dedication and License (PDDL)',
                 u'OKD Compliant::Other',
                 u'OKD Compliant::Other (Attribution)',
                 u'OKD Compliant::Other (Public Domain)',
                 u'OKD Compliant::Public Domain',
                 u'OKD Compliant::UK Click Use PSI',
                 u'OKD Compliant::UK Crown Copyright with data.gov.uk rights',
                 u'OSI Approved::Academic Free License',
                 u'OSI Approved::Adaptive Public License',
                 u'OSI Approved::Apache License, 2.0',
                 u'OSI Approved::Apache Software License',
                 u'OSI Approved::Apple Public Source License',
                 u'OSI Approved::Artistic license',
                 u'OSI Approved::Attribution Assurance Licenses',
                 u'OSI Approved::CUA Office Public License Version 1.0',
                 u'OSI Approved::Common Development and Distribution License',
                 u'OSI Approved::Common Public License 1.0',
                 u'OSI Approved::Computer Associates Trusted Open Source License 1.1',
                 u'OSI Approved::EU DataGrid Software License',
                 u'OSI Approved::Eclipse Public License',
                 u'OSI Approved::Educational Community License',
                 u'OSI Approved::Eiffel Forum License',
                 u'OSI Approved::Eiffel Forum License V2.0',
                 u'OSI Approved::Entessa Public License',
                 u'OSI Approved::Fair License',
                 u'OSI Approved::Frameworx License',
                 u'OSI Approved::GNU General Public License (GPL)',
                 u'OSI Approved::GNU General Public License v3 (GPLv3)',
                 u'OSI Approved::GNU Library or "Lesser" General Public License (LGPL)',
                 u'OSI Approved::IBM Public License',
                 u'OSI Approved::Intel Open Source License',
                 u'OSI Approved::Jabber Open Source License',
                 u'OSI Approved::Lucent Public License (Plan9)',
                 u'OSI Approved::Lucent Public License Version 1.02',
                 u'OSI Approved::MIT license',
                 u'OSI Approved::MITRE Collaborative Virtual Workspace License (CVW License)',
                 u'OSI Approved::Motosoto License',
                 u'OSI Approved::Mozilla Public License 1.0 (MPL)',
                 u'OSI Approved::Mozilla Public License 1.1 (MPL)',
                 u'OSI Approved::NASA Open Source Agreement 1.3',
                 u'OSI Approved::Naumen Public License',
                 u'OSI Approved::Nethack General Public License',
                 u'OSI Approved::New BSD license',
                 u'OSI Approved::Nokia Open Source License',
                 u'OSI Approved::OCLC Research Public License 2.0',
                 u'OSI Approved::Open Group Test Suite License',
                 u'OSI Approved::Open Software License',
                 u'OSI Approved::PHP License',
                 u'OSI Approved::Python Software Foundation License',
                 u'OSI Approved::Python license (CNRI Python License)',
                 u'OSI Approved::Qt Public License (QPL)',
                 u'OSI Approved::RealNetworks Public Source License V1.0',
                 u'OSI Approved::Reciprocal Public License',
                 u'OSI Approved::Ricoh Source Code Public License',
                 u'OSI Approved::Sleepycat License',
                 u'OSI Approved::Sun Industry Standards Source License (SISSL)',
                 u'OSI Approved::Sun Public License',
                 u'OSI Approved::Sybase Open Watcom Public License 1.0',
                 u'OSI Approved::University of Illinois/NCSA Open Source License',
                 u'OSI Approved::Vovida Software License v. 1.0',
                 u'OSI Approved::W3C License',
                 u'OSI Approved::X.Net License',
                 u'OSI Approved::Zope Public License',
                 u'OSI Approved::wxWindows Library License',
                 u'OSI Approved::zlib/libpng license',
                 u'Other::License Not Specified']

    @staticmethod
    def ckan_url(ckan_url=None):
        if not ckan_url:
            return dpm.lib.get_config(Settings._ckan_section, Settings._ckan_url_option)
        else:
            return dpm.lib.set_config(Settings._ckan_section, Settings._ckan_url_option, ckan_url)

    @staticmethod
    def ckan_api(ckan_api=None):
        if not ckan_api:
            return dpm.lib.get_config(Settings._ckan_section, Settings._ckan_api_key_option)
        else:
            return dpm.lib.set_config(Settings._ckan_section, Settings._ckan_api_key_option, ckan_api)

    @staticmethod
    def library_path(default_path=None):
        if not default_path:
            return dpm.lib.get_config(Settings._datadeck_section, Settings._datadeck_library_path_option)
        else:
            return dpm.lib.set_config(Settings._datadeck_section, Settings._datadeck_library_path_option,
                                      default_path)

    @staticmethod
    def licenses(key=None):
        if not key:
            return Settings._licenses
        if type(key) == int:
            try:
                return Settings._licenses[key]
            except IndexError:
                return u'Other::License Not Specified'
        if type(key) == str or type(key) == unicode:
            try:
                return Settings._licenses.index(key)
            except ValueError:
                return Settings._licenses.index(u'Other::License Not Specified')
        else:
            return u'Other::License Not Specified'