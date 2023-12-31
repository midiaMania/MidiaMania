<p align="center">
  <img src="https://raw.githubusercontent.com/midiaMania/MidiaMania/b0c63ab80f1412584889cb09b274dce7497ab2ed/frontend/static/logo.svg?token=A74ZPD2HW4TE4HU7BEXS2ZLFNQIUG" alt="MidiaMania" />
</p>

## 🚀 Sobre o Projeto

O projeto para um Sistema de Locadora Online de Filmes, Músicas e Mídias "MidiaMania" é uma aplicação web desenvolvida em Django, que tem como objetivo criar uma plataforma de locação e streaming de conteúdo multimídia. Esta iniciativa foi elaborada por estudantes de Engenharia da Computação da Universidade Federal do Vale do São Francisco como parte do currículo da disciplina de Sistemas Distribuídos.

## 🛠 Linguagens e Frameworks

![Python](https://img.shields.io/badge/Python-000?style=for-the-badge&logo=python)
![PyPI - Versions from Framework Classifiers](https://img.shields.io/pypi/frameworkversions/django/pacote)

**Front-end:** TailwindCSS, NES.css

**Back-end:** Django

## Requisitos

- Python
- Nodejs

## Ambiente Virtual

### Criar Ambiente

```sh
python -m venv venv
```

### Ativar Ambiente

#### Windows

```cmd
.\venv\Scripts\activate
```

#### Linux/Mac

```sh
source venv/bin/activate
```

## Instalação

```sh
pip install -r requirements.txt
```

```sh
python manage.py tailwind install
```

## Executar o projeto

### Bash/CMD

```sh
python manage.py tailwind start & python manage.py runserver
```

### Windows PowerShell

```sh
python manage.py tailwind start ; python manage.py runserver
```

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

#### Padrões de Commit

| Tipo       | Descrição                                                 |
|------------|----------------------------------------------------------|
| [FEAT]     | Quando um novo recurso foi desenvolvido                  |
| [FIX]      | Quando um recurso/bug foi corrigido                      |
| [UPDATE]   | Quando arquivos estáticos foram renomeados, removidos, movidos de um diretório para outro, adicionados ou substituídos |
| [REFACTOR] | Quando uma alteração de código que não corrige um bug nem adiciona um recurso |
| [DOCS]     | Somente alterações na documentação                        |


![git_Branchnaming](https://miro.medium.com/v2/resize:fit:720/format:webp/1*GpWwKA_FRh3o-3pWNJ767Q.png)

# Créditos

[<img src="https://www.gstatic.com/tenor/web/attribution/PB_tenor_logo_blue_horizontal.png" alt="tenor" width="200px" />](https://tenor.com/pt-BR/)

[<img src="https://raw.githubusercontent.com/cirla/vim-giphy/master/powered_by_giphy.gif" alt="giphy" width="200px" />](https://giphy.com/)
