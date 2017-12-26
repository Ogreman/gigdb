from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.dialects.postgresql.json import JSONB

from gigdb.models import db


class Band(db.Model):
    __tablename__ = 'band'

    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    country = db.Column(db.Text)
    name = db.Column(db.Text)
    town_city = db.Column(db.Text)

    ffo = db.Column(JSONB)
    tags = db.Column(JSONB)
    links = db.Column(JSONB)

    contact_email = db.Column(db.Text)
    contact_name = db.Column(db.Text)
    num_members = db.Column(db.Integer)

    dates = db.Column(JSONB)
    fee = db.Column(db.Integer)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
