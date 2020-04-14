import pandas as pd
import glob
mylist = [f for f in glob.glob("*.csv")]
mylist
print("""

ARCHIVOS .csv EN ESTE DIRECTORIO

""")
for item in mylist:
    print("-   {}".format(item))
input("""

ENTER PARA CONTINUAR

""")

def leer_csv_ais(archivo):
    df = pd.read_csv(archivo,sep=";",decimal=",",encoding="windows-1252",parse_dates=["Timestamp"])
    df.to_csv("TIME_MANAGER_"+archivo)



for item in mylist:
    try:
        leer_csv_ais(item)
        print("PROCESADO  FILE {} => TIME_MANAGER_{}   ".format(item,item))
    except:
        print("FILE {}           =>  NO PROCESADO".format(item))
      


input("""

ENTER PARA FINALIZAR

""")

