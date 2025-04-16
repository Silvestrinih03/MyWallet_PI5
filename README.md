# 💰 **MyWallet - Projeto-Integrador-5**
**SUA PLATAFORMA DE GESTÃO FINANCEIRA PESSOAL**

---

## 👥 **Integrantes do grupo**
- Bruno Tasso Savoia RA: 22000354
- Gabriel Padreca Nicoletti RA: 20013009
- Vitor Hugo Amaro Aristides RA: 20018040
- Luan de Campos Ferreira RA: 23005247
- Nicole Silvestrini Garrio RA: 23009486

---

## 🚀 Como rodar o projeto

### ✅ Pré-requisitos
- Docker Desktop instalado e em execução

### 🧭 Passo a passo
1. Abra o Docker Desktop
2. Clone o repositório ou baixe o projeto

### ▶️ Rodar aplicação
**docker-compose up --build**

### 🛑 Parar a aplicação
**docker-compose down**

### 🌐 Acessando a aplicação
- API simples: http://localhost:8000/hello
- Documentação da API (Swagger UI): http://localhost:8000/docs
- Documentação da API (Redoc): http://localhost:8000/redoc

---

### 📂 Estrutura do projeto
MyWallet/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
│
└── docker-compose.yml