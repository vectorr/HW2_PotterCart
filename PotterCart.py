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
