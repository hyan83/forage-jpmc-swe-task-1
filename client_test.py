import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    # Added reusable datapoint calculate assertion equal test function
    def datapoint_calculate_assertion_equal(self, q_list):
        for quote in q_list:
            self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                                                   (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

    # Added reusable ratio calculate assertion equal test function
    def ratio_calculate_assertion_equal(self, q_list, stock_a, stock_b):
        prices = dict()
        for quote in q_list:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price
        self.assertEqual(getRatio(price_a=prices[stock_a], price_b=prices[stock_b]),
                         round(float(((q_list[0]['top_bid']['price'] + q_list[0]['top_ask']['price']) / 2) /
                                     ((q_list[1]['top_bid']['price'] + q_list[1]['top_ask']['price']) / 2)), 6))
        # Below is a test where the function getRation has a different result which will give error and fail the test.
        # self.assertEqual(getRatio(price_a=prices[stock_a], price_b=prices[stock_b]),
        #                  float(((q_list[0]['top_bid']['price'] + q_list[0]['top_ask']['price']) / 2) /
        #                        ((q_list[1]['top_bid']['price'] + q_list[1]['top_ask']['price']) / 2)))

    def test_getDataPoint_calculatePrice(self):
        quotes = [
          {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
          {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        self.datapoint_calculate_assertion_equal(q_list=quotes)

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
          {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
          {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        self.datapoint_calculate_assertion_equal(q_list=quotes)

    # Added testing for getRatio with dataset
    def test_getRatio_calculatePrice(self):
        quotes = [
          {'top_ask': {'price': 131.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 130.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'GHI'},
          {'top_ask': {'price': 131.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 127.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'JKL'}
        ]

        # This following data set below is used to test division zero which will fail and give error
        # quotes = [
        #   {'top_ask': {'price': 131.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 130.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'GHI'},
        #   {'top_ask': {'price': 0, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 81}, 'id': '0.109974697771', 'stock': 'JKL'}
        # ]
        self.ratio_calculate_assertion_equal(q_list=quotes, stock_a="GHI", stock_b="JKL")

    # Added testing for getRatio with dataset for price bid greater than ask
    def test_getRatio_calculatePriceBidGreaterThanAsk(self):
        quotes = [
          {'top_ask': {'price': 129.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 130.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'GHI'},
          {'top_ask': {'price': 131.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 127.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'JKL'}
        ]
        self.ratio_calculate_assertion_equal(q_list=quotes, stock_a="GHI", stock_b="JKL")


if __name__ == '__main__':
    unittest.main()
