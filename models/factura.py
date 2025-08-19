from datetime import datetime
from models import db  # Importamos la instancia global de SQLAlchemy
from sqlalchemy.ext.hybrid import hybrid_property
from models.usuario import Usuario  # Importamos el modelo Usuario


class Factura(db.Model):
    __tablename__ = 'facturas'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cliente_id = db.Column(db.String(20), db.ForeignKey('clientes.identificacion'), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)  # Nuevo campo usuario
    fecha = db.Column(db.DateTime, default=datetime.utcnow)

    # Relaciones
    cliente = db.relationship('Cliente', backref=db.backref('facturas', lazy=True))
    usuario = db.relationship('Usuario', backref=db.backref('facturas', lazy=True))  # Relación con usuario
    detalles = db.relationship('DetalleFactura', backref='factura', lazy=True, cascade="all, delete-orphan")

    @hybrid_property
    def total(self):
        """Suma de subtotales de los detalles"""
        return sum(d.subtotal for d in self.detalles) if self.detalles else 0.0


class DetalleFactura(db.Model):
    __tablename__ = 'detalle_factura'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    factura_id = db.Column(db.Integer, db.ForeignKey('facturas.id'), nullable=False)
    producto_codigo = db.Column(db.String(20), db.ForeignKey('productos.codigo'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    precio_unitario = db.Column(db.Float, nullable=False)

    # Relaciones
    producto = db.relationship('Producto', backref=db.backref('detalles_factura', lazy=True))

    @hybrid_property
    def subtotal(self):
        """Subtotal calculado (cantidad * precio unitario)"""
        return (self.cantidad or 0) * (self.precio_unitario or 0.0)

