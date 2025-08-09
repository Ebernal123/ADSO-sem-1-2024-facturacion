# controllers/usuario_controller.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.usuario import Usuario
from models import db

# Blueprint con prefijo /usuarios -> rutas: /usuarios/, /usuarios/crear, etc.
usuario_bp = Blueprint('usuarios', __name__, url_prefix='/usuarios')

@usuario_bp.route('/', methods=['GET'])
def listar_usuarios():
    usuarios = Usuario.query.all()
    return render_template('usuarios/listar_usuarios.html', usuarios=usuarios)

@usuario_bp.route('/crear', methods=['GET', 'POST'])
def crear_usuario():
    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        correo = request.form.get('correo', '').strip()
        rol = request.form.get('rol', '').strip() or 'usuario'

        try:
            nuevo = Usuario(nombre=nombre, correo=correo, rol=rol)
            db.session.add(nuevo)
            db.session.commit()
            flash('Usuario creado correctamente.', 'success')
            return redirect(url_for('usuarios.listar_usuarios'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error al crear usuario: {e}', 'error')

    return render_template('usuarios/crear_usuario.html')

@usuario_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_usuario(id):
    usuario = Usuario.query.get_or_404(id)

    if request.method == 'POST':
        usuario.nombre = request.form.get('nombre', usuario.nombre).strip()
        usuario.correo = request.form.get('correo', usuario.correo).strip()
        usuario.rol = request.form.get('rol', usuario.rol).strip()

        try:
            db.session.commit()
            flash('Usuario actualizado correctamente.', 'success')
            return redirect(url_for('usuarios.listar_usuarios'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error al actualizar usuario: {e}', 'error')

    return render_template('usuarios/editar_usuario.html', usuario=usuario)

@usuario_bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    try:
        db.session.delete(usuario)
        db.session.commit()
        flash('Usuario eliminado correctamente.', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error al eliminar usuario: {e}', 'error')
    return redirect(url_for('usuarios.listar_usuarios'))

