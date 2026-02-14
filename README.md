# Password Manager feito em Python

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Study%20Project-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

Um gerenciador de senhas simples desenvolvido em Python com foco em aprendizado de criptografia, organização de código e fundamentos de cibersegurança.

---

## Sobre o Projeto

Este projeto foi criado para estudar conceitos importantes de segurança digital:

- Criptografia simétrica (Fernet / AES)
- Derivação de chave a partir de senha mestra
- Armazenamento seguro de dados
- Organização modular em Python
- Boas práticas de projetos no GitHub

O sistema funciona totalmente no terminal.

---

## Funcionalidades

- 🔐 Login com senha mestra
- 🔒 Criptografia automática das senhas
- 🔓 Descriptografia somente com senha correta
- 📁 Armazenamento local seguro
- 🧱 Código organizado em módulos

---

## Estrutura do Projeto

```
password-manager/
│
├── main.py
├── core/
│   └── crypto.py
├── ui/
│   └── banner.py
└── data/
    └── senhas.txt
```

---

## Como Executar

1. Clone o repositório:

```
git clone https://github.com/enzopereira1212/password-manager.git
```

2. Entre na pasta:

```
cd password-manager
```

3. Instale as dependências:

```
pip install cryptography
```

4. Execute:

```
python main.py
```

---

## ⚠️ Aviso

Este projeto foi desenvolvido **apenas para fins educacionais**.

Não utilize este código para armazenar dados sensíveis reais sem melhorias adicionais de segurança.

---

## 👨‍💻 Autor

Desenvolvido por **Enzo Pereira**

---

## 📜 Licença

Este projeto está sob a licença MIT.
