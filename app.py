from flask import Flask, render_template
from models.cliente import db
from controllers.cliente_controller import cliente_bp
from controllers.usuario_controller import usuario_bp  # Solo si ya tienes este controlador
from controllers.producto_controller import producto_bp
from controllers.factura_controller import factura_bp

app = Flask(__name__)
app.secret_key = "Jony123456789*"

# Configuración de la conexión a la base de datos MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Jony123456789*@localhost:3307/facturacion'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos con SQLAlchemy
db.init_app(app)

# Registrar los blueprints
app.register_blueprint(cliente_bp)
app.register_blueprint(producto_bp)
app.register_blueprint(factura_bp)
app.register_blueprint(usuario_bp)  # Solo si ya tienes ese controlador

# Ruta principal
@app.route('/')
def home():
    return render_template('inicio.html')

# Ruta temporal para crear las tablas en la base de datos
@app.route('/crear_tablas')
def crear_tablas():
    db.create_all()
    return 'Tablas creadas exitosamente.'

if __name__ == '__main__':
    app.run(debug=True)
