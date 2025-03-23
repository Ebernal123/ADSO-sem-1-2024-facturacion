document.addEventListener("DOMContentLoaded", function() {
    const productosLista = document.getElementById("productos-lista");
    const agregarProductoBtn = document.getElementById("agregar-producto");
    const subtotalInput = document.getElementById("subtotal");
    const impuestosInput = document.getElementById("impuestos");
    const totalInput = document.getElementById("total");

    function actualizarTotales() {
        let subtotal = 0;
        document.querySelectorAll("#productos-lista tr").forEach(row => {
            const cantidad = parseFloat(row.querySelector(".cantidad").value) || 0;
            const precio = parseFloat(row.querySelector(".precio").value) || 0;
            const total = cantidad * precio;
            row.querySelector(".total").value = total.toFixed(2);
            subtotal += total;
        });

        const impuestos = subtotal * 0.19;
        subtotalInput.value = subtotal.toFixed(2);
        impuestosInput.value = impuestos.toFixed(2);
        totalInput.value = (subtotal + impuestos).toFixed(2);
    }

    agregarProductoBtn.addEventListener("click", function() {
        const nuevaFila = document.createElement("tr");
        nuevaFila.innerHTML = `
            <td><select class="form-control"><option value="1">Producto 1</option><option value="2">Producto 2</option></select></td>
            <td><input type="number" class="form-control cantidad" value="1"></td>
            <td><input type="text" class="form-control precio" value="0" readonly></td>
            <td><input type="text" class="form-control total" value="0" readonly></td>
        `;
        productosLista.appendChild(nuevaFila);
        nuevaFila.querySelector(".cantidad").addEventListener("input", actualizarTotales);
    });

    document.getElementById("productos-lista").addEventListener("input", actualizarTotales);
});
