document.addEventListener("DOMContentLoaded", function() {
    console.log("usuarios.js cargado correctamente");  // 🔹 Mensaje de prueba

    const usuarioForm = document.getElementById("usuario-form");
    const usuariosLista = document.getElementById("usuarios-lista");

    if (!usuarioForm || !usuariosLista) {
        console.error("Error: No se encontró el formulario o la tabla.");
        return;
    }

    usuarioForm.addEventListener("submit", function(event) {
        event.preventDefault(); // Evita que la página se recargue

        const nombre = document.getElementById("nombre").value.trim();
        const correo = document.getElementById("correo").value.trim();
        const rol = document.getElementById("rol").value;

        if (nombre === "" || correo === "") {
            alert("Por favor, complete todos los campos.");
            return;
        }

        const nuevaFila = document.createElement("tr");
        nuevaFila.innerHTML = `
            <td>${nombre}</td>
            <td>${correo}</td>
            <td>${rol}</td>
            <td>
                <button class="btn btn-danger btn-sm eliminar">Eliminar</button>
            </td>
        `;
        usuariosLista.appendChild(nuevaFila);
        console.log("Usuario agregado:", nombre, correo, rol);  // 🔹 Mensaje de prueba

        // Agregar evento para eliminar usuario
        nuevaFila.querySelector(".eliminar").addEventListener("click", function() {
            nuevaFila.remove();
            console.log("Usuario eliminado");  // 🔹 Mensaje de prueba
        });

        usuarioForm.reset();
    });
});


