import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def load_and_preprocess_data(filepath):
    """
    Charge le fichier CSV et effectue le nettoyage de base.
    """
    # Charger les données
    df = pd.read_csv(filepath)
    
    # Supprimer les colonnes inutiles pour l'analyse
    # UDI: identifiant unique sans valeur prédictive
    # Product ID: identifiant string
    if 'UDI' in df.columns:
        df = df.drop(['UDI'], axis=1)
    if 'Product ID' in df.columns:
        df = df.drop(['Product ID'], axis=1)
    
    # Encoder la colonne 'Type' (L, M, H) en valeurs numériques
    if 'Type' in df.columns:
        le = LabelEncoder()
        df['Type'] = le.fit_transform(df['Type'])
    
    return df



def get_classification_data(df):
    """
    Prépare les données pour le Réseau de Neurones (Classification).
    Objectif : Prédire 'Machine failure'
    """
    # On retire la cible et les indicateurs de panne spécifiques (qui sont des réponses, pas des entrées)
    drop_cols = ['Machine failure', 'TWF', 'HDF', 'PWF', 'OSF', 'RNF']
    
    # On garde tout le reste comme features
    X = df.drop(drop_cols, axis=1)
    y = df['Machine failure']
    
    return train_test_split(X, y, test_size=0.3, random_state=42)
