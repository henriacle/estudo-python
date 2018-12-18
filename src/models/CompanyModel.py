from . import db
import datetime
from marshmallow import fields, Schema


class CompanyModel(db.Model):
    """
    Empresa do cabeleleiro
    """

    __tablename__ = 'companies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    descricao = db.Column(db.String(255), nullable=True)
    endereco = db.Column(db.String(100), nullable=True)
    tipoDocumento = db.Column(db.integer, nullable=True)
    documento = db.Column(db.String(20), nullable=True)    
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, data):
        self.title = data.get('title')
        self.descricao = data.get('descricao')
        self.endereco = data.get('endereco')
        self.tipoDocumento = data.get('tipoDocumento')
        self.documento = data.get('documento')
        self.owner_id = data.get('owner_id')
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key,item in data.items():
            setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_companies():
        return CompanyModel.query.all()

    @staticmethod
    def get_one_company(id):
        return CompanyModel.query.get(id)

    def __repr__(self):
        return '<id {}>'.format(self.id)

class CompanySchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(dump_only=True)
    descricao = fields.Str(dump_only=True)
    endereco = fields.Str(dump_only=True)
    tipoDocumento = fields.Int(dump_only=True)
    documento = fields.Str(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)
