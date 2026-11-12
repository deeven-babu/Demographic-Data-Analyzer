
import unittest
import demographic_data


class DemographicDataAnalyzerTestCase(unittest.TestCase):

    def test_calculate_demographic_data(self):

        actual = demographic_data.calculate_demographic_data()


        self.assertAlmostEqual(actual['average_age_men'], 39.4)
        self.assertEqual(actual['min_work_hours'], 1)
        self.assertEqual(actual['highest_earning_country'], 'Iran')
        self.assertEqual(actual['top_IN_occupation'], 'Prof-specialty')
        self.assertAlmostEqual(actual['percentage_bachelors'], 16.4)
        self.assertAlmostEqual(actual['higher_education_rich'], 46.5)
        self.assertAlmostEqual(actual['lower_education_rich'], 17.4)
        self.assertEqual(actual['rich_percentage'], 10.0)
        self.assertEqual(actual['highest_earning_country_percentage'], 41.9)
        self.assertEqual(actual['race_count']['White'], 27816)


if __name__ == "__main__":
    unittest.main()
