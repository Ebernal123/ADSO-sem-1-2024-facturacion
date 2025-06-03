from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "Jony123456789*"  # IMPORTANTE para usar flash()

# Configuración base de datos (ajusta si usas otro puerto)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3307/facturacion'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('index.html')


# Modelo Cliente
class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    telefono = db.Column(db.String(20))

# Ruta para crear la base de datos y tablas
@app.route('/crear_db')
def crear_db():
    db.create_all()
    return "Base de datos y tablas creadas correctamente"

# Mostrar lista clientes
@app.route('/clientes')
def clientes():
    lista_clientes = Cliente.query.all()
    return render_template('clientes/lista_clientes.html', clientes=lista_clientes)

# NUEVO Cliente - manejar GET y POST
@app.route('/cliente/nuevo', methods=['GET', 'POST'])
def nuevo_cliente():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        correo = request.form.get('correo')
        telefono = request.form.get('telefono')
        
        nuevo = Cliente(nombre=nombre, correo=correo, telefono=telefono)
        
        try:
            db.session.add(nuevo)
            db.session.commit()
            flash("Cliente guardado correctamente", "success")
            return redirect(url_for('clientes'))
        except Exception as e:
            db.session.rollback()
            flash(f"Error guardando cliente: {e}", "danger")
            return redirect(url_for('nuevo_cliente'))
    
    return render_template('clientes/formulario_cliente.html')


if __name__ == '__main__':
    app.run(debug=True)
