import functools
import logging

logger = logging.getLogger(__name__)


class CoveInputDataError(Exception):
    """
    An error that we think is due to the data input by the user, rather than a
    bug in the application.
    """
    pass


class UnrecognisedFileType(CoveInputDataError):
    pass


class UnrecognisedFileTypeXML(CoveInputDataError):
    pass

class CantConvertSpreadSheet(CoveInputDataError):
    pass

def cove_spreadsheet_conversion_error(func):
    @functools.wraps(func)
    def wrapper(request, *args, **kwargs):
        try:
            return func(request, *args, **kwargs)
        except Exception as err:
            logger.exception(err, extra={
                'request': request,
                })
            raise CantConvertSpreadSheet(format(repr(err)))
    return wrapper
