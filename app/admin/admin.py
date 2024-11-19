from sqladmin import Admin, ModelView


from src.models.product import Brand

from main import main_app
from src.models.db_config import db_config

admin = Admin(main_app, db_config.get_engine())


class BrandAdmin(ModelView, model=Brand):
    column_list = [Brand.id, Brand.name]


admin.add_view(BrandAdmin)
