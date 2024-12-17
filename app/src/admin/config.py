from sqladmin import Admin

from src.models.db_config import db_config
from .models import BrandAdmin, SizeAdmin, ProductAdmin, UserAdmin, OrderAdmin

list_views = [BrandAdmin, SizeAdmin, ProductAdmin, UserAdmin, OrderAdmin]


def create_admin(app):
    """Connect Admin Panel to database and to main_app"""
    admin = Admin(app=app, engine=db_config.get_engine())
    for view in list_views:
        admin.add_view(view)
    return admin
