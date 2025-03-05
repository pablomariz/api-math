# API Math - FastAPI

Esta é uma API simples para operações matemáticas básicas, fornecendo endpoints para soma e média de uma lista de números.

## 📦 Tecnologias Utilizadas

- Python 3.10+
- FastAPI
- Docker & Docker Compose
- Pytest

---

## 🚀 Como Executar o Projeto

### 📥 1. Clonar o Repositório
```sh
git clone https://github.com/{seu-usuario}/api-math.git
cd api-math
```

### 🐳 2. Executar com Docker
A maneira recomendada de rodar o projeto é via **Docker Compose**:

```sh
docker-compose up --build
```

A API estará disponível em:  
🔗 **http://localhost:8000**

---

## 📑 Documentação da API

A documentação interativa pode ser acessada em:

- 🔹 **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- 🔹 **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## Como Executar os Testes

```sh
docker-compose run --rm api pytest
```

Se tudo estiver correto, você verá uma saída semelhante a esta:

```
================================================================== test session starts ==================================================================
platform linux -- Python 3.10.16, pytest-8.3.5, pluggy-1.5.0
collected 6 items

app/tests/test_math.py ...                                                                                                                      [ 50%]
app/tests/test_routes.py ...                                                                                                                    [100%]

================================================================== 6 passed in 1.23s ===================================================================
```

---

### 📌 Exemplos de Uso

#### 🔹 Soma (`/sum`)
**Requisição:**
```json
{
  "numbers": [1, 2, 3, 4]
}
```
**Resposta:**
```json
{
  "result": 10
}
```

#### 🔹 Média (`/average`)
**Requisição:**
```json
{
  "numbers": [2, 4, 6, 8]
}
```
**Resposta:**
```json
{
  "result": 5.0
}
```
