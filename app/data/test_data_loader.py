import unittest
import app.data.data_loader as data_loader
import app.apputil.util as util
import app.apputil.config as config

class TestDataLoader(unittest.TestCase):

    def __init__(self, methodName = "runTest"):
        super().__init__(methodName)
        self.gl = data_loader.DataLoader()
        self.data = ['studenci_455-440-FAC-EN-WAE02_g1_2025-02-18.csv', 
                'studenci_455-440-FAC-EN-WAE02_g1_2025-02-17.csv', 
                'studenci_456-440-FAC-EN-WAE02_g1_2025-02-15.csv', 
                'studenci_456-440-FAC-EN-WAE02_g1_2025-02-17.csv']

    def test_get_matching_files(self):
        result = self.gl.get_matching_files('studenci_455-440-FAC-EN-WAE02_g1_', self.data)
        print(result)

    def test_get_latest(self):
        result = self.gl.get_latest(self.data)
        print(result)

    def test_get_one_file_per_group(self):
        result = self.gl.get_one_file_per_group(self.data)
        print(result)

    def test_load_groups(self):
        result = self.gl.load_groups()
        print(result)

    def test_open_df(self):
        group_file_name = 'studenci_440-000-1S-JA5-1_3_g203_2025-02-23.csv'
        result = self.gl.open_df(config.GROUP_FOLDER + group_file_name)
        print(result)

    def test_get_students(self):
        result = self.gl.get_students('studenci_440-000-1S-JA5-1_3_g203_2025-02-23.csv')
        print(result)

if __name__ == '__main__':
    unittest.main()
