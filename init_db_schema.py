import os
from dotenv import load_dotenv
from google.cloud.sql.connector import Connector
from sqlalchemy import create_engine, text
import pg8000

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
        INSTANCE_CONNECTION_NAME,  # type: ignore
        "pg8000",
        user=DB_USER,
        password=DB_PASSWORD,
        db=DB_NAME
    )

# Créer engine
engine = create_engine("postgresql+pg8000://", creator=getconn)

try:
    with engine.begin() as conn:  # Connexion ouverte ici
        print(f"✅ Connexion à la base de données {DB_NAME} réussie.")

        # Lecture et exécution du fichier SQL
        with open("cloud/sql/schema.sql", "r") as f:
            sql = f.read()
            conn.execute(text(sql))
            print("✅ Script SQL exécuté.")

        # Vérifier si la table a bien été créée
        result = conn.execute(text(
            "SELECT table_name FROM information_schema.tables WHERE table_schema='public';"
        ))
        tables = [row[0] for row in result]
        print("📋 Tables existantes :", tables)

        if "test_solar_data" not in tables:
            raise ValueError("❌ La table 'test_solar_data' n'a pas été trouvée.")

        print("✅ Table 'solar_data' confirmée.")

except Exception as e:
    print(f"❌ Erreur : {e}")

finally:
    connector.close()
    print("🔌 Connecteur fermé.")
