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


""" 
pprint(alta_mar)
boletin.keys()
boletin["situacion"].keys()
boletin["situacion"]["inicio"]
boletin["situacion"]["fin"]
boletin["situacion"]["texto"]
boletin["prediccion"].keys()
boletin["prediccion"]["zona"][8]
 """


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


print(prediccion_cantabrico)