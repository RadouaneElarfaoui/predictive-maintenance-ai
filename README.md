# Projet de Maintenance Prédictive (AI in Mécanique)

Ce projet applique des techniques d'Intelligence Artificielle au domaine de l'ingénierie mécanique pour prédire les pannes de machines. Il utilise Python et ses bibliothèques scientifiques, offrant une alternative moderne aux outils MATLAB (`fitnet`).

## 🎯 Objectif
L'objectif principal est de développer un modèle capable d'anticiper les défaillances d'équipements industriels en analysant les données de capteurs (température, vitesse de rotation, couple, usure de l'outil).

## 🛠️ Outils & Comparaison MATLAB

Nous utilisons l'écosystème Python Data Science :

| Concept | Équivalent MATLAB | Équivalent Python (Ce projet) | Description |
| :--- | :--- | :--- | :--- |
| **Langage** | MATLAB | **Python** | Langage standard en Data Science et Industrie 4.0. |
| **Données** | Matrices / Tables | **Pandas & NumPy** | Manipulation puissante de données tabulaires. |
| **Réseaux de Neurones** | `fitnet` / `nntool` | **Scikit-learn `MLPClassifier`** | Création de modèles prédictifs complexes (Deep Learning simple). |
| **Visualisation** | `plot` | **Matplotlib / Seaborn** | Tracé de graphiques et analyse visuelle. |

## 🧠 Tâche du Projet : Réseau de Neurones (Maintenance Prédictive)

*   **But :** Prédire le risque de panne (`Machine failure`).
*   **Méthode :** Entraîner un Perceptron Multicouche (MLP) sur l'ensemble des capteurs pour classifier l'état de la machine (0 = OK, 1 = Panne).
*   **Intérêt :** Détecter des modèles complexes non visibles par une simple régression.

## 🚀 Comment exécuter le projet

1.  **Installation des dépendances :**
    ```bash
    pip install pandas numpy scikit-learn matplotlib seaborn
    ```

2.  **Lancer l'analyse Python :**
    ```bash
    python main.py
    ```

3.  **Lancer l'analyse MATLAB :**
    *   Ouvrez MATLAB.
    *   Ouvrez le fichier `main.m`.
    *   Cliquez sur **Run**.

## 📂 Structure des Fichiers
*   `src/` : Code source Python.
*   `main.py` : Script principal Python.
*   `main.m` : Script principal MATLAB (Équivalent).

