# coding: utf-8


from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
import requests
import json


# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJqbWFudWVsYWJAc2FzZW1hci5lcyIsImp0aSI6IjU2NWM5MDc2LTcxN2YtNDc5My05NmY4LWFjZWRhOWQ3ZTIyNyIsImlzcyI6IkFFTUVUIiwiaWF0IjoxNTg2MDc0NTIyLCJ1c2VySWQiOiI1NjVjOTA3Ni03MTdmLTQ3OTMtOTZmOC1hY2VkYTlkN2UyMjciLCJyb2xlIjoiIn0.QGg-1ZVdBArdeiPlAfEAygKQSqPVwV-ErwXxRt6UEoM'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.PrediccionMaritimaApi(swagger_client.ApiClient(configuration))
area = '1' # str |  | Código | Área de Alta Mar | |----------|----------| | 0 | Océano Atlántico al sur de 35º N   | | 1  | Océano Atlántico al norte de 30º N   | | 2  | Mar Mediterráneo

# create an instance of the API class
api_instance = swagger_client.PrediccionMaritimaApi(swagger_client.ApiClient(configuration))
costa = '41' # str |  | Código | Área Costera | |----------|----------| | 42 | Costa de Andalucía Occidental y Ceuta   | | 47  | Costa de Andalucía Oriental y Melilla   | | 41  | Costa de Asturias, Cantabria y País Vasco  | | 45  | Costa de Cataluña   | | 40  | Costa de Galicia   | | 44  | Costa de Illes Balears   | | 43  | Costa de las Islas Canarias  | | 46  | Costa de Valencia y Murcia

try:
    # Predicción marítima de alta mar.
    api_response = api_instance.prediccin_martima_de_alta_mar_(area)
    pprint(api_response)
    
except ApiException as e:
    print("Exception when calling PrediccionMaritimaApi->prediccin_martima_de_alta_mar_: %s\n" % e)

response = requests.get(api_response.datos)  
#response.content
alta_mar = response.content.decode(encoding="windows-1252")
boletin = json.loads(alta_mar)[0]

prediccion_cantabrico = """
BOLETÍN METEOROLÓGICO PARA ALTA MAR
INICIO :{}
FIN    :{}
{}
{}
""".format(
    boletin["situacion"]["inicio"],
    boletin["situacion"]["fin"],
    boletin["prediccion"]["zona"][8]["nombre"],
    boletin["prediccion"]["zona"][8]["texto"]
          )





try:
    # Predicción marítima costera.
    api_response = api_instance.prediccin_martima_costera_(costa)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrediccionMaritimaApi->prediccin_martima_costera_: %s\n" % e)

response = requests.get(api_response.datos)
#response.content
aguas_costeras = response.content.decode(encoding="windows-1252")

#aguas_costeras

boletin_costero = json.loads(aguas_costeras)[0]

prediccion_cantabrico="""
BOLETÍN METEOROLÓGICO PARA AGUAS COSTERAS
INICIO :{}
FIN    :{}
{}
{}
""".format(
    boletin_costero["situacion"]["inicio"],
    boletin_costero["situacion"]["fin"],
    boletin_costero["prediccion"]["zona"][1]["subzona"]["nombre"].upper(),
    boletin_costero["prediccion"]["zona"][1]["subzona"]["texto"].upper()
)

print(prediccion_cantabrico)
print(prediccion_cantabrico)