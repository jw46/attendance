import unittest
from app.controllers.student_chooser_c import StudentChooserControler
from app.models.table_df_m import TableDfModel

class TestDataLoader(unittest.TestCase):

    def __init__(self, methodName = "runTest"):
        super().__init__(methodName)
        self.c = StudentChooserControler()

if __name__ == '__main__':
    unittest.main()