from marshmallow import fields, Schema
import datetime
from . import db
from .CompanyModel import CompanySchema

class Usermodel(db.Model):
    """
    User Model
    """

    #table name
    __tablename__ = 'users'

    id = db.Column(db.integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    tipoDocumento = db.Column(db.integer, nullable=True)
    documento = db.Column(db.String(20), nullable=True)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)
    company = db.relationship('CompanyModel', backref='users', lazy=True) # add this new line

    def __init__(self, data):
        """
        Class constructor
        """
        self.name = data.get('name')
        self.email = data.get('email')
        self.tipoDocumento = data.get('tipoDocumento')
        self.documento = data.get('documento')
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    @staticmethod
    def get_all_users():
        return UserModel.query.all()

    @staticmethod
    def get_one_user(id):
        return UserModel.query.get(id)

    def __repr__(self):
        return '<id {}>'.format(self.id)

class UserSchema(Schema):
    """
    User Schema
    """

    id = fields.Int(dump_only=True)
    name = fields.Str(dump_only=True)
    email = fields.Str(dump_only=True)
    tipoDocumento = fields.Int(dump_only=True)
    documento = fields.Str(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)
    company = fields.Nested(CompanySchema, many=True)