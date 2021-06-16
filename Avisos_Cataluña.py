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
api_instance = swagger_client.AvisosCapApi(swagger_client.ApiClient(configuration))
area = '69' # str |  | Código | Área | |----------|----------| | esp  | España| | 61  | Andalucía   | | 62  | Aragón   | | 63  | Asturias, Principado de  | | 64  | Ballears, Illes   | | 78  | Ceuta   | | 65  | Canarias   | | 66  | Cantabria   | | 67  | Castilla y León   | | 68  | Castilla - La Mancha   | | 69  | Cataluña   | | 77  | Comunitat Valenciana   | | 70  | Extremadura   | | 71  | Galicia   | | 72  | Madrid, Comunidad de    | | 79  | Melilla   | | 73  | Murcia, Región de   | | 74  | Navarra, Comunidad Foral de   | | 75  | País Vasco | | 76  | Rioja, La

try:
    # Avisos de Fenómenos Meteorológicos Adversos. Último.
    api_response = api_instance.avisos_de_fenmenos_meteorolgicos_adversos__ltimo_(area)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvisosCapApi->avisos_de_fenmenos_meteorolgicos_adversos__ltimo_: %s\n" % e)

response = requests.get(api_response.datos)
#print(response.content)
FF_AA = response.content.decode(encoding="windows-1252")
#print(FF_AA)

boletin = json.loads(FF_AA)[0]
print(boletin)

FF_MM_AA = """
{}
{}
""".format(
    boletin["area"][8]["areaDesc"],
    boletin["area"][8]["polygon"]
          )

print(FF_MM_AA)