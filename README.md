# ERP de EPI - Projeto Django

Este repositório contém um projeto desenvolvido com Django como parte de uma atividade do curso do SENAI. O objetivo do projeto é construir um sistema ERP (Enterprise Resource Planning) voltado para o gerenciamento de EPIs (Equipamentos de Proteção Individual) em uma organização.


## Tecnologias Utilizadas

* Django 4.x
* Python 3.x
* python-decouple (para variáveis de ambiente)
* MySQL




## Funcionalidades do Sistema

* Cadastro e gerenciamento de EPIs  
* Cadastro de colaboradores 
* Controle de entrega de EPIs para os colaboradores  
* Emissão de relatórios de entrega  
* Controle de validade dos EPIs
## Contribuição

Este projeto contou com a colaboração de três desenvolvedores dedicados:

* [Gabriel Chiarelli](https://github.com/gaab0418) – Desenvolvimento Backend e Modelagem de Dados;

* [Gabriel Vinicius](https://github.com/GabrielGVCB)  – Interface Frontend e Integrações;

* [Luis Perazza](https://github.com/LuisPerazza)  – Testes, Documentação e Suporte.
## Instalação

### 1. Clone o repositório:
```bash
git clone https://github.com/CSouzaCatolica/SENAIprojeto
```
### 2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```
### 3. Instale as dependências:
```bash
pip install -r requirements.txt
```
### 4. Configure o banco de dados MySQL com variáveis de ambiente:
Siga para ...[TODO]
### 5. Inicie a migração e o servidor:
```bash
python manage.py migrate
python manage.py runserver
```
Acesse o sistema em: http://localhost:8000
## Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```
DB_SETTINGS:{
    DB_NAME=ggp
    DB_USER=seu_usuario
    DB_PASSWORD=sua_senha
    DB_HOST=localhost
    DB_PORT=3306
}
```


## Dados de Demonstração (SQL opcional)

Para facilitar a demonstração do sistema, você pode executar o script SQL abaixo no banco MySQL:

```sql
-- Inserção de colaboradores
INSERT INTO teste (nome, cpf, setor) VALUES
('João da Silva', '12345678900', 'Almoxarifado'),
('Maria Oliveira', '98765432100', 'Produção');
```

**Obs.:** É necessário configurar as variavéis de ambiente!
