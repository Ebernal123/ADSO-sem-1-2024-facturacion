from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.cliente import db, Cliente
from models.factura import Factura, DetalleFactura
from models.producto import Producto
from models.usuario import Usuario  # Nuevo: importar modelo Usuario

factura_bp = Blueprint("facturas", __name__)

# LISTAR FACTURAS
@factura_bp.route("/facturas")
def listar_facturas():
    facturas = Factura.query.order_by(Factura.id.desc()).all()
    return render_template("facturas/lista.html", facturas=facturas)

# CREAR FACTURA (GET muestra formulario, POST guarda)
@factura_bp.route("/facturas/nueva", methods=["GET", "POST"])
def crear_factura():
    clientes = Cliente.query.order_by(Cliente.identificacion).all()
    productos = Producto.query.order_by(Producto.codigo).all()
    usuarios = Usuario.query.order_by(Usuario.nombre).all()  # Obtener usuarios

    if request.method == "POST":
        cliente_id = request.form.get("cliente_id")
        usuario_id = request.form.get("usuario_id")  # Captura del usuario
        if not cliente_id or not usuario_id:
            flash("Seleccione cliente y usuario.", "warning")
            return redirect(url_for("facturas.crear_factura"))

        # Fecha de la factura
        fecha_str = request.form.get("fecha")
        fecha_obj = None
        if fecha_str:
            try:
                fecha_obj = datetime.strptime(fecha_str, "%Y-%m-%d")
            except Exception:
                fecha_obj = None

        # Crear la factura
        factura = Factura(cliente_id=cliente_id, usuario_id=usuario_id)
        if fecha_obj:
            factura.fecha = fecha_obj

        db.session.add(factura)
        db.session.flush()  # Para obtener factura.id

        # Leer detalles
        codigos = request.form.getlist("producto_codigo[]")
        cantidades = request.form.getlist("cantidad[]")
        precios = request.form.getlist("precio_unitario[]")

        filas_validas = 0
        for codigo, cant, precio in zip(codigos, cantidades, precios):
            codigo = (codigo or "").strip()
            cant = (cant or "").strip()
            precio = (precio or "").strip()
            if not codigo or not cant or not precio:
                continue

            producto = Producto.query.filter_by(codigo=codigo).first()
            if not producto:
                continue

            try:
                cantidad = int(cant)
                precio_unitario = float(precio)
            except ValueError:
                continue
            if cantidad <= 0 or precio_unitario <= 0:
                continue

            detalle = DetalleFactura(
                factura_id=factura.id,
                producto_codigo=producto.codigo,
                cantidad=cantidad,
                precio_unitario=precio_unitario
            )
            db.session.add(detalle)
            filas_validas += 1

        if filas_validas == 0:
            db.session.rollback()
            flash("No se agregaron productos válidos.", "warning")
            return redirect(url_for("facturas.crear_factura"))

        db.session.commit()
        flash("Factura creada correctamente.", "success")
        return redirect(url_for("facturas.listar_facturas"))

    # GET: mostrar formulario
    productos_json = {p.codigo: {"nombre": p.nombre, "precio": float(p.precio)} for p in productos}
    return render_template(
        "facturas/nueva.html",
        clientes=clientes,
        productos=productos,
        usuarios=usuarios,
        productos_json=productos_json
    )

# ELIMINAR FACTURA (POST)
@factura_bp.route("/facturas/eliminar/<int:id>", methods=["POST"])
def eliminar_factura(id):
    factura = Factura.query.get_or_404(id)
    try:
        db.session.delete(factura)
        db.session.commit()
        flash("Factura eliminada correctamente.", "success")
    except Exception:
        db.session.rollback()
        flash("Error al eliminar la factura.", "danger")
    return redirect(url_for("facturas.listar_facturas"))

# VER DETALLE DE FACTURA
@factura_bp.route("/facturas/<int:id>")
def ver_factura(id):
    factura = Factura.query.get_or_404(id)
    return render_template("facturas/factura.detalle.html", factura=factura)

