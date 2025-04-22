from flask import Flask, render_template

app = Flask(__name__)

# Ruta principal
@app.route('/')
def home():
    return render_template('index.html')

# Clientes
@app.route('/clientes')
def clientes():
    return render_template('clientes/formulario_cliente.html')

# Productos
@app.route('/productos')
def productos():
    return render_template('productos/lista_productos.html')

@app.route('/producto/nuevo', methods=['GET', 'POST'])
def nuevo_producto():
    return render_template('productos/formulario_producto.html')

# Usuarios
@app.route('/usuarios')
def usuarios():
    return render_template('usuarios/formulario_usuario.html')

# Facturación
@app.route('/facturas')
def facturas():
    return render_template('facturas/factura.html')

if __name__ == '__main__':
    app.run(debug=True)
