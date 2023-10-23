from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

# MVC = Modelo Vista Controlador -> Acciones (métodos)
# MVT = MOdelo Template Vista -> Acciones (métodos)

layout = """
<h1> Sito Web con Django | Josué Martínez </h1>
<ul>
    <li>
        <a href="/inicio">Inicio</a>
    </li>
    <li>
        <a href="/hola-mundo">Hola mundo</a>
    </li>
    <li>
        <a href="/pagina">Pagina de pruebas</a>
    </li>
    <li>
        <a href="/contacto">Contacto</a>
    </li>
</ul>
"""
def index(request):
    html = """ 
            <h1>Inicio</h1>
            <p>Años hasta el 2050:</p>
            <ul>
            """
    year = 2021
    while year <= 2050:
        if year % 2 == 0:
            html += f"<li>{str(year)}</li>"
        year +=1
    html += """
            </ul>
            """
    a = 5
    nombre = 'Esaú Martinez'
    lenguajes = ['JavaScript', 'Python', 'PHP', 'C']
    
    return render(request, 'index.html',{
        'mi_variable': f'Soy un dato que esta en la vista  {a}',
        'title': 'Este es un titulo',
        'nombre': nombre,
        'lenguajes': lenguajes 
    })
def hola_mundo(request):
    return render(request,'hola_mundo.html')
def pagina(request,redirigir = 0):
    if redirigir == 1:
        return redirect('//www.google.com')

    return render(request, 'pagina.html')

def contacto(request):
    return HttpResponse(layout+f"<h2>Contacto:</h2>")