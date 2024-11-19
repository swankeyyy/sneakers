from sqladmin import Admin

from src.models.db_config import db_config
from .models import BrandAdmin, SizeAdmin, ProductAdmin


def create_admin(app):
    """Connect Admin Panel to database and to main_app"""
    admin = Admin(app=app, engine=db_config.get_engine())
    admin.add_view(BrandAdmin)
    admin.add_view(SizeAdmin)
    admin.add_view(ProductAdmin)

    return admin
