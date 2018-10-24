import ocdsmacaw.api
import tempfile
import shutil
import os


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
