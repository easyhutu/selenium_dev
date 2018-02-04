"""
CREATE: 2018/2/4
AUTHOR: Hehahutu
"""
import unittest

test_case = unittest.TestCase()
asType = {
    # 判断a是否在b
    'in': test_case.assertIn,
    'notIn': test_case.assertNotIn,

    # 判断是否是真
    'true': test_case.assertTrue,
    'false': test_case.assertFalse,

    # 判断两个对象是否一样
    'is': test_case.assertIs,
    'isNot': test_case.assertIsNot,

    # 判断是否等于
    'equal': test_case.assertEqual,
    'notEqual': test_case.assertNotEqual,

    # a < b
    'less': test_case.assertLess,
    # a <= b
    'lessEqual': test_case.assertLessEqual,
    # a > b
    'greater': test_case.assertGreater,
    # a >= b
    'greaterEqual': test_case.assertLessEqual,

}


class AsParser:
    @staticmethod
    def parser_data(as_type: str = 'in or true and so on', *args):
        return asType[as_type](*args)

    @staticmethod
    def show_all_assert_type():
        all_type = [key for key in asType.keys()]
        print(all_type)
        return all_type


# if __name__ == '__main__':
#     AsParser.show_all_assert_type()
