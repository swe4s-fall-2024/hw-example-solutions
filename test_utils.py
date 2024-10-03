import unittest
from utils import *
'''
Test Variables: 
    --file_path 'Agrofood_co2_emission.csv'
    --country 'United States of America'
    --country_column 0
    --emissions_column 2
'''
rows = get_rows_by_column_value(file_path='Agrofood_co2_emission.csv', column_value='United States of America', column_index=0)
data_points = get_data_points(rows,2)

class testUtils(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(find_sum(data_points),43152.3581,msg="Sum Function Failed")

    def test_mean(self):
        self.assertEqual(find_mean(data_points),1392.0115516129033,msg="Mean Function Failed")

    def test_standard_dev(self):
        self.assertEqual(find_standard_dev(data_points),428.64534364222743,msg="Standard Deviation Function Failed")

    def test_median(self):
        self.assertEqual(find_median(data_points),1391.1481,msg="Median Function Failed")


if __name__ == '__main__':
    unittest.main()