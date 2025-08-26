import requests

def main():
    print("=== Sum Client (FastAPI) ===")
    print("Enter two numbers to calculate their sum.\n")

    try:
        a = int(input("👉 Enter the first number (a): "))
        b = int(input("👉 Enter the second number (b): "))
    except ValueError:
        print("⚠️ Please enter valid integers only.")
        return

    url = "http://127.0.0.1:8000/sum"
    payload = {"a": a, "b": b}

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            data = response.json()
            print(f"\n✅ The sum of {a} + {b} = {data['sum']}")
        else:
            print("❌ Server error:", response.text)
    except requests.exceptions.ConnectionError:
        print("⚠️ Could not connect to the server. Make sure it is running.")

if __name__ == "__main__":
    main()
