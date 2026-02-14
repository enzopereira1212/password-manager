from core.crypto import criar_fernet
from getpass import getpass
from cryptography.fernet import InvalidToken
from ui.banner import mostrar_banner

mostrar_banner()

# pede a senha mestre
senha_mestra = getpass("Digite a senha mestra: ")

# cria o sistema de criptografia
fernet = criar_fernet(senha_mestra)

# valida a senha mestre
try:
    with open("data/senhas.txt", "rb") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if linha:
                partes = linha.split(b":")
                if len(partes) == 2:
                    fernet.decrypt(partes[1])
                    break
except FileNotFoundError:
    pass
except InvalidToken:
    print("Senha mestre incorreta!")
    exit()

print("Acesso permitido")

def deletar_senha(fernet):
    try:
        with open("data/senhas.txt", "rb") as arquivo:
            linhas = arquivo.readlines()

        registros = []

        for linha in linhas:
            linha = linha.strip()
            if not linha:
                continue

            partes = linha.split(b":")

            if len(partes) != 2:
                continue

            site, senha_cripto = partes
            senha = fernet.decrypt(senha_cripto).decode()
            registros.append((site.decode(), senha))

        if not registros:
            print("Nenhuma senha salva.")
            return

        print("\nSenhas salvas:")
        for i, (site, _) in enumerate(registros):
            print(f"{i+1} - {site}")

        escolha = int(input("Qual deseja deletar? ")) - 1

        if escolha < 0 or escolha >= len(registros):
            print("Opção inválida")
            return

        registros.pop(escolha)

        with open("data/senhas.txt", "wb") as arquivo:
            for site, senha in registros:
                linha = (
                    site.encode()
                    + b":"
                    + fernet.encrypt(senha.encode())
                    + b"\n"
                )
                arquivo.write(linha)

        print("Senha deletada!")

    except FileNotFoundError:
        print("Nenhuma senha salva ainda")

#menu
while True:
    print("\n1 - adicionar senha")
    print("2 - ver senhas")
    print("3 - apagar senha")
    print("4 - sair")

    opcao = input("escolha: ")

    # ---------------------
    # 1 - ADICIONAR SENHA
    # ---------------------
    if opcao == "1":
        site = input("Site: ")
        senha_site = input("Senha: ")

        senha_criptografada = fernet.encrypt(
            senha_site.encode()
        )

        with open("data/senhas.txt", "ab") as arquivo:
            linha = site.encode() + b":" + senha_criptografada + b"\n"
            arquivo.write(linha)

        print("senha salva")

    # -----------
    # 2 - VER SENHAS
    # -----------
    elif opcao == "2":
        try:
            with open("data/senhas.txt", "rb") as arquivo:
                for linha in arquivo:
                    linha = linha.strip()

                    if not linha:
                        continue

                    partes = linha.split(b":")

                    if len(partes) != 2:
                        continue

                    site, senha_cripto = partes

                    senha_original = fernet.decrypt(
                        senha_cripto
                    ).decode()

                    print(f"{site.decode()} -> {senha_original}")

        except FileNotFoundError:
            print("Nenhuma senha salva ainda")


    # ----------
    # 3 - apagar senha
    # ----------
    elif opcao == "3":
        deletar_senha(fernet)

    # -----------------
    # 4 - sair
    # -----------------
    elif opcao == "4":
        print("Saindo")
        break

    else:
        print("Opção invalida")