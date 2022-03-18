from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field

from db.models import Advert


class AdvertSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Advert

    id = auto_field(dump_only=True)
    created_at = auto_field(dump_only=True)
