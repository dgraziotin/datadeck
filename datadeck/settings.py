import dpm.lib

class Settings(object):
    _ckan_section = 'index:ckan'
    _ckan_url_option = 'ckan.url'
    _ckan_api_key_option = 'ckan.api_key'
    _datadeck_section = 'datadeck'
    _datadeck_default_path_option = 'default_path'

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
    def datadeck_default_path(datadeck_default_path=None):
        if not datadeck_default_path:
            return dpm.lib.get_config(Settings._datadeck_section, Settings._datadeck_default_path_option)
        else:
            return dpm.lib.set_config(Settings._datadeck_section, Settings._datadeck_default_path_option,
                                      datadeck_default_path)

    _licenses = {
        u'OSI Approved::Mozilla Public License 1.1 (MPL)': 'mozilla1.1',
        u'OKD Compliant::Creative Commons Attribution-ShareAlike': 'cc-by-sa',
        u'OSI Approved::Nokia Open Source License': 'nokia',
        u'OSI Approved::Computer Associates Trusted Open Source License 1.1': 'ca-tosl1.1',
        u'OKD Compliant::Higher Education Statistics Agency Copyright with data.gov.uk rights': 'hesa-withrights',
        u'OSI Approved::Lucent Public License Version 1.02': 'lucent1.02',
        u'OSI Approved::Open Software License': 'osl-3.0',
        u'OSI Approved::Motosoto License': 'motosoto',
        u'OSI Approved::MIT license': 'mit-license',
        u'OSI Approved::Mozilla Public License 1.0 (MPL)': 'mozilla',
        u'OSI Approved::GNU General Public License v3 (GPLv3)': 'gpl-3.0',
        u'OKD Compliant::UK Click Use PSI': 'ukclickusepsi',
        u'OSI Approved::Eiffel Forum License': 'eiffel',
        u'OSI Approved::Jabber Open Source License': 'jabber-osl',
        u'OSI Approved::Open Group Test Suite License': 'opengroup',
        u'OSI Approved::Entessa Public License': 'entessa',
        u'OKD Compliant::Other': 'other-open',
        u'OSI Approved::EU DataGrid Software License': 'eudatagrid',
        u'OSI Approved::Zope Public License': 'zpl',
        u'OSI Approved::Naumen Public License': 'naumen',
        u'OSI Approved::wxWindows Library License': 'wxwindows',
        u'OKD Compliant::GNU Free Documentation License (GFDL)': 'gfdl',
        u'Non-OKD Compliant::Non-Commercial Other': 'other-nc',
        u'OKD Compliant::Open Data Commons Public Domain Dedication and License (PDDL)': 'odc-pddl',
        u'OSI Approved::NASA Open Source Agreement 1.3': 'nasa1.3',
        u'OSI Approved::X.Net License': 'xnet',
        u'OSI Approved::W3C License': 'W3C',
        u'OSI Approved::Academic Free License': 'afl-3.0',
        u'Non-OKD Compliant::Crown Copyright': 'ukcrown',
        u'OSI Approved::RealNetworks Public Source License V1.0': 'real',
        u'OSI Approved::Common Development and Distribution License': 'cddl1',
        u'OSI Approved::Intel Open Source License': 'intel-osl',
        u'OSI Approved::GNU General Public License (GPL)': 'gpl-2.0',
        u'Non-OKD Compliant::Creative Commons Non-Commercial (Any)': 'cc-nc',
        u'Non-OKD Compliant::Other': 'other-closed',
        u'Other::License Not Specified': 'notspecified',
        u'OSI Approved::Sybase Open Watcom Public License 1.0': 'sybase',
        u'OSI Approved::Educational Community License': 'ecl2',
        u'OSI Approved::Sun Industry Standards Source License (SISSL)': 'sun-issl',
        u'OKD Compliant::Other (Public Domain)': 'other-pd',
        u'OKD Compliant::Public Domain': 'other-pd',
        u'OKD Compliant::Creative Commons Attribution': 'cc-by',
        u'OSI Approved::OCLC Research Public License 2.0': 'oclc2',
        u'OSI Approved::Artistic license': 'artistic-license-2.0',
        u'OKD Compliant::Other (Attribution)': 'other-at',
        u'OSI Approved::Sleepycat License': 'sleepycat',
        u'OSI Approved::PHP License': 'php',
        u'OKD Compliant::Creative Commons CCZero': 'cc-zero',
        u'OSI Approved::University of Illinois/NCSA Open Source License': 'UoI-NCSA',
        u'OSI Approved::Adaptive Public License': 'apl1.0',
        u'OSI Approved::Ricoh Source Code Public License': 'ricohpl',
        u'OSI Approved::Eiffel Forum License V2.0': 'ver2_eiffel',
        u'OSI Approved::Python license (CNRI Python License)': 'pythonpl',
        u'OSI Approved::Frameworx License': 'frameworx',
        u'OSI Approved::IBM Public License': 'ibmpl',
        u'OSI Approved::Fair License': 'fair',
        u'OSI Approved::Lucent Public License (Plan9)': 'lucent-plan9',
        u'OSI Approved::Nethack General Public License': 'nethack',
        u'OSI Approved::Common Public License 1.0': 'cpal_1.0',
        u'OSI Approved::Attribution Assurance Licenses': 'attribution',
        u'OSI Approved::Reciprocal Public License': 'rpl1.5',
        u'OSI Approved::Eclipse Public License': 'eclipse-1.0',
        u'OSI Approved::CUA Office Public License Version 1.0': 'cuaoffice',
        u'OSI Approved::Vovida Software License v. 1.0': 'vovidapl',
        u'OSI Approved::Apple Public Source License': 'apsl-2.0',
        u'OKD Compliant::UK Crown Copyright with data.gov.uk rights': 'ukcrown-withrights',
        u'OKD Compliant::Local Authority Copyright with data.gov.uk rights': 'localauth-withrights',
        u'OKD Compliant::Open Data Commons Open Database License (ODbL)': 'odc-odbl',
        u'OSI Approved::New BSD license': 'bsd-license',
        u'OSI Approved::Qt Public License (QPL)': 'qtpl',
        u'OSI Approved::GNU Library or "Lesser" General Public License (LGPL)': 'lgpl-2.1',
        u'OSI Approved::MITRE Collaborative Virtual Workspace License (CVW License)': 'mitre',
        u'OSI Approved::Apache License, 2.0': 'apache2.0',
        u'OSI Approved::Apache Software License': 'apache',
        u'OSI Approved::Python Software Foundation License': 'PythonSoftFoundation',
        u'OSI Approved::Sun Public License': 'sunpublic',
        u'OSI Approved::zlib/libpng license': 'zlib-license'
    }

    @staticmethod
    def licenses(license=None):
        if not license:
            return Settings._licenses
        else:
            try:
                return Settings._licenses[license]
            except KeyError:
                return license