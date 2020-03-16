# API ChamaMoeda

### Informações Gerais

--- 

Esta API foi desenvolvida como Desafio para emprego em um StartUp carioca. O objetivo é permitir que funcionalidades diversas consultem a página de cotações de moedas  https://www.bcb.gov.br/conversao) do site do Banco Central do Brasil (BCB).

O produto atual pode ser chamado de versão beta, pois contempla apenas as atividades do exercício 1, se caracterizando como o Minimum Viable Product (MVP) dentro do prazo acordado, das dificuldades e, principalmente, da necessidade de aprender novos conceitos e ferramentas.
Ao longo do desenvolvimento foram constatadas imperfeições na página de cotações que acabaram se tornando na maior dificuldade da atividade, sendo o fator que mais tomou tempo em todo o processo. 

O site é extremamente lento, não funciona de forma adequada em todos os browsers, principalmente no Google Chrome que, atualmente é o navegador mais popular. Em versões posteriores da API, seria interessante a preparação para outros browsers, não apenas o Google Chrome. Apesar da página mostrar como opção de escolha moedas que podemos considerar como exóticas para o brasileiro (Malásia e Nepal, por exemplo), os testes nunca obtiveram sucesso, deixando a dúvida se realmente existem cotações para extas moedas na base de dados do BCB. A solução ideal seria a obtenção de API com fornecedor que substituísse esta página para uma comunicação mais eficiente e um serviço mais eficaz.

Instalação
====================================
Para poder executar a solução, além do Python, algumas bibliotecas foram necessáriasm sege a lista:
Componentes necessários
-----------------------
**Flask**	- provê um modelo simples para desenvolvimento web (API)

**Selenium** – Ferramenta para automação de testes que foi usada para navegação automática no site, pois não bastava extrair os dados dados (Data scraping), mas também interagir com a página web.

**RE** – módulo Python para expressões regulares

### Ambiente virtual

---

pip install virtualenv
virtualenv ambvir --python=python3.8
ambvir\Scripts\activate.bat
pip install ngrok

### Como instalar

--- 

pip install Flask
pip install flask_restful
pip install selenium
pip install requests

Fazer download do chromedriver.exe para a pasta do projeto

Disponibilizar a API: python app.py



### Checagem do ambiente com pip freeze
Arquivo requirements.txt

aniso8601==8.0.0
certifi==2019.11.28
chardet==3.0.4
click==7.1.1
Flask==1.1.1
Flask-RESTful==0.3.8
idna==2.9
itsdangerous==1.1.0
Jinja2==2.11.1
MarkupSafe==1.1.1
ngrok==0.0.1
pytz==2019.3
requests==2.23.0
selenium==3.141.0
six==1.14.0
urllib3==1.25.8
Werkzeug==1.0.0

Para instalação em outra máquina

	pip install -r requirements.txt

Se quiser desativar o ambiente virtual

	deactivate

Para disponibilidade para a web

	Utilizar ngrok

Acesso externo:

	http://c7039d05.ngrok.io/ChamaMoeda

Exemplo de chamada:

	Exemplo no consumo.py


### Bugs conhecidos

---

Devido às falhas informadas na seção Informações Gerais, existem momentos que o site do BCB não responde adequadamente, principalmente no momento da seleção das moedas por não aceitar clique. 

A API está preparada para tratar este e outros erros, trazendo o valor -1 para a cotação e uma mensagem de texto explicativa, no caso especificado “Erro na seleção da Moeda Origem”.

### Referências:

---

Seguem listas sites que foram usados como base de consulta e aprendizado nesta atividade:

- stackoverflow

-	https://www.python.org/

-	https://www.w3schools.com/

-	https://www.selenium.dev/documentation/en/

-	https://agiletesters.com.br/

-	https://www.journaldev.com/

-	https://readme.md/

-	https://wikipedia.org


### Cursos realizados

---

- youtube.com (Gratuitos)

-	Curso de Flask - Júlia Rizza

-	Expressões Regulares em Python - Otávio Miranda

-	Código Fonte TV

-	NGROK Como permitir que o seu cliente acesse o projeto sem precisar de hospedagem

- udemy.com.br (Pago)

	REST APIs com Python e Flask


### Principais ferramentas utilizadas

---

- Python

	Expressões Regulares

	Criação de Funções

	Modularização

- API

	Criação, disponibilização e consumo

	Métodos Get, Post e Put

	Postman

	Ngrok

- JSON

	Criação e Consumo

- Selenium

	Controle de Janelas

	Uso de teclas

	Uso campos texto, listas e botões

- readme

	Estrutura do documento

	MarkDown Editor