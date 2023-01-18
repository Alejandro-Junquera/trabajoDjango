import datetime
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render
class Persona(object):
    def __init__(self,nombre,apellidos):
        self.nombre = nombre
        self.apellidos =apellidos

def inicio(request): #primera vista
    p1=Persona("Vengo de un objeto y soy la propiedad nombre","Vengo del mismo objeto perosona y soy la propiedad apellidos")
    nombre="Soy la variable nombre"
    p2=Persona("Rafa","Montero")
    lista=["Soy la posición 1 de la lista","Soy la posición 2 de la lista","Soy la posición 3 de la lista","Soy la posición 4 de la lista"]
    # Punto 8: Usar loader para cargar plantillas 
    # (El metodo es loader.get_template, pero esta importado el metodo directamente)
    # Ademas, en settings.py hay un apartado para configurar el archivo de donde Django saca
    # las plantillas. En este caso, 'DIRS': ['trabajoDjango/plantillas'] 
    # en Templates (linea 62 de Settings)
    doc_externo=get_template("index.html")
    # Puntos 1,2 y 4: Pasar variables a la plantilla html desde las funciones,
    # Pasar objetos a la plantilla html desde las funciones	y Pasar lista a una plantilla
    # Descomenta lo de abajo y comenta el punto de los shortcuts	
    #documento=doc_externo.render({"objeto_persona":p1,"nombre_variable":nombre, "lista":lista, "profesor":p2})
    #return HttpResponse(documento)
    # Punto 9: Usar shortcuts para la carga de plantillas	
    return render (request, 'index.html',{"objeto_persona":p1,"nombre_variable":nombre, "lista":lista, "profesor":p2})
def saludo(request):
    return HttpResponse("Hola mundo!")

def hola(request): 
    p1=Persona("Profesor Rafa","Montero")
    ahora=datetime.datetime.now()
    return render(request, 'plantillaBase.html',{"nombre_persona":p1.nombre,"apellido_persona":p1.apellidos,"fecha":ahora})

def mostrar_fecha(request): #mostar fecha
    fecha_actual=datetime.datetime.now()
    documento="""
        <html>
            <head>
            </head>
            <body>
                <h3>Fecha y hora actual: %s</h3>
            </body>
        </html>
    """%fecha_actual
    return HttpResponse(documento)

def calcular_edad(request,edad,cumplidos,anio):
    #edad_actual = 18
    cumplidos = cumplidos == 'True'
    periodo = anio-2022
    if(cumplidos):
        edad_futura=edad+periodo-1
    else:
        edad_futura=edad+periodo
    documento="""
        <html>
            <head>
            </head>
            <body>
                <h3>En el año %s tendrás %s años</h3>
            </body>
        </html>
    """%(anio,edad_futura)
    return HttpResponse(documento)
