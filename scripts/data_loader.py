import pandas as pd
import os

# Ruta absoluta de la carpeta dond e se encuentra este script (...../scripts/data_loader.py
SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))

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
    