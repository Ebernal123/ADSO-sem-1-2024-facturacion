# models/usuario.py
from models import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    rol = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Usuario(nombre={self.nombre}, rol={self.rol})>"
