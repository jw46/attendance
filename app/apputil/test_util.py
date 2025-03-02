import unittest
import app.apputil.util as util

class TestUtil(unittest.TestCase):
    def test_string_to_date(self):
        result = util.string_to_date('2024-02-17')
        print(result)

    def test_get_parent_path(self):
        result = util.get_app_path()
        print(result)

    def test_get_today(self):
        result = util.get_today()
        print(result)
        
if __name__ == '__main__':
    unittest.main()
