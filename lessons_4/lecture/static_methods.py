
class Shop:

    total_sales = 0

    def __init__(self, shop_name, sales):
        self.shop_name = shop_name
        self.sales = sales
        self.__class__.total_sales += sales
        # Shop.total_sales += sales

    def make_sales(self, sales):
        self.sales += sales
        self.__class__.total_sales += sales
        # Shop.total_sales += sales

    @staticmethod
    def get_total_sales():
        if Shop.total_sales < 100:
            return 'Прода
class Shop:

    total_sales = 0

    def __init__(self, shop_name, sales):
        self.shop_name = shop_name
        self.sales = sales
        self.__class__.total_sales += sales
        # Shop.total_sales += sales

    def make_sales(self, sales):
        self.sales += sales
        self.__class__.total_sales += sales
        # Shop.total_sales += sales

    @staticmethod
    def get_total_sales():
        if Shop.total_sales < 100:
            return 'Продажи идут плохо', Shop.total_sales
        return 'Продажи идут хорощо', Shop.total_sales

    @classmethod
    def get_total_sales_class_method(cls):
        if cls.total_sales < 100:
            return 'Продажи идут плохо', cls.total_sales
        return 'Продажи идут хорощо', cls.total_sales


print(Shop.get_total_sales_class_method())