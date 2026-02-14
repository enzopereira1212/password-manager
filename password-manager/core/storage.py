import json
import os

VAULT_FILE = "data/vault.json"


def carregar_senhas():
    """Carrega as senhas do arquivo"""

    if not os.path.exists(VAULT_FILE):
        return {}

    with open(VAULT_FILE, "r") as file:
        return json.load(file)


def salvar_senhas(dados):
    """Salva as senhas no arquivo"""

    with open(VAULT_FILE, "w") as file:
        json.dump(dados, file, indent=4)
