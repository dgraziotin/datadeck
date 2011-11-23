"""
Tools for handling validation of Packages
"""
__author__ = 'dgraziotin'
import dpm
import dpm.lib
import os

class PackageNonValid(Exception):
    def __init__(self, message, missing_fields=None):
        Exception.__init__(self, message)
        self.missing_fields = missing_fields

    def __str__(self):
        return repr(self.message + self.missing_fields)


class PackageValidator(object):
    """
    Validates a Package to be submitted to CKAN
    """
    MANDATORY_FIELDS = (
        'name',
        'title'
    )

    @classmethod
    def validate(cls, package):
        for field in PackageValidator.MANDATORY_FIELDS:
            attribute = getattr(package, field, None)
            if not attribute:
                raise PackageNonValid("Package misses a mandatory field: ", field)
        return True

    @classmethod
    def already_existing(cls, path, package_name):
        try:
            dpm.lib.load(os.path.join(path, package_name))
        except dpm.DatapkgException:
            return False
        return True