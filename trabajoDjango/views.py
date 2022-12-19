import datetime
from django.http import HttpResponse

def saludo(request): #primera vista
    return HttpResponse("Hola mundo!")

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
