
# Midia Mania Project




## 🚀 Sobre o Projeto
O projeto para um Sistema de Locadora Online de Filmes, Músicas e Mídias "MidiaMania" é uma aplicação web desenvolvida em Django, que tem como objetivo criar uma plataforma de locação e streaming de conteúdo multimídia. Esta iniciativa foi elaborada por estudantes de Engenharia da Computação da Universidade Federal do Vale do São Francisco como parte do currículo da disciplina de Sistemas Distribuídos.




## 🛠 Linguagens e Frameworks

![Python](https://img.shields.io/badge/Python-000?style=for-the-badge&logo=python)
![PyPI - Versions from Framework Classifiers](https://img.shields.io/pypi/frameworkversions/django/pacote)


## Documentação da API

#### Retorna todos os itens

```http
  GET /api/items
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `api_key` | `string` | **Obrigatório**. A chave da sua API |

#### Retorna um item

```http
  GET /api/items/${id}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `string` | **Obrigatório**. O ID do item que você quer |

#### add(num1, num2)

Recebe dois números e retorna a sua soma.

