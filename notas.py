<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Registro de Notas</title>
</head>
<body>
  <h2>Registro de Notas del Estudiante</h2>

  <label>Nombre del estudiante:</label>
  <input type="text" id="nombre"><br><br>

  <label>Matemáticas:</label>
  <input type="number" id="matematicas" step="0.1"><br>

  <label>Lenguaje:</label>
  <input type="number" id="lenguaje" step="0.1"><br>

  <label>Ciencias:</label>
  <input type="number" id="ciencias" step="0.1"><br>

  <label>Historia:</label>
  <input type="number" id="historia" step="0.1"><br>

  <label>Inglés:</label>
  <input type="number" id="ingles" step="0.1"><br><br>

  <button onclick="guardarJSON()">Guardar en JSON</button>

  <script>
    async function guardarJSON() {
      const datos = {
        "Nombre": document.getElementById("nombre").value,
        "Matemáticas": parseFloat(document.getElementById("matematicas").value),
        "Lenguaje": parseFloat(document.getElementById("lenguaje").value),
        "Ciencias": parseFloat(document.getElementById("ciencias").value),
        "Historia": parseFloat(document.getElementById("historia").value),
        "Inglés": parseFloat(document.getElementById("ingles").value)
      };

      const jsonData = JSON.stringify(datos, null, 2);

      try {
        const handle = await window.showSaveFilePicker({
          suggestedName: "notas.json",
          types: [{
            description: "Archivo JSON",
            accept: { "application/json": [".json"] }
          }]
        });

        const writable = await handle.createWritable();
        await writable.write(jsonData);
        await writable.close();

        alert("Archivo 'notas.json' guardado correctamente");
      } catch (error) {
        alert("No se pudo guardar el archivo");
        console.error(error);
      }
    }
  </script>
</body>
</html>
