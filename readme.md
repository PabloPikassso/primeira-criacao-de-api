# Primeira criação de API

API simples de livros feita com Python e Flask. Permite listar, buscar, criar, atualizar e excluir livros (CRUD).

## Como rodar

```bash
pip install flask
python app.py
```

A API sobe em `http://localhost:5000`.

## Rotas

| Método | Rota           | Descrição                |
|--------|----------------|--------------------------|
| GET    | `/livros`      | Lista todos os livros    |
| GET    | `/livros/<id>` | Busca um livro pelo id   |
| POST   | `/livros`      | Cria um novo livro       |
| PUT    | `/livros/<id>` | Atualiza um livro        |
| DELETE | `/livros/<id>` | Exclui um livro          |

## Exemplo de livro

```json
{
  "id": 1,
  "titulo": "Berserk",
  "autor": "Kentaro Miura"
}
```
