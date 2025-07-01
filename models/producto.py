from models.cliente import db  # Usamos la instancia existente de db

class Producto(db.Model):
    __tablename__ = 'productos'

    codigo = db.Column(db.String(10), primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(200))
    precio = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Producto {self.codigo} - {self.nombre}>'
