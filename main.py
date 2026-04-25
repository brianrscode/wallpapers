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

print("README.md generado con éxito.")
