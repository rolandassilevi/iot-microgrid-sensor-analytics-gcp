import os
from dotenv import load_dotenv
from google.cloud.sql.connector import Connector
from sqlalchemy import create_engine
import pandas as pd

# Charger les variables d'environnement
if not os.path.exists(".env"):
    raise FileNotFoundError("❌ .env file not found. Please create one from .env.example.")
load_dotenv()

# Variables
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
INSTANCE_CONNECTION_NAME = os.getenv("INSTANCE_CONNECTION_NAME")

if not INSTANCE_CONNECTION_NAME:
    raise ValueError("❌ INSTANCE_CONNECTION_NAME is not set.")

# Initialiser le connecteur
connector = Connector()

def getconn():
    return connector.connect(
        INSTANCE_CONNECTION_NAME, # type: ignore
        "pg8000",
        user=DB_USER,
        password=DB_PASSWORD,
        db=DB_NAME
    )

# Créer engine SQLAlchemy
engine = create_engine("postgresql+pg8000://", creator=getconn)

try:
    # Lire le fichier CSV
    csv_path = "clean-data/inverter_cleaned.csv"
    print(f"📄 Chargement du fichier : {csv_path}")
    df = pd.read_csv(csv_path, parse_dates=["TIMESTAMP"])
    
    # Nettoyer les colonnes
    df.columns = df.columns.str.strip().str.lower() #.str.strip() Supprime les espaces vides au début et à la fin de chaque nom de colonne. Exemple : " PV1 " devient "PV1" # .str.lower() Convertit tous les noms de colonnes en minuscules. Exemple : "PV1" devient "pv1"

    # Renommer la colonne si nécessaire
    if "TIMESTAMP" in df.columns:
        df.rename(columns={"TIMESTAMP": "timestamp"}, inplace=True)
        
    # Renommer TIMESTAMP si besoin
    if "timestamp" not in df.columns and "timestamp" in df.columns.str.upper():
        df.rename(columns={"timestamp": "timestamp"}, inplace=True)



    # Insérer dans la base
    with engine.begin() as conn:
        df.to_sql("solar_data", con=conn, if_exists="append", index=False)
        print(f"✅ {len(df)} lignes insérées dans la table 'solar_data'.")

except Exception as e:
    print(f"❌ Erreur : {e}")

finally:
    connector.close()
    print("🔌 Connecteur fermé.")
