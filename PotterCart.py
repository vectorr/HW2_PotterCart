import traceback

class PotterCart:
    discount_for_bundle = [1, 0.95, 0.9, 0.8, 0.75]
    book_unit_price = 100

    def _special_calculate_for_bundle_3_plus_5(self, bundle_quantity):
        price = 0
        # special case for 3 different books bundle plus 5 different books bundle
        # is more expensive than couple 4 different books bundle.
        if bundle_quantity[2] > 0 and bundle_quantity[4] > 0:
            num_of_special_3_plug_5_bundles = min(bundle_quantity[2],\
                                                    bundle_quantity[4])
            # change 3+5 bundle to 2*4 bundle
            price = 2*4*PotterCart.book_unit_price*\
                    PotterCart.discount_for_bundle[3]*\
                    num_of_special_3_plug_5_bundles

            bundle_quantity[2] -= num_of_special_3_plug_5_bundles
            bundle_quantity[4] -= num_of_special_3_plug_5_bundles

        return price

    def get_price(self, order):

        def calculate_bundle_quantity(order, bundle_quantity):
            if not order:
                return
            else:
                bundle_quantity[len(order)-1] += 1
                return calculate_bundle_quantity([i-1 for i in order if i-1 > 0],\
                                                    bundle_quantity)

        bundle_quantity = [0]*len(order)
        calculate_bundle_quantity([i for i in order if i > 0], bundle_quantity)

        price = self._special_calculate_for_bundle_3_plus_5(bundle_quantity)

        for idx, val in enumerate(bundle_quantity):
            price += (idx+1)*PotterCart.book_unit_price*\
                        PotterCart.discount_for_bundle[idx]*val

        return int(price)

class PotterCartTest:

    def Assert(self, expected, actual):
        try:
            assert expected == actual
        except Exception as e:
            print 'expected({0}) != actual({1})'.format(expected, actual)
            raise

    def test_buy_1_vol1_0_vol2_0_vol3_0_vol4_0_vol5(self):
        #arrange
        sut = PotterCart()
        order = [1, 0, 0, 0, 0]
        expected = 100
        #act
        actual = sut.get_price(order)
        #assert
        self.Assert(expected, actual)

    def test_buy_1_vol1_1_vol2_0_vol3_0_vol4_0_vol5(self):
        #arrange
        sut = PotterCart()
        order = [1, 1, 0, 0, 0]
        expected = 190
        #act
        actual = sut.get_price(order)
        #assert
        self.Assert(expected, actual)

    def test_buy_1_vol1_1_vol2_1_vol3_0_vol4_0_vol5(self):
        #arrange
        sut = PotterCart()
        order = [1, 1, 1, 0, 0]
        expected = 270
        #act
        actual = sut.get_price(order)
        #assert
        self.Assert(expected, actual)

    def test_buy_1_vol1_1_vol2_1_vol3_1_vol4_0_vol5(self):
        #arrange
        sut = PotterCart()
        order = [1, 1, 1, 1, 0]
        expected = 320
        #act
        actual = sut.get_price(order)
        #assert
        self.Assert(expected, actual)

    def test_buy_1_vol1_1_vol2_1_vol3_1_vol4_1_vol5(self):
        #arrange
        sut = PotterCart()
        order = [1, 1, 1, 1, 1]
        expected = 375
        #act
        actual = sut.get_price(order)
        #assert
        self.Assert(expected, actual)

    def test_buy_1_vol1_1_vol2_2_vol3_0_vol4_0_vol5(self):
        #arrange
        sut = PotterCart()
        order = [1, 1, 2, 0, 0]
        expected = 370
        #act
        actual = sut.get_price(order)
        #assert
        self.Assert(expected, actual)

    def test_buy_1_vol1_2_vol2_2_vol3_0_vol4_0_vol5(self):
        #arrange
        sut = PotterCart()
        order = [1, 2, 2, 0, 0]
        expected = 460
        #act
        actual = sut.get_price(order)
        #assert
        self.Assert(expected, actual)

    def test_buy_2_vol1_2_vol2_2_vol3_2_vol4_1_vol5(self):
        #arrange
        sut = PotterCart()
        order = [2, 2, 2, 2, 1]
        expected = 695
        #act
        actual = sut.get_price(order)
        #assert
        self.Assert(expected, actual)

    def test_buy_4_vol1_4_vol2_4_vol3_2_vol4_2_vol5(self):
        #arrange
        sut = PotterCart()
        order = [4, 4, 4, 2, 2]
        expected = 1280
        #act
        actual = sut.get_price(order)
        #assert
        self.Assert(expected, actual)

if __name__ == "__main__":
    test = PotterCartTest()
    try:
        test.test_buy_1_vol1_0_vol2_0_vol3_0_vol4_0_vol5()
    except Exception as e:
        traceback.print_exc()
    else:
        print 'test_buy_1_vol1_0_vol2_0_vol3_0_vol4_0_vol5 ok'

    try:
        test.test_buy_1_vol1_1_vol2_0_vol3_0_vol4_0_vol5()
    except Exception as e:
        traceback.print_exc()
    else:
        print 'test_buy_1_vol1_1_vol2_0_vol3_0_vol4_0_vol5 ok'

    try:
        test.test_buy_1_vol1_1_vol2_1_vol3_0_vol4_0_vol5()
    except Exception as e:
        traceback.print_exc()
    else:
        print 'test_buy_1_vol1_1_vol2_1_vol3_0_vol4_0_vol5 ok'

    try:
        test.test_buy_1_vol1_1_vol2_1_vol3_1_vol4_0_vol5()
    except Exception as e:
        traceback.print_exc()
    else:
        print 'test_buy_1_vol1_1_vol2_1_vol3_1_vol4_0_vol5 ok'

    try:
        test.test_buy_1_vol1_1_vol2_1_vol3_1_vol4_1_vol5()
    except Exception as e:
        traceback.print_exc()
    else:
        print 'test_buy_1_vol1_1_vol2_1_vol3_1_vol4_1_vol5 ok'

    try:
        test.test_buy_1_vol1_1_vol2_2_vol3_0_vol4_0_vol5()
    except Exception as e:
        traceback.print_exc()
    else:
        print 'test_buy_1_vol1_1_vol2_2_vol3_0_vol4_0_vol5 ok'

    try:
        test.test_buy_1_vol1_2_vol2_2_vol3_0_vol4_0_vol5()
    except Exception as e:
        traceback.print_exc()
    else:
        print 'test_buy_1_vol1_2_vol2_2_vol3_0_vol4_0_vol5 ok'

    try:
        test.test_buy_2_vol1_2_vol2_2_vol3_2_vol4_1_vol5()
    except Exception as e:
        traceback.print_exc()
    else:
        print 'test_buy_2_vol1_2_vol2_2_vol3_2_vol4_1_vol5 ok'

    try:
        test.test_buy_4_vol1_4_vol2_4_vol3_2_vol4_2_vol5()
    except Exception as e:
        traceback.print_exc()
    else:
        print 'test_buy_4_vol1_4_vol2_4_vol3_2_vol4_2_vol5 ok'
