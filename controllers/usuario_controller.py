from flask import Blueprint, render_template, request, redirect, flash, url_for
from models.usuario import Usuario  # Asegúrate de tener este modelo creado
from models.cliente import db       # Reutilizamos db desde cliente

usuario_bp = Blueprint('usuarios', __name__, url_prefix='/usuarios')

# Listar usuarios
@usuario_bp.route('/')
def listar_usuarios():
    usuarios = Usuario.query.all()
    return render_template('usuarios/listar_usuarios.html', usuarios=usuarios)

# Crear usuario
@usuario_bp.route('/crear', methods=['GET', 'POST'])
def crear_usuario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        rol = request.form['rol']

        nuevo_usuario = Usuario(nombre=nombre, correo=correo, rol=rol)
        db.session.add(nuevo_usuario)
        db.session.commit()
        return redirect(url_for('usuarios.listar_usuarios'))

    return render_template('usuarios/crear_usuario.html')

# Editar usuario
@usuario_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_usuario(id):
    usuario = Usuario.query.get_or_404(id)

    if request.method == 'POST':
        usuario.nombre = request.form['nombre']
        usuario.correo = request.form['correo']
        usuario.rol = request.form['rol']

        try:
            db.session.commit()
            flash('Usuario actualizado exitosamente.')
            return redirect(url_for('usuarios.listar_usuarios'))
        except Exception as e:
            db.session.rollback()
            flash('Error al actualizar el usuario.')

    return render_template('usuarios/editar_usuario.html', usuario=usuario)

# Eliminar usuario
@usuario_bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return redirect(url_for('usuarios.listar_usuarios'))

