import datetime
from django.http import HttpResponse
from django.template import Template,Context

class Persona(object):
    def __init__(self,nombre,apellidos):
        self.nombre = nombre
        self.apellidos =apellidos


def saludo(request): #primera vista
    return HttpResponse("Hola mundo!")

def hola(request): #primera vista
    p1=Persona("Profesor Rafa","Montero")
    #nombre="Rafa"
    #apellidos="Montero"
    doc_externo=open("C:/Users/alber/OneDrive/Documentos/GitHub/trabajoDjango/trabajoDjango/plantillas/plantillaBase.html")
    ahora=datetime.datetime.now()
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellidos,"fecha":ahora})
    documento=plt.render(ctx)
    return HttpResponse(documento)

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

def calcular_edad(request,edad,anio):
    #edad_actual = 18
    periodo = anio-2022
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
