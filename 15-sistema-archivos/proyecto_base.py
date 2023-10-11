import os
from io import open
import pathlib

ruta_components = "./proyecto_base/components"
ruta_css = "./proyecto_base/css"
ruta_pug = "./proyecto_base/pug"

def head(file):
    try:
        file.write("head \n")
        file.write("   meta(http-equiv='X-UA-Compatible', content='IE=edge')\n")
        file.write("   meta(name='viewport' content='initial-scale=1.0')\n")
        file.write("   title Titulo del sitio\n")
        file.write("   link(rel='preconnect' href='https://fonts.googleapis.com')\n")
        file.write("   link(rel='preconnect' href='https://fonts.gstatic.com') crossorigin \n")
        file.write("   link(href='https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=Raleway:wght@100;300;400;600;800&display=swap' rel='stylesheet')\n")
        file.write("   link(rel='stylesheet' href='css/style.css')\n")
        file.write("   link(rel='stylesheet' href='css/tablet.css' media='screen and (min-width: 768px)')\n")
        file.write("   link(rel='stylesheet' href='css/desktop.css' media='screen and (min-width: 1024px)')\n")
        file.write("   link(rel='stylesheet' href='css/menu.css')\n")
        file.write("   link(rel='stylesheet' href='css/form.css')\n")
        file.write("   link(rel='shortcut icon' href='images/favIcon.png')\n")
        file.write("   link(href='https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css' rel='stylesheet'  crossorigin='anonymous')\n")
        file.write("   script(src='https://code.jquery.com/jquery-3.2.1.slim.min.js' integrity='sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN' crossorigin='anonymous')\n")
        file.write("   script(src='https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.5/dist/umd/popper.min.js' integrity='sha384-Xe+8cL9oJa6tN/veChSP7q+mnSPaj5Bcu9mPX5F5xIGE0DVittaqT5lorf0EI7Vk' crossorigin='anonymous')\n")
        file.write("   script(src='https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.min.js' integrity='sha384-kjU+l4N0Yf4ZOJErLsIcvOU2qSb74wXpOhqTvwVx3OElZRweTnQ6d31fXEoRD1Jy' crossorigin='anonymous')\n")
        file.write("   script(src='https://code.jquery.com/jquery-latest.js')\n")
        print("head.pug: Se han ingresado la información de head.pug exitosamente")
    except:
        print("head.pug: Ha ocurrido un error al ingresar la información en el archivo head.pug")
def index(file):
    try:
        file.write("extend ../components/template.pug")
        file.write("block content")
        print("index.pug: Se han ingresado la información de index.pug exitosamente")
    except:
        print("index.pug: Ocurrio un error al ingresar la información en index.pug")
def template(file):
    try:
        file.write("include ../components/config.pug\n")
        file.write("doctype html \n")
        file.write("html \n")
        file.write("    include ../components/head.pug \n")
        file.write("    body  \n")
        file.write("    include ../components/header.pug \n")
        file.write("    block content \n")
        file.write("    include ../components/footer.pug \n")
        print("template.pug: Se han ingresado la información de template.pug exitosamente")
    except:
        print("template.pug: Hubo un error al cargar la información en template.pug")
def header(file):
    try:
        file.write("header\n")
        print("header.pug: Se ha ingresado correctamente la información.")
    except:
        print("header.pug: Hubo un error al ingresar la información")
def footer(file):
    try:
        file.write("footer\n")
        file.write("    script(src='../js/script.js') \n")
        print("footer.pug: Se ha ingresado correctamente la información.")
    except:
        print("footer.pug: Hubo un error al ingresar la información")
def desktop_css(file):
    try:
        file.write("@import 'globals.less';\n")
        file.write("@import 'variables.less';\n")
        print("desktop.less: Se ha ingresado exitosamente la información")

    except:
        print("desktop.less: Ha ocurrido un error al ingresar la información")
def tablet_css(file):
    try:
        file.write("@import 'globals.less';\n")
        file.write("@import 'variables.less';\n")
        print("tablet.less: Se ha ingresado exitosamente la información")

    except:
        print("tablet.less: Ha ocurrido un error al ingresar la información")
def mobile_css(file):
    try:
        file.write("@import 'globals.less';\n")
        file.write("@import 'variables.less';\n")
        print("mobile.less: Se ha ingresado exitosamente la información")

    except:
        print("mobile.less: Ha ocurrido un error al ingresar la información")
def globals_css(file):
    try:
        file.write("@import 'variables.less';\n")
        file.write("* {\n-webkit-box-sizing: border-box;\nbox-sizing: border-box;\nmargin: 0;\npadding: 0;\n}\nhtml{\nfont-size: 62.5%;\n}body {\nfont-family: @font-family;\n}\n.hidden{\ndisplay: none !important;\n}\n")
        print("globals.less: Se ha ingresado exitosamente la información")

    except:
        print("globals.less: Ha ocurrido un error al ingresar la información")
def variables_css(file):
    try:
        file.write("@font-size-sm: 1.2rem;\n")
        file.write("@font-size-md: 1.4rem;\n")
        file.write("@font-size-lg: 1.8rem;\n")
        file.write("@font-extralight: 200;\n")
        file.write("@font-light: 300;\n")
        file.write("@font-regular: 400;\n")
        file.write("@font-semibold: 600;\n")
        file.write("@font-bold: 800;\n")
        print("variables.less: Se ha ingresado correctamente la información")
    except:
        print("variables.less: Ha ocurrido un error al ingresar la información")

#Creación de la carpeta principal
if not os.path.isdir("./poyecto_base"):
    os.mkdir("./proyecto_base")
    print("Se crea la carpeta principal")
    # Creación de la carpeta components
    if not os.path.isdir("./proyecto_base/components"):
        os.mkdir("./proyecto_base/components")
        print("Se ha creado la carpeta components con éxito")
        # Creación del archivo head.pug
        path_head = ruta_components + "/head.pug"
        file_head = open(path_head, "a+")
        head(file_head)
        file_head.close()
        # Creación del archivo template.pug
        path_template = ruta_components + "/template.pug"
        file_template = open(path_template, "+a")
        template(file_template)
        file_template.close()
        # Creación del archivo header.pug
        path_header = ruta_components + "/header.pug"
        file_header = open(path_header, "+a")
        header(file_header)
        file_header.close()
        # Creación del archivo footer.pug
        path_footer = ruta_components + "/footer.pug"
        file_footer = open(path_footer, "+a")
        footer(file_footer)
        file_footer.close()

    # Creación de la carpeta css    
    if not os.path.isdir("./proyecto_base/css"):
        os.mkdir("./proyecto_base/css")
        print("Se ha creado la carpeta css con éxito")
        # Creación del archivo desktop.less
        path_desktop = ruta_css +"/desktop.less"
        file_desktop = open(path_desktop,"+a")
        desktop_css(file_desktop)
        file_desktop.close()
        # Creación del archivo tablet.less
        path_tablet = ruta_css +"/tablet.less"
        file_tablet = open(path_tablet,"+a")
        tablet_css(file_tablet)
        file_tablet.close()
         # Creación del archivo mobile.less
        path_mobile = ruta_css +"/mobile.less"
        file_mobile = open(path_mobile,"+a")
        mobile_css(file_mobile)
        file_mobile.close()
        # Creación del archivo variables.less
        path_variables = ruta_css +"/variables.less"
        file_variables = open(path_variables,"+a")
        variables_css(file_variables)
        file_variables.close()
        # Creación del archivo globals.less
        path_globals = ruta_css +"/globals.less"
        file_globals = open(path_globals,"+a")
        globals_css(file_globals)
        file_globals.close()
    # Creación de la carpeta Images  
    if not os.path.isdir("./proyecto_base/images"):
        os.mkdir("./proyecto_base/images")
        print("Se ha creado la carpeta images con éxito")
    # Creación de la carpeta pug  
    if not os.path.isdir("./proyecto_base/pug"):
        os.mkdir("./proyecto_base/pug")
        print("Se ha creado la carpeta pug con éxito")
        # Creación del archivo index.pug
        path_index = ruta_pug+"/index.pug"
        file_index = open(path_index, "+a")
        index(file_index)
        file_index.close()
else:
    print("La carpeta ya existe.")