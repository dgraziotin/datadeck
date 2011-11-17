__author__ = 'dgraziotin'

class PackageNonValid(Exception):

       def __init__(self, value, missing_fields=None):
           self.parameter = value
           self.missing_fields = missing_fields

       def __str__(self):
           return repr(self.parameter + self.missing_fields)

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
            if not getattr(package, field):
                raise PackageNonValid("Package misses a mandatory field: ", field)

