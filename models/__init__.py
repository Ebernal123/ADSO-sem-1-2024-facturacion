from flask_sqlalchemy import SQLAlchemy

# Crear la instancia de SQLAlchemy
db = SQLAlchemy()

# Importar los modelos para que se registren correctamente en SQLAlchemy
from models.cliente import Cliente
from models.producto import Producto
from models.factura import Factura, DetalleFactura
from models.usuario import Usuario
