import pandas as pd
import os

# Ruta absoluta de la carpeta donde se encuentra este script (.../scripts/data_loader.py)
SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))

# Ruta al archivo CSV dentro de la carpeta data
DATA_PATH = os.path.join(SCRIPTS_DIR, "..", "data", "games.csv")

def cargar_datos(path):
    print(f"Cargando datos desde: {path}...")
    try:
        df = pd.read_csv(path)
        print("Datos cargados exitosamente.")
        return df
    except FileNotFoundError:
        print(f"Error: El archivo {path} no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al cargar los datos: {e}")
        return None

if __name__ == "__main__":
    print(f"Iniciando el proceso de carga de datos... : {os.path.abspath(__file__)}")

    # Llamamos a la función para cargar los datos
    dataframe_juegos = cargar_datos(DATA_PATH)

    if dataframe_juegos is not None:
        print("\n--Primeras 5 filas del DataFrame--")
        print(dataframe_juegos.head())

        print("\n--Información del DataFrame--")
        print(dataframe_juegos.info())

         
         
         