"""
<table>
  <!-- Fila de la cabecera -->
  <tr>
    <th>Título columna 1</th> <!-- Celda cabecera de la columna 1 -->
    <th>Título columna 2</th> <!-- Celda cabecera de la columna 2 -->
    <th>Título columna 3</th> <!-- Celda cabecera de la columna 3 -->
  </tr>
  <!-- Primera fila -->
  <tr>
    <td>Celda 1x1</td> <!-- Primera celda de la primera fila -->
    <td>Celda 2x1</td> <!-- Segunda celda de la primera fila -->
    <td>Celda 3x1</td> <!-- Tercera celda de la primera fila -->
  </tr>
  <!-- Segunda fila -->
  <tr>
    <td>Celda 1x2</td> <!-- Primera celda de la segunda fila -->
    <td>Celda 2x2</td> <!-- Segunda celda de la segunda fila -->
    <td>Celda 3x2</td> <!-- Tercera celda de la segunda fila -->
  </tr>
</table>
"""

import os

EXTENSIONES_VALIDAS = (".png", ".jpg", ".jpeg", ".webp", ".gif")
COLUMNAS = 4


def es_imagen(nombre):
    return nombre.lower().endswith(EXTENSIONES_VALIDAS)


def ruta_github(path):
    return path.replace("\\", "/")


with open("README.md", "w", encoding="utf-8") as f:
    f.write("# Wallpapers\n\n")

    for ruta, directorios, archivos in os.walk("."):
        # Ignorar .git
        if ".git" in directorios:
            directorios.remove(".git")

        # Filtrar imágenes y ordenar
        imagenes = sorted([a for a in archivos if es_imagen(a)])

        if not imagenes:
            continue

        ruta_relativa = ruta.replace("./", "")
        titulo = ruta_relativa if ruta_relativa else "Root"

        f.write(f"## 📁 {titulo}\n\n")
        f.write("<table>\n")

        for i, archivo in enumerate(imagenes):
            if i % COLUMNAS == 0:
                f.write("<tr>\n")

            path = ruta_github(os.path.join(ruta, archivo))

            f.write(
                f'<td align="center">'
                f'<img src="{path}" width="200"><br>'
                f"<sub>{archivo}</sub>"
                f"</td>\n"
            )

            if (i + 1) % COLUMNAS == 0:
                f.write("</tr>\n")

        # Cerrar fila incompleta
        if len(imagenes) % COLUMNAS != 0:
            f.write("</tr>\n")

        f.write("</table>\n\n")
