"""Contenu du portfolio - source unique utilisee par l'accueil et la page parcours.
Pour modifier une experience, une competence ou un lien : c'est ici et nulle part ailleurs.
"""

EMAIL = "cisseniang564@gmail.com"
GITHUB = "https://github.com/cisseniang564"
LINKEDIN = "https://www.linkedin.com/in/cisseniang/"

EXPERIENCES = [
    {
        "role": "Consultant Data / Actuariat",
        "org": "La Mutuelle Saint Christophe (Groupe AXA)",
        "when": "Juillet 2024 – aujourd'hui",
        "bullets": [
            "Pilotage du suivi de production : récupération des données externes, intégration dans l'infocentre et création des datamarts.",
            "Responsable du processus de qualité des données.",
            "Cartographie de l'ensemble des données du service Infocentre via SAS et Power BI.",
            "Conception et automatisation de bout en bout du processus de purge et d'anonymisation des données sous SAS.",
            "Développement de programmes SAS dans le cadre de la migration AXAPAC et DABSM (DAB Sur Mesure).",
            "Développement d'un outil d'extraction sous VBA et participation aux travaux de reportings techniques.",
        ],
        "tags": ["SAS", "Power BI", "VBA", "Infocentre", "Datamarts", "Qualité des données"],
    },
    {
        "role": "Data Analyst Technique (CDD)",
        "org": "GAN Assurances",
        "when": "Décembre 2023 – Juillet 2024",
        "bullets": [
            "Automatisation sous SAS des analyses de ventes et des tableaux de bord de résultats techniques mensuels du Marché Pro, diffusés à la Direction Générale et aux autres directions.",
            "Création de datamarts via des requêtes SAS, SQL, Python et R pour répondre aux besoins du métier et du Datalab.",
            "Analyse de la rentabilité et de la sinistralité pour le pilotage de l'activité et des résultats techniques.",
            "Mise à disposition de données et de reportings permettant au marché de suivre l'évolution des risques en portefeuille.",
            "Interlocuteur privilégié du métier sur l'analyse des indicateurs clés (Affaires Nouvelles, Affaires Résiliées, S/P, Majoration) et garant de la qualité des données mises à disposition.",
        ],
        "tags": ["SAS", "SQL", "Python", "R", "Datamart", "Rentabilité", "Sinistralité"],
    },
    {
        "role": "Responsable Technique Actuarielle (CDD)",
        "org": "SwissLife",
        "when": "Janvier 2023 – Août 2023",
        "bullets": [
            "Réalisation des analyses financières (ratios de rentabilité), techniques et actuarielles relatives à la souscription des risques, des reportings mensuels et des audits techniques pour définir les axes d'amélioration par produit (Flotte, Habitation).",
            "Analyse des résultats et des risques détaillés par produit ; pilotage tarifaire.",
            "Pilotage de la structure tarifaire des produits pour maintenir le niveau de rentabilité et atteindre la marge visée.",
            "Participation au processus de l'exercice budgétaire (MTP) et au calcul des SCR (SCR CAT).",
            "Participation au pilotage quotidien de l'enveloppe commerciale des intermédiaires.",
        ],
        "tags": ["Tarification IARD", "Rentabilité", "SCR CAT", "MTP", "Flotte", "Habitation"],
    },
    {
        "role": "Chargé d'études actuarielles (CDD)",
        "org": "La Mutuelle Générale",
        "when": "Janvier 2022 – Décembre 2022",
        "bullets": [
            "Suivi et actualisation des provisions techniques.",
            "Rapprochement des flux de cotisations et de prestations avec la comptabilité.",
            "Établissement et analyse des comptes clients (S/P).",
            "Participation aux travaux d'inventaire sur le portefeuille de contrats collectifs Santé / Prévoyance.",
            "Analyse des résultats et de leur évolution en vue du renouvellement.",
            "Calcul des provisions (PSAP, PM…), des S/P et des CANE pour alimenter les comptes de résultat (méthode Chain-Ladder).",
            "Développement, sous VBA, d'un outil d'analyse des résultats des arrêtés de comptes.",
        ],
        "tags": ["Chain-Ladder", "PSAP", "PM", "CANE", "Santé / Prévoyance", "Inventaire", "VBA"],
    },
    {
        "role": "Chargé d'études actuarielles (stage)",
        "org": "SADA Assurances",
        "when": "Juillet 2021 – Novembre 2021",
        "bullets": [
            "Calcul du SCR Marché (formule standard).",
            "Automatisation de l'outil de pilotage de la gestion des actifs : transposition du fichier Excel existant vers RShiny, avec alimentation directe depuis le datamart.",
            "Automatisation et sécurisation de l'alimentation de plusieurs processus du pilier 1 de la réglementation Solvabilité II.",
            ("Calcul des exigences quantitatives de fonds propres au titre des piliers 1 et 2 de la directive Solvabilité II :", [
                "fichier Best Estimate ;",
                "QRT non pris en charge par le modèle Addactis (par exemple le QRT S.19.01) ;",
                "taux de cession en réassurance (par LoB et par année de survenance).",
            ]),
            "Suivi des placements et de la réassurance.",
            "Travaux sur les provisionnements.",
        ],
        "tags": ["RShiny", "Excel / VBA", "SQL", "Addactis Modeling", "Addactis DataFlow", "Addactis One", "ResQ", "SCR Marché", "QRT S.19.01"],
    },
]

FORMATIONS = [
    {
        "role": "Master 2 Actuariat & DU Big Data – Data Science sous Python (double diplôme)",
        "org": "Université de Montpellier",
        "when": "2020 – 2021",
        "bullets": [
            "Introduction à l'intelligence artificielle.",
            "Études actuarielles, techniques de tarification et de provisionnement.",
            "Calibration de modèles statistiques (GLM).",
        ],
        "tags": ["Actuariat", "Python", "GLM", "Big Data"],
    },
    {
        "role": "Master Expertise Statistique",
        "org": "Université de Lorraine",
        "when": "2019 – 2020",
        "bullets": [
            "Analyse de données approfondie.",
            "Techniques de régression et de segmentation.",
            "Programmation avancée en R, VBA et SAS.",
        ],
        "tags": ["Statistiques", "R", "VBA", "SAS"],
    },
]

CERTIFICATIONS = [
    "Spécialiste certifié SAS",
    "Machine Learning avec Python — Udemy",
    "SQL using SAS — Coursera",
    "SAS Macro Language — Coursera",
    "Analyse de données multidimensionnelles sous R",
]

COMPETENCES = [
    ("Actuariat", ["Provisionnement (Chain-Ladder, Bootstrap)", "Tarification IARD", "Réassurance",
                    "Inventaire Santé / Prévoyance", "Pilotage technique"]),
    ("Solvabilité II", ["Best Estimate", "SCR (marché, CAT)", "QRT (dont S.19.01)", "Piliers 1 et 2"]),
    ("Outils actuariels", ["Addactis Modeling", "Addactis DataFlow", "Addactis One", "Addactis IBNRs", "ResQ"]),
    ("Data & langages", ["SAS (certifié)", "SQL", "Python", "R", "VBA", "Stata"]),
    ("Machine learning", ["scikit-learn", "XGBoost", "pandas", "NumPy", "Keras", "TensorFlow", "PyTorch"]),
    ("BI & applications", ["Power BI", "RShiny", "Streamlit", "MySQL", "Excel avancé"]),
]
