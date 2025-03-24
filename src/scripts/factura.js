document.addEventListener("DOMContentLoaded", function() {
    console.log("✅ factura.js cargado correctamente");

    const productosLista = document.getElementById("productos-lista");
    const agregarProductoBtn = document.getElementById("agregar-producto");
    const subtotalInput = document.getElementById("subtotal");
    const impuestosInput = document.getElementById("impuestos");
    const totalInput = document.getElementById("total");
    const numeroFacturaInput = document.getElementById("numero_factura");

    // Generar número de factura aleatorio
    numeroFacturaInput.value = "FAC-" + Math.floor(Math.random() * 10000);

    // Función para actualizar los totales
    function actualizarTotales() {
        let subtotal = 0;
        document.querySelectorAll("#productos-lista tr").forEach(row => {
            const cantidadInput = row.querySelector(".cantidad");
            const precioInput = row.querySelector(".precio");
            const totalInput = row.querySelector(".total");

            if (!cantidadInput || !precioInput || !totalInput) return;

            const cantidad = parseFloat(cantidadInput.value) || 0;
            const precio = parseFloat(precioInput.value) || 0;
            const total = cantidad * precio;

            totalInput.value = total.toFixed(2);
            subtotal += total;
        });

        const impuestos = subtotal * 0.19;
        subtotalInput.value = subtotal.toFixed(2);
        impuestosInput.value = impuestos.toFixed(2);
        totalInput.value = (subtotal + impuestos).toFixed(2);
    }

    // Evento para agregar un producto
    agregarProductoBtn.addEventListener("click", function() {
        const nuevaFila = document.createElement("tr");
        nuevaFila.innerHTML = `
            <td>
                <select class="form-control producto">
                    <option value="1" data-precio="5000">Pan tajado bolsa 200 grs</option>
                    <option value="2" data-precio="32000">Carne cerdo costilla</option>
                </select>
            </td>
            <td><input type="number" class="form-control cantidad" value="1"></td>
            <td><input type="text" class="form-control precio" value="5000" readonly></td>
            <td><input type="text" class="form-control total" value="5000" readonly></td>
        `;
        productosLista.appendChild(nuevaFila);

        // Evento para actualizar totales al cambiar cantidad
        nuevaFila.querySelector(".cantidad").addEventListener("input", actualizarTotales);

        // Evento para actualizar precio según el producto seleccionado
        nuevaFila.querySelector(".producto").addEventListener("change", function() {
            const precio = parseFloat(this.selectedOptions[0].getAttribute("data-precio")) || 0;
            nuevaFila.querySelector(".precio").value = precio.toFixed(2);
            actualizarTotales();
        });

        actualizarTotales();
    });

    // Evento para capturar el envío del formulario
    document.getElementById("factura-form").addEventListener("submit", function(event) {
        event.preventDefault(); // Evita que la página se recargue
        
        console.log("🔄 Actualizando totales antes de generar la factura...");
        actualizarTotales(); // Asegura que los valores están correctos
    
        const numeroFactura = numeroFacturaInput.value;
        const fecha = document.getElementById("fecha").value;
        const cliente = document.getElementById("cliente").value;
        const metodoPago = document.getElementById("metodo_pago").value;
        const subtotal = parseFloat(subtotalInput.value) || 0;
        const impuestos = parseFloat(impuestosInput.value) || 0;
        const total = parseFloat(totalInput.value) || 0;
    
        console.log("✅ Factura generada con éxito:");
        console.log("Número de Factura:", numeroFactura);
        console.log("Fecha de Emisión:", fecha);
        console.log("Cliente:", cliente);
        console.log("Método de Pago:", metodoPago);
        console.log("Subtotal:", subtotal.toFixed(2));
        console.log("Impuestos (IVA):", impuestos.toFixed(2));
        console.log("Total a Pagar:", total.toFixed(2));
    
        if (subtotal === 0) {
            console.warn("⚠️ Error: El subtotal es 0. Verifica que los productos tengan precios correctos.");
        }
    });
});

