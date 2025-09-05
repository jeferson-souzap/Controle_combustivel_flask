# Sistema de Gestão de Frota

Um sistema completo para gerenciamento de frotas de veículos desenvolvido em Flask com interface moderna e responsiva.

## 🚀 Acesso Online

**URL da Aplicação:** http:// --

## 📋 Funcionalidades

### Dashboard

- Visão geral com estatísticas da frota
- Gráficos de consumo mensal
- Distribuição por tipos de combustível
- Indicadores de performance

### Módulos de Cadastro

- **Combustíveis**: Gerenciamento de tipos e preços
- **Marcas**: Cadastro de marcas de veículos
- **Modelos**: Modelos por marca
- **Veículos**: Controle completo da frota
- **Motoristas**: Gestão de condutores

### Movimentações

- Registro de abastecimentos
- Controle de quilometragem
- Histórico completo de movimentações

## 🎨 Características da Interface

### Design Responsivo

- Layout adaptável para desktop, tablet e mobile
- Barra lateral retrátil com toggle
- Interface moderna com Bootstrap 5

### Experiência do Usuário

- Navegação intuitiva
- Alertas de feedback
- Formulários validados
- Tabelas organizadas com ações

## 🛠️ Tecnologias Utilizadas

### Backend

- **Flask**: Framework web Python
- **SQLAlchemy**: ORM para banco de dados
- **SQLite**: Banco de dados
- **Flask-CORS**: Suporte a CORS

### Frontend

- **HTML5/CSS3**: Estrutura e estilização
- **Bootstrap 5**: Framework CSS
- **JavaScript**: Interatividade
- **Chart.js**: Gráficos e visualizações
- **Bootstrap Icons**: Ícones

## 📁 Estrutura do Projeto

```bash
gestao-frota/
├── src/
│   ├── models/          # Modelos de dados
│   │   ├── combustivel.py
│   │   ├── marca.py
│   │   ├── modelo.py
│   │   ├── veiculo.py
│   │   ├── motorista.py
│   │   └── movimentacao.py
│   ├── routes/          # Rotas da API
│   │   ├── combustivel.py
│   │   ├── marca.py
│   │   ├── modelo.py
│   │   ├── veiculo.py
│   │   ├── motorista.py
│   │   └── movimentacao.py
│   ├── static/          # Arquivos estáticos
│   │   ├── index.html
│   │   └── app.js
│   ├── database/        # Banco de dados
│   │   └── app.db
│   └── main.py          # Aplicação principal
├── venv/                # Ambiente virtual
├── requirements.txt     # Dependências
└── README.md           # Documentação
```

## 🚀 Como Usar

1. **Acesse a aplicação**:

2. **Navegação**: Use o menu lateral para acessar os diferentes módulos

3. **Cadastros**:
Comece cadastrando:
   - Combustíveis (ex: Gasolina, Etanol, Diesel)
   - Marcas de veículos
   - Modelos de veículos
   - Veículos da frota
   - Motoristas

4. **Movimentações**: Registre abastecimentos e movimentações

5. **Dashboard**: Acompanhe estatísticas e gráficos

## 📱 Responsividade

O sistema é totalmente responsivo e funciona em:

- Desktop (1200px+)
- Tablet (768px - 1199px)
- Mobile (até 767px)

## 🔒 Segurança

- Validação de dados no frontend e backend
- Sanitização de entradas
- Tratamento de erros
- CORS configurado adequadamente

## 📈 Próximas Funcionalidades

- Relatórios em PDF
- Exportação de dados
- Notificações de manutenção
- Controle de usuários
- Backup automático

---

**Desenvolvido com Flask e tecnologias modernas para gestão eficiente de frotas.**
