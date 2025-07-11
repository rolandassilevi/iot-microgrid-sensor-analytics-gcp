
# Microgrid IoT Sensor Analytics 

## Réseau de Capteurs pour Evaluation de risques et Optimisation de la Résilience de Micro-réseau d'énergie renouvelable
## Sensor Network risks assessment and Renewable energy Microgrid Resilience Optimisation

**Auteur / Author :** Roland Assilevi

**Dernière mise à jour / Last updated :** Juillet / July 2025 

**Tags :** IoT, Microgrid, Analyse de données / Data Analysis, Google Colab, Power BI, Machine Learning, Résilience / Resilience, Réseau de capteurs / Sensor Network


---

## 🎯 Objectif du projet / Project Objective

Collecter les données de capteurs IoT dans un micro-réseau intelligent pour analyse, détection d'anomalies; les transformer en vecteur pour évaluer les risques et optimiser la résilience via le Machine Learning.

Collect IoT sensor data in a smart microgrid for analysis and anomaly detection; transform it into vectors to assess risks and optimize resilience through Machine Learning

---

## 🧠 Intégration Google Cloud SQL / Google Cloud SQL Integration

Les données de capteurs sont migrées vers une base de données Google Cloud SQL (PostgreSQL ou MySQL), utilisée comme source principale pour les notebooks Python et les tableaux de bord (Power BI, Looker Studio).

Sensors' data is migrated to a Google Cloud SQL database (PostgreSQL or MySQL), used as the main data source for Python notebooks and dashboards (Power BI, Looker Studio).

- 📁 `/cloud/sql/schema.sql` : définition des tables capteurs
- 🐍 Intégration Python via `SQLAlchemy` ou `google-cloud-sql-python-connector`
- 📊 Connexion Power BI via connecteur PostgreSQL ou ODBC

---

## 📊 1. Tableau de bord interactif / Interactive Dashboard

**FR :**  
Visualisation de données d’un microgrid (tension, courant, température, production du panneau solaire photovoltaïque, etc.) avec Power BI et Looker Studio.

**EN :**  
Visualization of microgrid data (voltage, current, temperature, production of photovoltaic solar pannel, etc.) using Power BI and Looker Studio.



---

## 📈 2. Analyse statistique / Statistical Analysis

**FR :**  
Méthodes statistiques : moyenne, écart-type, Z-score, détection de dérive temporelle, corrélations.

**EN :**  
Statistical methods: mean, standard deviation, Z-score, time-drift detection, correlation analysis.

➡️ `notebook/1_statistical_analysis.ipynb`

---

## ☁️ 3. Vectorisation du réseau de capteurs – Google Colab / Sensor Network Vectorization – Google Colab

**FR :**  
Transformation des valeurs en vecteurs d’état des capteurs. Possibilité de les convertir en matrice d’adjacence pour modèles GNN.

**EN :**  
Transformation of sensor values into state vectors. Optionally converted into adjacency matrix for GNN models.

➡️ Colab: `vectorization_colab.ipynb`

---

## ⚠️ 4. Évaluation des risques / Risk Evaluation Framework

**FR :**  
Calcul du niveau de risque, de l’impact estimé, et des indices de vulnérabilité/résilience.

**EN :**  
Calculates risk level, estimated impact, vulnerability/resilience indices.

➡️ `notebook/2_risk_evaluation.ipynb`

---

## 🤖 5. Tests de modèles ML / DL / Machine Learning & Deep Learning Tests

| Modèle / Model        | Tâche / Task                  | Métrique / Metric      |
|-----------------------|-------------------------------|------------------------|
| Régression logistique | Détection binaire de panne    | Accuracy, F1-score     |
| Random Forest         | Classification multi-label    | Precision@k            |
| LSTM                  | Anomalies séries temporelles  | ROC-AUC, RMSE          |
| Autoencoder           | Anomalie non supervisée       | Reconstruction error   |
| GNN (optionnel)       | Analyse de propagation        | Node classification    |

➡️ `notebook/3_ml_models.ipynb`

---

## 📁 Structure du dépôt / Folder Structure

```
iot-microgrid-sensor-analytics-gcp/
├── cloud/
│   └── sql/
│       ├── schema.sql
│       ├── seed_data.sql
│       └── connection_config.json
├── data/
│   └── README.md
├── notebooks/
│   ├── 1_statistical_analysis.ipynb
│   ├── 2_risk_evaluation.ipynb
│   ├── 3_ml_models.ipynb
│   └── 4_gcp_sql_integration.ipynb
├── colab/
│   └── sensor_vectorization_colab.ipynb
├── dashboard/
│   ├── microgrid_dashboard.pbix
│   ├── dashboard_lookerstudio.pdf
│   └── README.md
├── README.md
├── requirements.txt
└── .env.example
```

---

## ▶️ Utilisation / How to Use

1. Cloner le repo / Clone the repo  
   `git clone https://github.com/rolandassilevi/iot-microgrid-sensor-analytics-gcp.git`

2. Configurer la connexion Cloud SQL  
   Setup connection to Cloud SQL

3. Exécuter les notebooks  
   Run the notebooks

4. Visualiser dans Power BI ou Looker  
   Visualize results in Power BI or Looker Studio

---

## 🧠 Contexte & Impact / Context & Impact

**FR :**  
Ce projet s’inscrit dans une approche jumeau numérique pour microgrids. Il peut évoluer vers de la maintenance prédictive ou du scoring de résilience en temps réel.

**EN :**  
This project simulates a digital twin approach for microgrids. It can evolve into predictive maintenance and real-time resilience scoring.

---

## 📬 Contact

Pour toute question ou collaboration / For questions or collaboration: [LinkedIn](https://linkedin.com/in/rolandassilevi)
