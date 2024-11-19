from sqladmin import Admin

from src.models.db_config import db_config
from .models import BrandAdmin, SizeAdmin





def create_admin ( app ):

    admin = Admin(app=app, engine=db_config.get_engine())
    admin.add_view(BrandAdmin)
    admin.add_view(SizeAdmin)

    return admin

