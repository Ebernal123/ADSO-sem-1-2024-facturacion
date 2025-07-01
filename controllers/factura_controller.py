from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.factura import Factura
from models.cliente import db, Cliente
from datetime import datetime

factura_bp = Blueprint('factura_bp', __name__, template_folder='../templates/factura')

@factura_bp.route('/facturas')
def listar_facturas():
    facturas = Factura.query.all()
    return render_template('factura/lista.html', facturas=facturas)

@factura_bp.route('/facturas/nueva', methods=['GET', 'POST'])
def nueva_factura():
    if request.method == 'POST':
        cliente_id = request.form['cliente_id']
        fecha = datetime.strptime(request.form['fecha'], '%Y-%m-%d')
        nueva = Factura(cliente_id=cliente_id, fecha=fecha)
        db.session.add(nueva)
        db.session.commit()
        flash('Factura creada exitosamente')
        return redirect(url_for('factura_bp.listar_facturas'))
    



    clientes = Cliente.query.all()
    return render_template('factura/nueva.html', clientes=clientes)
