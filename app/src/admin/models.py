from sqladmin import ModelView

from src.models import Brand, Size


class BrandAdmin(ModelView, model=Brand):
    name = 'Бренд'
    name_plural = 'Бренды'
    page_size = 50

    column_list = [Brand.name]
    column_details_list = [Brand.id, Brand.name]


class SizeAdmin(ModelView, model=Size):
    name = 'Размер'
    name_plural = 'Размеры'
    page_size = 50

    column_list = [Size.size]
    column_details_list = [Brand.id, Size.size]