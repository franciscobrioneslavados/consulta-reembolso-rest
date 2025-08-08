from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Boleta(db.Model):
    __tablename__ = 'boletas'

    id_ = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_boleta = db.Column(db.Integer, nullable=False)
    key_boleta = db.Column(db.String(255), nullable=False)
    procesa_isapre = db.Column(db.Boolean, default=False)
    response_isapre = db.Column(db.JSON)
    key_response_isapre = db.Column(db.String(255))
    procesa_seguro = db.Column(db.Boolean, default=False)
    response_seguro = db.Column(db.JSON)
    key_response_seguro = db.Column(db.String(255))
    half = db.Column(db.Float)