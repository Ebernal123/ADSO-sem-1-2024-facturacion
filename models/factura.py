from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from models import db  # Importamos la instancia global de SQLAlchemy


class Factura(db.Model):
    __tablename__ = 'facturas'

    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.String(20), db.ForeignKey('clientes.identificacion'))
    fecha = db.Column(db.DateTime, default=datetime.utcnow)

    # Relaciones
    cliente = db.relationship('Cliente', backref=db.backref('facturas', lazy=True))
    detalles = db.relationship('DetalleFactura', backref='factura', lazy=True, cascade="all, delete-orphan")


class DetalleFactura(db.Model):
    __tablename__ = 'detalle_factura'

    id = db.Column(db.Integer, primary_key=True)
    factura_id = db.Column(db.Integer, db.ForeignKey('facturas.id'), nullable=False)
    producto_codigo = db.Column(db.String(20), db.ForeignKey('productos.codigo'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    precio_unitario = db.Column(db.Float, nullable=False)

    # Relaciones
    producto = db.relationship('Producto', backref=db.backref('detalles_factura', lazy=True))

