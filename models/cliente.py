
from models import db

class Cliente(db.Model):
    __tablename__ = 'clientes'

    identificacion = db.Column(db.String(20), primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20), nullable=True)

    def __repr__(self):
        return f'<Cliente {self.identificacion} - {self.nombre}>'
