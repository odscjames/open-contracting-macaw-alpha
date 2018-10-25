
from ocdsmacaw.common.exceptions import CoveInputDataError

class UnrecognisedVersionOfTheSchema(CoveInputDataError):
    pass

def raise_invalid_version_argument(version):
    raise UnrecognisedVersionOfTheSchema('{} is not a valid schema version'.format(version))
