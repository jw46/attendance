import pandas as pd
import unittest
import app.data.data_saver as data_saver
import app.apputil.util as util

class TestdataSaver(unittest.TestCase):

    def __init__(self, methodName = "runTest"):
        super().__init__(methodName)
        self.gs = data_saver.DataSaver()

    def test_filename_to_today(self):
        result = self.gs.filename_to_today('studenci_455-440-FAC-EN-WAE02_g1_2025-02-18.csv')
        print(result)

    def test_save(self):
        df = pd.read_csv(util.get_parent_path() + '/groups/studenci_455-440-FAC-EN-WAE02_g1_2025-02-18.csv', sep=';')
        result = self.gs.save(df, 'studenci_555-440-FAC-EN-WAE02_g1_2025-02-18.csv')

if __name__ == '__main__':
    unittest.main()
