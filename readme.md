# Projeto prático de Banco de Dados - Inserção e Relatórios no Northwind

Este projeto foi desenvolvido como atividade prática da disciplina de Banco de Dados e tem como objetivo:

- Inserir pedidos no banco de dados Northwind
- Gerar relatórios de pedidos e vendas por funcionário
- Demonstrar o uso de `psycopg2` (driver puro) e `SQLAlchemy` (ORM)
- Implementar versões seguras e **inseguras** (vulneráveis a SQL Injection)

---

## :hammer_and_wrench: Tecnologias utilizadas
- Python 3.12+
- PostgreSQL
- Psycopg2
- SQLAlchemy
- DBeaver (cliente visual para banco de dados)

---

## :file_folder: Estrutura do projeto

```
├── config/                 # Conexão com o banco via psycopg2
├── controller/             # Lógica de negócio
├── dao/                    # Acesso a dados (versão segura e insegura)
├── model/                  # Classes de modelo
├── relatorios/             # Relatórios SQL
├── view/                   # Interface interativa via terminal
├── sqlalchemy_version/     # Versão alternativa usando SQLAlchemy ORM
│   └── app_sqlalchemy.py   # Executa a versão com ORM
├── app_driver.py           # Executa a versão com psycopg2
```

---

## :lock: Segurança vs Vulnerabilidade (SQL Injection)

O projeto demonstra dois cenários:

### ✅ Versão segura
- Usa **parâmetros** na SQL (`%s`) via psycopg2
- Protege contra SQL Injection

### ❌ Versão vulnerável
- Concatena diretamente valores na query (f-strings)
- Permite entrada como:
  ```
  MEREP'); SELECT 1; --
  ```
  Resultando em erro de sintaxe: **isso mostra que a injeção foi tentada** e parcialmente executada, mas bloqueada pelo psycopg2.

### 🔒 Relatório inseguro
- No relatório detalhado de pedidos, o usuário pode digitar:
  ```
  0 OR 1=1
  ```
  E a query retorna **todos os pedidos do banco**, demonstrando vazamento de dados.

---

## :rocket: Como rodar o projeto

### ὜4 Versão com `psycopg2` (driver puro)
```bash
python app_driver.py
```
No menu interativo, você pode:
- Inserir pedidos (modo seguro ou inseguro)
- Ver relatórios (seguro e vulnerável)

### ὜4 Versão com `SQLAlchemy ORM`
```bash
python -m sqlalchemy_version.app_sqlalchemy
```
Essa versão reimplementa a inserção de pedidos com ORM, mantendo a mesma lógica da versão principal.

---

## :warning: Ajuste necessário para inserção de pedidos

Ao importar o banco Northwind, a tabela `orders` já possuía dados com IDs altos (ex: `11077`), mas a sequência de autoincremento não estava sincronizada.

Foi executado o seguinte comando para corrigir:
```sql
SELECT setval('orders_orderid_seq', (SELECT MAX(orderid) FROM northwind.orders));
```
Isso garante que novos pedidos recebam um ID correto e sequencial a partir do maior existente.

---

## :white_check_mark: Checklist da atividade

- [x] Inserção de pedidos com psycopg2 (seguro e inseguro)
- [x] Relatório detalhado de pedido
- [x] Relatório de ranking de funcionários por período
- [x] SQL Injection demonstrado na inserção (com erro) e no relatório (vazamento)
- [x] Adaptação da inserção usando SQLAlchemy ORM
- [x] Interface interativa com menu em terminal

---

> Projeto prático desenvolvido por Gabriel de Souza Ribeiro e Bryan Miller para fins de avaliação em disciplina de Banco de Dados II - 2025/1

