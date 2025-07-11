import pandas as pd
from pathlib import Path

# === Définir les chemins ===
input_path = Path("raw-data/inverter.csv")
output_path = Path("clean-data/inverter_cleaned.csv")
output_path.parent.mkdir(parents=True, exist_ok=True)

# === Charger le CSV ===
df = pd.read_csv(input_path)

# === Convertir la colonne TIMESTAMP en format ISO ===
df["TIMESTAMP"] = pd.to_datetime(df["TIMESTAMP"], dayfirst=True)

# === Supprimer les colonnes redondantes ===
cols_to_drop = ["DATE", "ANNEE", "MOIS", "JOUR", "HEURE"]
df.drop(columns=[col for col in cols_to_drop if col in df.columns], inplace=True)

# === Réorganiser les colonnes (optionnel) ===
cols = ["TIMESTAMP"] + [col for col in df.columns if col != "TIMESTAMP"]
df = df[cols]

# === Sauvegarder le fichier nettoyé ===
df.to_csv(output_path, index=False)

print(f"✅ Données nettoyées et sauvegardées dans : {output_path}")

