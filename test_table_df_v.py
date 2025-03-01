import unittest
from app.views.table_df_v import TableDfView
from app.models.table_df_m import TableDfModel

class TestDataLoader(unittest.TestCase):

    def __init__(self, methodName = "runTest"):
        super().__init__(methodName)
        self.model = TableDfModel('att/studenci_440-000-1S-JA-3_3_g304_2025-02-28.csv')
        self.tdv = TableDfView(self.model)

    def test_get_column_x_widths(self):
        result = self.tdv.get_column_x_widths()
        print(result)

if __name__ == '__main__':
    unittest.main()