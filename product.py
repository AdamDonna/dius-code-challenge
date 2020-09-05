class BaseProduct:

    sku = None
    price = None
    name = None

    __subclass_map__ = {}

    @classmethod
    def register_product(cls):
        cls.__subclass_map__[cls.sku] = cls

    def __init_subclass__(cls, **kwargs):
        """Register the class in the list of products we have"""
        super().__init_subclass__(**kwargs)
        cls.register_product()

    @classmethod
    def get_catalog_product(cls, sku):
        """Get the product in the catalog"""
        return cls.__subclass_map__.get(sku)


class SuperIpad(BaseProduct):
    sku = 'ipd'
    price = 549.99
    name = 'Super iPad'


class MacbookPro(BaseProduct):
    sku = 'mbp'
    price = 1399.99
    name = 'MacBook Pro'


class AppleTV(BaseProduct):
    sku = 'atv'
    price = 109.50
    name = 'Apple TV'


class VGAadapter(BaseProduct):
    sku = 'vga'
    price = 30.00
    name = 'VGA adapter'
