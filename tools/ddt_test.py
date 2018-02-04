"""
CREATE: 2018/2/3
AUTHOR: Hehahutu
"""
import unittest
from ddt import ddt, data, unpack
from tools.assert_parser.as_paser import AsParser


@ddt
class FooTestCase(unittest.TestCase):

    @data(3, 4, 12, 23)
    def test_larger_than_two(self, value):
        self.assertTrue(value)

    @data(*[[{'a': 'a'}], [{'a': 'a'}]])
    @unpack
    def test_list_extracted_into_arguments(self, data):
        print(data['a'])
        AsParser.parser_data('in', 'i', 'i love you')


if __name__ == '__main__':
    FooTestCase().run()
