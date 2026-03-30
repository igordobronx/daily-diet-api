# 📋 Daily Diet API

Uma API RESTful desenvolvida em Python com Flask para gerenciar informações sobre dieta diária, permitindo registrar, consultar e controlar refeições e nutrientes.

## 🚀 Sobre o Projeto

A Daily Diet API é uma aplicação backend que fornece endpoints para gerenciar dados de alimentação diária. Desenvolvida com **Flask** e **SQLAlchemy**, oferece uma solução robusta para controlar a ingestão de alimentos e nutrientes.

## 📦 Tecnologias Utilizadas

- **Python 3.x** - Linguagem de programação
- **Flask** - Framework web minimalista
- **SQLAlchemy** - ORM para gerenciamento de banco de dados
- **SQLite** - Banco de dados (desenvolvimento)
- **Python-dotenv** - Gerenciamento de variáveis de ambiente

## 🔧 Pré-requisitos

- Python 3.8+
- pip (gerenciador de pacotes Python)
- Git

## 📥 Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/igordobronx/daily-diet-api.git
cd daily-diet-api
```

### 2. Crie um ambiente virtual
```bash
python -m venv venv
```

### 3. Ative o ambiente virtual

**No Windows:**
```bash
venv\Scripts\activate
```

**No macOS/Linux:**
```bash
source venv/bin/activate
```

### 4. Instale as dependências
```bash
pip install -r requirements.txt
```

### 5. Configure as variáveis de ambiente

Copie o arquivo `.env.example` para `.env` e configure conforme necessário:
```bash
cp .env.example .env
```

### 6. Execute a aplicação
```bash
python app.py
```

A API estará disponível em `http://localhost:5000`

## 📚 Estrutura do Projeto
```
daily-diet-api/
├── app.py                 # Arquivo principal da aplicação
├── database.py            # Configuração do banco de dados
├── models/                # Modelos de dados
├── instance/              # Arquivos de instância (banco de dados)
├── .env.example           # Exemplo de variáveis de ambiente
├── .gitignore             # Arquivos ignorados pelo Git
├── requirements.txt       # Dependências do projeto
└── __pycache__/           # Cache Python
```

## 🔌 Endpoints Disponíveis

A API oferece os seguintes endpoints (ajuste conforme seus endpoints reais):

- `GET /api/meals` - Listar todas as refeições
- `POST /api/meals` - Criar nova refeição
- `GET /api/meals/<id>` - Obter detalhes de uma refeição
- `PUT /api/meals/<id>` - Atualizar uma refeição
- `DELETE /api/meals/<id>` - Deletar uma refeição

## 💻 Exemplo de Uso

### Criar uma refeição
```bash
curl -X POST http://localhost:5000/api/meals \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Almoço",
    "description": "Frango com arroz e feijão",
    "calories": 750,
    "date": "2024-01-15"
  }'
```

### Listar refeições
```bash
curl http://localhost:5000/api/meals
```

## 🛠️ Desenvolvendo

### Rodar em modo debug
```bash
python app.py
```

### Estrutura de Models

Os modelos estão organizados na pasta `models/` e utilizam SQLAlchemy para definir a estrutura das tabelas.

## 📝 Variáveis de Ambiente

Configure no arquivo `.env`:
```env
FLASK_ENV=development
FLASK_APP=app.py
DATABASE_URL=sqlite:///instance/daily_diet.db
SECRET_KEY=sua_chave_secreta_aqui
```

## 🚨 Tratamento de Erros

A API retorna respostas JSON com códigos HTTP apropriados:

- `200 OK` - Requisição bem-sucedida
- `201 Created` - Recurso criado com sucesso
- `400 Bad Request` - Dados inválidos
- `404 Not Found` - Recurso não encontrado
- `500 Internal Server Error` - Erro no servidor

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Autor

**Igor Dobronx**  
GitHub: [@igordobronx](https://github.com/igordobronx)

## 📞 Suporte

Para dúvidas ou sugestões, abra uma issue no repositório.
