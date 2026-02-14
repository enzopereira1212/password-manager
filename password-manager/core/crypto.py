from cryptography.fernet import Fernet
import base64
import hashlib

def gerar_chave_da_senha(senha):
    #transforma senha em hash
    hash_senha = hashlib.sha256(senha.encode()).digest()

    #converte para formato aceito pelo fernet
    chave = base64.urlsafe_b64encode(hash_senha)

    return chave

def criar_fernet(senha):
    chave = gerar_chave_da_senha(senha)
    return Fernet(chave)