import unittest 
import pandas as p
from library_pipeline_copy import calculate_days_between,clean_customers,metrics,clean_checkouts


class TestOperations(unittest.TestCase):
    def setUp(self):
        self.data = [('2026-01-01','2026-01-11',10),('2026-01-01','2026-01-01',0)]
    def test_days_between(self):
        for a,b,c in self.data:
            start_dt = p.to_datetime(p.Series([a]))
            end_dt = p.to_datetime(p.Series([b]))
            result = calculate_days_between(start_dt,end_dt)
            actual_days = result.iloc[0]
            self.assertEqual(actual_days,c,f"Failed for {a} and {b}")

    def test_clean_customers(self):
        dummy_data = p.DataFrame({
            'Customer ID': [101.0, 102, None, '104'],
            'Customer Name': ['   John Smith ','John Smith','Test Name','  Batman   ']
        })
        expected_data = p.DataFrame({
            'Customer ID': [101, 102, 104],
            'Customer Name': ['John Smith','John Smith','Batman']
        })

        df = clean_customers(dummy_data)

        p.testing.assert_frame_equal(df.reset_index(drop=True),expected_data.reset_index(drop=True))

    def test_metrics(self):
        test_data = [("test1",1,0,1),("test2",100,90,10)]

        for name,ini,fin,expected in test_data:
            result = metrics(name,ini,fin)
            self.assertEqual(result,expected,f"failed for {name}")

    def test_clean_checkouts(self):
        dummy_data = p.DataFrame({
            'Id': [1.0,None,3.0],
            'Books': ['Book A','Book B', 'Book C'],
            'Customer ID': [101,102,103],
            'Book checkout': ["'01/01/2026","01/01/2026","01/01/2027"],
            'Book Returned': ["'10/01/2026","15/01/2026","01/02/2027"],
            'Days allowed to borrow': ['2 weeks','2 weeks','2 weeks']
        })

        expected_data = p.DataFrame({
            'Id': [1],
            'Books': ['Book A'],
            'Customer ID': [101],
            'Book checkout': ['01/01/2026'],
            'Book Returned': ['10/01/2026'],
            'Days allowed to borrow': ['2 weeks'],
            'Days Allowed': [14],
            'Actual Days Checked Out': [9],
            'Exceeded Allowed Days': [False]
        })

        df = clean_checkouts(dummy_data.reset_index(drop=True))
        expected_df = expected_data.reset_index(drop=True)

        df = df[expected_df.columns]

        p.testing.assert_frame_equal(df,expected_df)

if __name__ == "__main__":
    unittest.main()

    
