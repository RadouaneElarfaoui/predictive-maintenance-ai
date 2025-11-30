from src.data_loader import load_and_preprocess_data, get_classification_data
import os

# Chemin vers le fichier de données
DATA_PATH = 'machine failure.csv'

def main():
    if not os.path.exists(DATA_PATH):
        print(f"Erreur: Le fichier {DATA_PATH} est introuvable.")
        return

    print("--- 1. Chargement et Nettoyage des Données ---")
    df = load_and_preprocess_data(DATA_PATH)
    print(f"Données chargées avec succès : {df.shape[0]} lignes, {df.shape[1]} colonnes")
    print("Aperçu des premières lignes :")
    print(df.head())



    print("\n--- 3. Préparation des Données pour le Réseau de Neurones (IA) ---")
    X_class_train, X_class_test, y_class_train, y_class_test = get_classification_data(df)
    print(f"Données d'entraînement (Classification) : {X_class_train.shape}")
    print(f"Données de test (Classification) : {X_class_test.shape}")

    # Exécution du Réseau de Neurones
    from src.neural_network import train_evaluate_neural_network, plot_confusion_matrix
    model_nn, y_pred_nn = train_evaluate_neural_network(X_class_train, X_class_test, y_class_train, y_class_test)
    plot_confusion_matrix(y_class_test, y_pred_nn)

    print("\n--- Prêt pour l'entraînement des modèles ! ---")

if __name__ == "__main__":
    main()
