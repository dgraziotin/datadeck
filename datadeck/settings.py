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
