# 📧 NLP Email Classifier (AI-powered)

Aplicação web que utiliza **Inteligência Artificial (OpenAI)** para **classificar emails automaticamente** como **Produtivos** ou **Improdutivos**, simulando um cenário real de uso corporativo no setor financeiro.

O objetivo do projeto é demonstrar a capacidade de estruturar soluções, integrar IA de forma clara e entregar uma aplicação funcional end-to-end.

---

## 🚀 Funcionalidades

- Classificação automática de emails usando IA
- Interface web simples e intuitiva
- Feedback visual de carregamento durante a classificação
- Backend em FastAPI
- Integração segura com OpenAI via variáveis de ambiente
- Deploy em ambiente cloud (Render)

---

## 🧠 Como funciona a classificação

O texto do email enviado pelo usuário é processado por um serviço de IA que analisa o conteúdo e retorna uma classificação baseada em contexto e intenção.

### Exemplos

- **Produtivo:** Emails relacionados a finanças, contratos, pagamentos, relatórios ou decisões estratégicas
- **Improdutivo:** Emails informais, mensagens pessoais ou sem impacto direto nos processos da empresa

---

## 🛠️ Tecnologias Utilizadas

### Backend

- Python
- FastAPI
- OpenAI API
- Uvicorn
- Jinja2

### Frontend

- HTML5
- CSS3

### Infraestrutura

- Render (deploy)
- GitHub (versionamento)

---

## 📁 Estrutura do Projeto

nlp-email-classifier/
├── app/
│ ├── main.py
│ ├── service_ai.py
│ ├── templates/
│ │ └── index.html
│ └── static/
│ ├── css/
│ └── img/
├── requirements.txt
├── .gitignore
└── README.md

## ⚙️ Configuração do Ambiente

### 1️⃣ Clonar o repositório

git clone https://github.com/seu-usuario/nlp-email-classifier.git
cd nlp-email-classifier

## 2️⃣ Criar ambiente virtual

python -m venv venv
source venv/bin/activate

## 3️⃣ Instalar dependências

pip install -r requirements.txt

## 4️⃣ Variáveis de ambiente

Crie a variável de ambiente com sua chave da OpenAI:
export OPENAI_API_KEY="sua_api_key_aqui"

## ▶️ Executando o projeto localmente

uvicorn app.main:app --reload

Acesse:

http://127.0.0.1:8000
