import Helpers as AUX
import pandas as pd

import warnings
warnings.simplefilter("ignore")
print("Elimininar Carpeta B1_Output_Params si existe, antes de ejecutar este script")
# TODO: fix

libro=AUX.LeerExcel("ScenariosChanges.xlsx")
listaHojas=AUX.ListaHojas(libro)

# Hoja del InputActivityRatio

hoja1=AUX.LeerHoja2(libro, listaHojas[0], 0)
encab=AUX.LeerHeaders(hoja1)
years=AUX.LeerCol(hoja1, encab[0])
for i in range(1,len(encab)):
     df_Energy_output = pd.read_csv("A2_Output_Params/"+encab[i].split(";")[2]+"/InputActivityRatio.csv", index_col=None, header=0, low_memory=False)
     lista1=list(df_Energy_output.columns)
     #print(lista1)
     col=AUX.LeerCol(hoja1,encab[i])
     dic=dict(zip(years,col))
     for j in range(len(df_Energy_output)):
         if df_Energy_output["TECHNOLOGY"][j]==encab[i].split(";")[0] and df_Energy_output["FUEL"][j]==encab[i].split(";")[1]:
             df_Energy_output["Value"][j]=dic[df_Energy_output["YEAR"][j]]
    
     df_Energy_output.to_csv("A2_Output_Params/"+encab[i].split(";")[2]+"/InputActivityRatio.csv", index = None, header=True)
     
     
# Hoja del Variable Cost

hoja1=AUX.LeerHoja2(libro, listaHojas[1], 0)
encab=AUX.LeerHeaders(hoja1)
years=AUX.LeerCol(hoja1, encab[0])
for i in range(1,len(encab)):
     df_Energy_output = pd.read_csv("A2_Output_Params/"+encab[i].split(";")[1]+"/VariableCost.csv", index_col=None, header=0, low_memory=False)
     lista1=list(df_Energy_output.columns)
     #print(lista1)
     col=AUX.LeerCol(hoja1,encab[i])
     dic=dict(zip(years,col))
     for j in range(len(df_Energy_output)):
         if df_Energy_output["TECHNOLOGY"][j]==encab[i].split(";")[0]:
             df_Energy_output["Value"][j]=dic[df_Energy_output["YEAR"][j]]
    
     df_Energy_output.to_csv("A2_Output_Params/"+encab[i].split(";")[1]+"/VariableCost.csv", index = None, header=True)
     
     
# Hoja del EmissionsPenalty

hoja1=AUX.LeerHoja2(libro, listaHojas[2], 0)
encab=AUX.LeerHeaders(hoja1)
years=AUX.LeerCol(hoja1, encab[0])
for i in range(1,len(encab)):
    df_Energy_output = pd.read_csv("A2_Output_Params/"+encab[i].split(";")[1]+"/EmissionsPenalty.csv", index_col=None, header=0, low_memory=False)
    
    lista1=list(df_Energy_output.columns)
    # print(lista1)
    # print(len(df_Energy_output))
    col=AUX.LeerCol(hoja1,encab[i])
    dic=dict(zip(years,col))
    for j in range(len(years)):
        listaAux=['EmissionsPenalty',encab[i].split(";")[1],'ECU','','',encab[i].split(";")[0],'',years[j],'','','','','',dic[years[j]]]
        df_Energy_output.loc[len(df_Energy_output)] = listaAux
    
    df_Energy_output = df_Energy_output.drop_duplicates(subset = ['EMISSION','YEAR'],keep = 'last')
    df_Energy_output.to_csv("A2_Output_Params/"+encab[i].split(";")[1]+"/EmissionsPenalty.csv", index = None, header=True)
    
# Hoja de RED

hoja1=AUX.LeerHoja2(libro, listaHojas[3], 0)
encab=AUX.LeerHeaders(hoja1)
years=AUX.LeerCol(hoja1, encab[0])

for i in range(1,len(encab)):
    archivo_csv = "A2_Output_Params/"+encab[i].split(";")[2]+"/"+encab[i].split(";")[1]+".csv"
    
    df_Energy_output = pd.read_csv(archivo_csv, index_col=None, header=0, low_memory=False)
    
    print(f"Procesando: {archivo_csv}")
    print(f"Filas en archivo: {len(df_Energy_output)}")
    print(f"Columnas: {list(df_Energy_output.columns)}")
    if len(df_Energy_output) > 0:
        print(f"Primera fila: {df_Energy_output.iloc[0].to_dict()}")
    else:
        print("ARCHIVO VACÍO")
    
    col=AUX.LeerCol(hoja1,encab[i])
    dic=dict(zip(years,col))
    
    tecnologia_buscada = encab[i].split(";")[0]
    filas_encontradas = 0
    
    for j in range(len(df_Energy_output)):
        if df_Energy_output["TECHNOLOGY"][j]==tecnologia_buscada:
            filas_encontradas += 1
            valor_actual = df_Energy_output["Value"][j]
            factor_reduccion = dic[df_Energy_output["YEAR"][j]]
            df_Energy_output["Value"][j] = round(valor_actual * (1 - factor_reduccion), 4)
    
    print(f"  Tecnología buscada: {tecnologia_buscada}")
    print(f"  Filas encontradas y modificadas: {filas_encontradas}")
    if filas_encontradas == 0:
        print(f"  ADVERTENCIA: No se encontraron filas con TECHNOLOGY='{tecnologia_buscada}' en este archivo")
        tecnologias_en_archivo = df_Energy_output["TECHNOLOGY"].unique()
        print(f"  Tecnologías disponibles en el archivo: {list(tecnologias_en_archivo)}")
    
    df_Energy_output.to_csv(archivo_csv, index = None, header=True)
########################################################################
########### COPIAAMOS CARPETAS DE A2_Outputs_Params a B1_Outputs_Params
########################################################################
        
from shutil import copytree


DIRECTORIO_ORIGEN = "./A2_Output_Params/"
DIRECTORIO_DESTINO = "./B1_Output_Params/"


print("Copiando...")
copytree(DIRECTORIO_ORIGEN, DIRECTORIO_DESTINO)
print("Copiado")

########################################################################