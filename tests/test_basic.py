import ocdsmacaw.api
import tempfile
import shutil


def test_basic_1():
    package = {}

    cove_temp_folder = tempfile.mkdtemp(prefix='ocdsmacaw-tests-', dir=tempfile.gettempdir())
    try:
        result = ocdsmacaw.api.ocds_json_output(cove_temp_folder, None, None, convert=False, cache_schema=True,
                                                file_type='json', json_data=package)
    finally:
        shutil.rmtree(cove_temp_folder)

    assert result['cats'] == 'are great'
