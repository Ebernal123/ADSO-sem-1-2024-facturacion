from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.producto import Producto
from models import db

producto_bp = Blueprint('producto_bp', __name__, url_prefix='/producto')


@producto_bp.route('/crear_db')
def crear_db():
    db.create_all()
    return 'Tabla de productos creada correctamente.'


@producto_bp.route('/nuevo')
def nuevo_producto():
    return render_template('productos/formulario_producto.html')


@producto_bp.route('/guardar', methods=['POST'])
def guardar_producto():
    codigo = request.form['codigo']
    nombre = request.form['nombre']
    descripcion = request.form['descripcion']
    precio = request.form['precio']

    producto = Producto(
        codigo=codigo,
        nombre=nombre,
        descripcion=descripcion,
        precio=precio
    )

    db.session.add(producto)
    db.session.commit()

    flash('Producto guardado correctamente.')
    return redirect(url_for('producto_bp.lista_productos'))


@producto_bp.route('/lista')
def lista_productos():
    productos = Producto.query.all()
    return render_template('productos/lista_productos.html', productos=productos)


@producto_bp.route('/eliminar/<codigo>')
def eliminar_producto(codigo):
    producto = Producto.query.get(codigo)
    if producto:
        db.session.delete(producto)
        db.session.commit()
        flash('Producto eliminado correctamente.')
    return redirect(url_for('producto_bp.lista_productos'))


@producto_bp.route('/editar/<codigo>', methods=['GET', 'POST'])
def editar_producto(codigo):
    producto = Producto.query.get(codigo)

    if request.method == 'POST':
        producto.nombre = request.form['nombre']
        producto.descripcion = request.form['descripcion']
        producto.precio = request.form['precio']
        db.session.commit()
        flash('Producto actualizado correctamente.')
        return redirect(url_for('producto_bp.lista_productos'))

    return render_template('productos/formulario_producto.html', producto=producto)

