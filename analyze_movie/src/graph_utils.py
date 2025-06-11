import matplotlib.pyplot as plt

def display_predic_diff_error(y_test, predictions):
    plt.figure(figsize=(12, 6))
    plt.plot(range(20), y_test[:20], label='Valeur réelle', marker='o')
    plt.plot(range(20), predictions[:20], label='Prédiction', marker='x')
    plt.title("Erreurs")
    plt.xlabel("Index dans l'ensemble de test")
    plt.ylabel("Ticket Vendu")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()