import unittest
import scaleconverter


class Test_ScaleConverter(unittest.TestCase):
    def test_convert_meters_to_scale_returns_6dot6_for_1(self):
        self.assertTrue(scaleconverter.convert_meter_to_scale(1, 2), 6.6)

    def test_convert_feet_to_scale_returns_2_for_1(self):
        self.assertTrue(scaleconverter.convert_feet_to_scale(1, 2), 2)

    def test_convert_feet_to_scale_returns_1_for_1_over_2(self):
        self.assertTrue(scaleconverter.convert_feet_to_scale("1/2", 2), 1)

    def test_convert_feet_to_scale_returns_1_for_0_space_12(self):
        self.assertTrue(scaleconverter.convert_feet_to_scale("0 12", 2), 1)

    def test_convert_feet_to_scale_returns_1_for_0_space_0_space_12_ove_1(self):
        self.assertTrue(scaleconverter.convert_feet_to_scale("0 0 12/1", 2), 1)


if __name__ == '__main__':
    unittest.main()
