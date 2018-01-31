import unittest
from PotterCart import PotterCart

class TestPotterCart(unittest.TestCase):

    def test_buy_1_vol1_0_vol2_0_vol3_0_vol4_0_vol5(self):
        #arrange
        sut = PotterCart()
        order = [1, 0, 0, 0, 0]
        expected = 100
        #act
        actual = sut.get_price(order)
        #assert
        self.assertEqual(actual, expected)

    def test_buy_1_vol1_1_vol2_0_vol3_0_vol4_0_vol5(self):
        #arrange
        sut = PotterCart()
        order = [1, 1, 0, 0, 0]
        expected = 190
        #act
        actual = sut.get_price(order)
        #assert
        self.assertEqual(actual, expected)

    def test_buy_1_vol1_1_vol2_1_vol3_0_vol4_0_vol5(self):
        #arrange
        sut = PotterCart()
        order = [1, 1, 1, 0, 0]
        expected = 270
        #act
        actual = sut.get_price(order)
        #assert
        self.assertEqual(actual, expected)

    def test_buy_1_vol1_1_vol2_1_vol3_1_vol4_0_vol5(self):
        #arrange
        sut = PotterCart()
        order = [1, 1, 1, 1, 0]
        expected = 320
        #act
        actual = sut.get_price(order)
        #assert
        self.assertEqual(actual, expected)

    def test_buy_1_vol1_1_vol2_1_vol3_1_vol4_1_vol5(self):
        #arrange
        sut = PotterCart()
        order = [1, 1, 1, 1, 1]
        expected = 375
        #act
        actual = sut.get_price(order)
        #assert
        self.assertEqual(actual, expected)

    def test_buy_1_vol1_1_vol2_2_vol3_0_vol4_0_vol5(self):
        #arrange
        sut = PotterCart()
        order = [1, 1, 2, 0, 0]
        expected = 370
        #act
        actual = sut.get_price(order)
        #assert
        self.assertEqual(actual, expected)

    def test_buy_1_vol1_2_vol2_2_vol3_0_vol4_0_vol5(self):
        #arrange
        sut = PotterCart()
        order = [1, 2, 2, 0, 0]
        expected = 460
        #act
        actual = sut.get_price(order)
        #assert
        self.assertEqual(actual, expected)

    def test_buy_2_vol1_2_vol2_2_vol3_2_vol4_1_vol5(self):
        #arrange
        sut = PotterCart()
        order = [2, 2, 2, 2, 1]
        expected = 695
        #act
        actual = sut.get_price(order)
        #assert
        self.assertEqual(actual, expected)

    def test_buy_4_vol1_4_vol2_4_vol3_2_vol4_2_vol5(self):
        #arrange
        sut = PotterCart()
        order = [4, 4, 4, 2, 2]
        expected = 1280
        #act
        actual = sut.get_price(order)
        #assert
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPotterCart)
    unittest.TextTestRunner(verbosity=2).run(suite)
