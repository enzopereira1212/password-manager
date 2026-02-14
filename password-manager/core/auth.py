import os
import hashlib

ARQUIVO_SENHA = "master.hash"

def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def verificar_ou_criar(senha):
    if not os.path.exists(ARQUIVO_SENHA):
        with open(ARQUIVO_SENHA, "w") as f:
            f.write(hash_senha(senha))
        return True
    with open(ARQUIVO_SENHA, "r") as f:
        salva = f.read()

        return salva == hash_senha(senha)