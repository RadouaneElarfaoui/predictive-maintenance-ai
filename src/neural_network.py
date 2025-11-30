from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

def train_evaluate_neural_network(X_train, X_test, y_train, y_test):
    """
    Entraîne et évalue un réseau de neurones (MLP).
    Équivalent à 'fitnet' ou 'patternnet' de MATLAB.
    """
    print("   -> Initialisation du Réseau de Neurones (MLP)...")
    # MLPClassifier : Multi-Layer Perceptron
    # hidden_layer_sizes=(100, 50) : 2 couches cachées de 100 et 50 neurones
    # max_iter=500 : Nombre max d'itérations pour l'entraînement
    model = MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=500, random_state=42)
    
    print("   -> Entraînement du modèle (ça peut prendre quelques secondes)...")
    model.fit(X_train, y_train)
    
    print("   -> Prédiction sur les données de test...")
    y_pred = model.predict(X_test)
    
    # Évaluation
    acc = accuracy_score(y_test, y_pred)
    print(f"   -> Résultats :")
    print(f"      Précision (Accuracy): {acc:.4f} ({acc*100:.2f}%)")
    
    print("      Rapport de classification :")
    print(classification_report(y_test, y_pred))
    
    return model, y_pred

def plot_confusion_matrix(y_test, y_pred):
    """
    Affiche la matrice de confusion pour voir les erreurs.
    """
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False)
    plt.xlabel('Prédit')
    plt.ylabel('Réel')
    plt.title('Matrice de Confusion (0=OK, 1=Panne)')
    
    # Sauvegarder le graphique
    plt.savefig('confusion_matrix.png')
    print("   -> Matrice de confusion sauvegardée sous 'confusion_matrix.png'")
    # plt.show()
