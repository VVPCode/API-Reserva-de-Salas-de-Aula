
# API de Reserva de Salas

Esta é uma API desenvolvida em Flask para gerenciar reservas de salas vinculadas às turmas de uma API de gerenciamento escolar.

## 🔗 Dependência

Esta API depende da API de **Gerenciamento Escolar**, que fornece dados de turmas.

---

## 🚀 Funcionalidades

- ✅ Listar reservas de salas
- ✅ Criar reservas (validação se a turma existe)
- ✅ Integração com a API de gerenciamento de turmas
- ✅ Banco de dados SQLite via SQLAlchemy

---

## 🏗️ Tecnologias e Bibliotecas

- Python 3
- Flask
- Flask-SQLAlchemy
- Requests
- SQLite
- Docker (opcional)

---

## 🗂️ Estrutura de Pastas

```
.
├── app.py
├── controllers/
│   └── reserva_controller.py
├── models/
│   └── reserva.py
├── database.py
├── config.py
├── requirements.txt
└── README.md
```

---

## 🔧 Configuração

### 1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/api-reserva-salas.git
cd api-reserva-salas
```

### 2. Crie o ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências:

```bash
pip install -r requirements.txt
```

### 4. Configure a URL da API de gerenciamento no arquivo `reserva_controller.py`:

```python
API_GERENCIAMENTO_URL = "http://localhost:5000"
```

Ajuste se estiver rodando com Docker (ex: `host.docker.internal` ou nome do serviço no docker-compose).

### 5. Execute a aplicação:

```bash
python app.py
```

---

## 🐳 Executando com Docker

### Build da imagem:

```bash
docker build -t api-reserva-salas .
```

### Execute o container:

```bash
docker run -d -p 5001:5000 --name reserva api-reserva-salas
```

---

## 🔥 Endpoints da API

### ▶️ Listar todas as reservas

- **GET** `/reservas`

**Resposta:**
```json
[
  {
    "id": 1,
    "id_turma": 2,
    "sala": "A101",
    "data_reserva": "2025-05-28",
    "horario": "10:00"
  }
]
```

---

### ▶️ Criar uma reserva

- **POST** `/reservas`

**Corpo da requisição (JSON):**
```json
{
  "id_turma": 1,
  "sala": "A201",
  "data_reserva": "2025-06-01",
  "horario": "14:00"
}
```

**Respostas possíveis:**

- ✅ **201 Created**
```json
{
  "id": 2,
  "id_turma": 1,
  "sala": "A201",
  "data_reserva": "2025-06-01",
  "horario": "14:00"
}
```

- ⚠️ **400 - Dados incompletos**
```json
{
  "erro": "Dados incompletos"
}
```

- ⚠️ **400 - Turma inválida**
```json
{
  "erro": "ID da turma inválido"
}
```

- ❌ **500 - Erro na comunicação**
```json
{
  "erro": "Erro na comunicação com API de gerenciamento"
}
```

---

## 📜 Observações

- Certifique-se de que a API de Gerenciamento Escolar esteja rodando antes de criar reservas, pois ela valida a existência da turma.
- A API é destinada para uso em desenvolvimento e aprendizado.

---

## 📄 Licença

Este projeto é livre para uso educacional.
