import requests

def main():
    print("=== Client Somme (FastAPI) ===")
    print("Entrez deux nombres pour calculer leur somme.\n")

    try:
        a = int(input("👉 Entrez le premier nombre (a) : "))
        b = int(input("👉 Entrez le deuxième nombre (b) : "))
    except ValueError:
        print("⚠️ Veuillez entrer uniquement des nombres entiers.")
        return

    url = "http://127.0.0.1:8000/sum"
    payload = {"a": a, "b": b}

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            data = response.json()
            print(f"\n✅ La somme de {a} + {b} = {data['sum']}")
        else:
            print("❌ Erreur serveur :", response.text)
    except requests.exceptions.ConnectionError:
        print("⚠️ Impossible de se connecter au serveur. Vérifiez qu'il est bien lancé.")

if __name__ == "__main__":
    main()
