from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.cliente import Cliente
from models import db

cliente_bp = Blueprint('cliente_bp', __name__, url_prefix='/cliente')

# Ruta para crear la base de datos
@cliente_bp.route('/crear_db')
def crear_db():
    db.create_all()
    return 'Base de datos y tabla creadas correctamente.'

# Ruta para ver el formulario de nuevo cliente
@cliente_bp.route('/nuevo', methods=['GET'])
def nuevo_cliente():
    return render_template('clientes/formulario_cliente.html')

# Ruta para guardar el cliente (POST)
@cliente_bp.route('/guardar', methods=['POST'])
def guardar_cliente():
    identificacion = request.form['identificacion']
    nombre = request.form['nombre']
    correo = request.form['correo']
    telefono = request.form['telefono']

    cliente = Cliente(
        identificacion=identificacion,
        nombre=nombre,
        correo=correo,
        telefono=telefono
    )

    try:
        db.session.add(cliente)
        db.session.commit()
        flash('Cliente guardado correctamente.', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error al guardar el cliente: {str(e)}', 'error')

    return redirect(url_for('cliente_bp.lista_clientes'))

# Ruta para ver la lista de clientes
@cliente_bp.route('/lista')
def lista_clientes():
    clientes = Cliente.query.all()
    return render_template('clientes/lista_clientes.html', clientes=clientes)

# Ruta para eliminar cliente
@cliente_bp.route('/eliminar/<identificacion>')
def eliminar_cliente(identificacion):
    cliente = Cliente.query.get(identificacion)
    if cliente:
        db.session.delete(cliente)
        db.session.commit()
        flash('Cliente eliminado correctamente.', 'success')
    else:
        flash('Cliente no encontrado.', 'error')

    return redirect(url_for('cliente_bp.lista_clientes'))

# Ruta para editar cliente (GET para ver el formulario, POST para guardar)
@cliente_bp.route('/editar/<identificacion>', methods=['GET', 'POST'])
def editar_cliente(identificacion):
    cliente = Cliente.query.get(identificacion)

    if request.method == 'POST':
        cliente.nombre = request.form['nombre']
        cliente.correo = request.form['correo']
        cliente.telefono = request.form['telefono']

        try:
            db.session.commit()
            flash('Cliente actualizado correctamente.', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error al actualizar: {str(e)}', 'error')

        return redirect(url_for('cliente_bp.lista_clientes'))

    return render_template('clientes/formulario_cliente.html', cliente=cliente)
