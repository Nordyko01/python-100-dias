"""import json
from pathlib import Path

FILENAME = Path("users.json")


def load_users():
    if FILENAME.exists():
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_users(users):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=2)


def main():
    # lê os dados guardados (ou cria dicionário vazio)
    users = load_users()

    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha de admin: ")

    # adiciona/actualiza utilizador
    users[nome] = senha
    save_users(users)

    print("Usuários armazenados:", users)


if __name__ == "__main__":
    main()"""
