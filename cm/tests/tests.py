import unittest
from werkzeug.exceptions import NotFound
from app import create_app
import os.path
from shutil import copyfile
from .test_client import TestClient
UPLOAD_DIRECTORY = '/var/hotmaps/cm_files_uploaded'

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)
    os.chmod(UPLOAD_DIRECTORY, 0o777)


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = create_app(os.environ.get('FLASK_CONFIG', 'development'))
        self.ctx = self.app.app_context()
        self.ctx.push()
        self.client = TestClient(self.app,)

    def tearDown(self):
        self.ctx.pop()
    def test_compute(self):
        raster_file_path = 'tests/data/cleaned_data.csv'
        # simulate copy from HTAPI to CM
        save_path = UPLOAD_DIRECTORY + "/cleaned_data.csv"
        copyfile(raster_file_path, save_path)
        # provide input parameters
        inputs_raster_selection = {}
        inputs_parameter_selection = {
            "field_of_intervention": "All",
            "intervention_type": "All",
            "building_type": "Non-residential"

        }
        # register the calculation module a
        payload = {"inputs_parameter_selection": inputs_parameter_selection}

        rv, json = self.client.post('computation-module/compute/', data=payload)

        self.assertTrue(rv.status_code == 200)
