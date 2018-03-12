"""
CREATE: 2018/2/3
AUTHOR: Hehahutu
"""
from framework.mongo_object import DBS


class PageDataType:
    def __init__(self):
        self.db = DBS

    @classmethod
    def serializer(cls, data):
        da_list = []
        for da in data:
            if da.get('is_run'):
                da.pop('_id')
                da_list.append([da])
        return da_list

    def login_page(self):
        """
        data:
        {'username': 'zqq',
        'password': '666666',
        'assert_type': 'in',
        'assert_data': 'aaa'
        'title': 'title'
        'is_run': bool
        }

        :return:
        """
        data = self.db.login_page.find()
        return self.serializer(data)


# if __name__ == '__main__':
#     print(PageDataType().login_page())
