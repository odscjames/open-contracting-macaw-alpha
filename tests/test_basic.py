import ocdsmacaw.api
import tempfile
import shutil
import os
import pytest


def test_basic_1():
    filename = os.path.join(os.path.dirname(
        os.path.realpath(__file__)), 'fixtures', 'basic', '1.json'
    )

    cove_temp_folder = tempfile.mkdtemp(prefix='ocdsmacaw-tests-', dir=tempfile.gettempdir())
    try:
        result = ocdsmacaw.api.ocds_json_output(cove_temp_folder, filename, None, convert=False, cache_schema=True,
                                                file_type='json')
    finally:
        shutil.rmtree(cove_temp_folder)

    assert result['file_type'] == 'json'


def test_error_wrong_file_type():
    filename = os.path.join(os.path.dirname(
        os.path.realpath(__file__)), 'fixtures', 'basic', 'test.txt'
    )

    cove_temp_folder = tempfile.mkdtemp(prefix='ocdsmacaw-tests-', dir=tempfile.gettempdir())
    try:
        with pytest.raises(ocdsmacaw.api.APIException):
            ocdsmacaw.api.ocds_json_output(cove_temp_folder, filename, None, convert=False, cache_schema=True,
                                                    file_type='json')
    finally:
        shutil.rmtree(cove_temp_folder)

def test_error_bad_version():
    filename = os.path.join(os.path.dirname(
        os.path.realpath(__file__)), 'fixtures', 'basic', 'bad_version.json'
    )

    cove_temp_folder = tempfile.mkdtemp(prefix='ocdsmacaw-tests-', dir=tempfile.gettempdir())
    try:
        with pytest.raises(ocdsmacaw.api.APIException):
            ocdsmacaw.api.ocds_json_output(cove_temp_folder, filename, None, convert=False, cache_schema=True,
                                                    file_type='json')
    finally:
        shutil.rmtree(cove_temp_folder)

def test_error_bad_json():
    filename = os.path.join(os.path.dirname(
        os.path.realpath(__file__)), 'fixtures', 'basic', 'bad_json.json'
    )

    cove_temp_folder = tempfile.mkdtemp(prefix='ocdsmacaw-tests-', dir=tempfile.gettempdir())
    try:
        with pytest.raises(ocdsmacaw.api.APIException):
            ocdsmacaw.api.ocds_json_output(cove_temp_folder, filename, None, convert=False, cache_schema=True,
                                                    file_type='json')
    finally:
        shutil.rmtree(cove_temp_folder)
