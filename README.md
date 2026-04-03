# 🚛 Sistema de Gestão de Frota

> Aplicação web completa para controle e gerenciamento de frotas de veículos, desenvolvida com **Python + Flask** e banco de dados **SQLite**.

---

## 📋 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Funcionalidades](#-funcionalidades)
- [Tecnologias](#-tecnologias)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Banco de Dados](#-banco-de-dados)
- [Como Executar](#-como-executar)
- [Telas do Sistema](#-telas-do-sistema)

---

## 💡 Sobre o Projeto

Sistema web para gerenciamento completo de frotas, permitindo o controle de veículos, motoristas, abastecimentos, rotas e postos de combustível. Ideal para empresas que precisam acompanhar os custos operacionais e o histórico de movimentações da frota.

---

## ✅ Funcionalidades

### Dashboard
- Cards com totais de veículos ativos, motoristas, movimentações e gastos do mês
- Total de litros abastecidos no mês
- Tabela com as últimas movimentações registradas
- Atalhos rápidos para as principais ações

### Movimentações
- Registro completo de saídas e abastecimentos
- Controle de KM inicial e final com cálculo automático de distância percorrida
- Associação com rota e posto de combustível
- Controle de nível do tanque (%)
- Campo de observações
- Histórico completo com as últimas 200 entradas

### Veículos
- Cadastro com marca, modelo, combustível, consumo km/l e capacidade do tanque
- Controle de status: **Ativo**, **Manutenção** ou **Inativo**
- Dropdown de modelos carregado dinamicamente conforme a marca selecionada
- Edição inline via modal
- Exclusão com confirmação

### Motoristas
- Cadastro com CPF, categoria CNH, telefone e e-mail
- Controle de status (Ativo / Inativo)
- Edição e exclusão

### Marcas e Modelos
- CRUD completo com edição via modal
- Modelos vinculados às marcas com validação de unicidade

### Combustíveis
- Cadastro de tipos de combustível com preço por litro
- Edição e exclusão

### Rotas
- Cadastro de trajetos com origem, destino e distância em km
- Campo de descrição / observações
- CRUD completo com modal de edição

### Postos de Combustível
- Cadastro com endereço, cidade e UF
- **Histórico de preços** por posto e tipo de combustível
- Registro de variações de preço com data de coleta

---

## 🛠 Tecnologias

| Camada | Tecnologia |
|--------|-----------|
| Backend | Python 3.11 · Flask 3.x |
| Banco de dados | SQLite 3 |
| Frontend | Bootstrap 5.3 · Bootstrap Icons 1.10 |
| Gráficos | Chart.js 4.4 |
| Estilo | CSS customizado com variáveis e gradientes |

> Todas as bibliotecas front-end são servidas **localmente** (sem dependência de CDN), garantindo funcionamento mesmo sem acesso à internet.

---

## 📁 Estrutura do Projeto

```
Controle_combustivel_flask/
│
├── app.py                          # Aplicação Flask principal (rotas e lógica)
├── requirements.txt                # Dependências Python
│
├── database/
│   ├── db.py                       # Criação e migração automática do banco
│   ├── cadastro_combustivel.py     # CRUD de combustíveis
│   ├── crud_marcas.py              # CRUD de marcas
│   ├── crud_modelos.py             # CRUD de modelos
│   ├── crud_veiculos.py            # CRUD de veículos
│   ├── crud_motoristas.py          # CRUD de motoristas
│   ├── crud_rotas.py               # CRUD de rotas
│   ├── crud_postos.py              # CRUD de postos e histórico de preços
│   └── crud_movimentacoes.py       # CRUD de movimentações e estatísticas
│
├── dados/
│   └── consumo.db                  # Banco de dados SQLite (gerado automaticamente)
│
├── templates/
│   ├── template.html               # Layout base (sidebar + flash messages)
│   ├── home.html                   # Dashboard
│   ├── cadastro_combustivel.html   # Gestão de combustíveis
│   ├── cadastro_marcas.html        # Gestão de marcas
│   ├── cadastro_modelos.html       # Gestão de modelos
│   ├── cadastro_veiculos.html      # Gestão de veículos
│   ├── cadastro_motorista.html     # Gestão de motoristas
│   ├── cadastro_rotas.html         # Gestão de rotas
│   ├── cadastro_postos.html        # Gestão de postos e histórico de preços
│   └── movimentacoes.html          # Registro de movimentações
│
└── static/
    ├── css/
    │   ├── bootstrap.min.css       # Bootstrap 5 (local)
    │   ├── bootstrap-icons.css     # Bootstrap Icons (local)
    │   ├── template.css            # Estilos globais e sidebar
    │   └── cadastro_veiculos.css   # Estilos da tela de veículos
    ├── js/
    │   ├── bootstrap.bundle.min.js # Bootstrap JS (local)
    │   ├── chart.min.js            # Chart.js (local)
    │   └── template.js             # Toggle da sidebar
    └── fonts/
        ├── bootstrap-icons.woff2   # Fonte de ícones (local)
        └── bootstrap-icons.woff
```

---

## 🗄 Banco de Dados

O banco é criado e migrado automaticamente na primeira execução. O esquema contempla 9 tabelas interligadas:

```
marca ──┐
        ├──► modelo ──┐
                      ├──► veiculo ──────────────┐
combustivel ──────────┘                          │
                                                 ▼
motorista ──────────────────────────────► movimentacao
                                                 ▲
rota ────────────────────────────────────────────┤
                                                 │
posto ──┬────────────────────────────────────────┘
        └──► historico_preco ◄── combustivel
```

| Tabela | Descrição |
|--------|-----------|
| `marca` | Fabricantes de veículos |
| `modelo` | Modelos vinculados a marcas |
| `combustivel` | Tipos de combustível com preço base |
| `veiculo` | Frota cadastrada |
| `motorista` | Motoristas com categoria de CNH |
| `rota` | Trajetos com origem, destino e distância |
| `posto` | Postos de abastecimento |
| `movimentacao` | Saídas, retornos e abastecimentos |
| `historico_preco` | Variação de preço por posto e combustível |

---

## ▶ Como Executar

### Pré-requisitos

- Python 3.9 ou superior

### Instalação

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/controle-combustivel-flask.git
cd controle-combustivel-flask

# 2. (Recomendado) Crie um ambiente virtual
python -m venv venv

# Ative o ambiente — Windows:
venv\Scripts\activate
# Ative o ambiente — Linux/macOS:
source venv/bin/activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Execute a aplicação
python app.py
```

### Acesse no navegador

```
http://127.0.0.1:5000
```

> O banco de dados SQLite e todas as tabelas são criados automaticamente na primeira execução. Nenhuma configuração adicional é necessária.

---

## 🖥 Telas do Sistema

| Rota | Descrição |
|------|-----------|
| `/` | Dashboard com estatísticas e últimas movimentações |
| `/movimentacoes` | Registro e histórico de abastecimentos |
| `/cadastro_veiculos` | Gestão da frota de veículos |
| `/cadastro_motorista` | Gestão de motoristas |
| `/cadastro_combustivel` | Tipos e preços de combustível |
| `/cadastro_marcas` | Marcas de veículos |
| `/cadastro_modelos` | Modelos de veículos |
| `/cadastro_rotas` | Rotas e trajetos |
| `/cadastro_postos` | Postos e histórico de preços |

### Endpoint interno (API JSON)

| Endpoint | Descrição |
|----------|-----------|
| `GET /api/modelos?marca_id=X` | Retorna modelos de uma marca — utilizado para popular dropdowns dinamicamente |

---

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar, modificar e distribuir.

---

**Desenvolvido com Flask · SQLite · Bootstrap 5**
