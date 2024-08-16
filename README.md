# Gerador de Receitas - README
## Descrição
O Gerador de Receitas é uma aplicação web que permite aos usuários inserir ingredientes e gerar uma receita personalizada com base nesses ingredientes. A aplicação é composta por uma interface de usuário intuitiva onde os ingredientes podem ser adicionados ou removidos, e um backend que utiliza um modelo generativo para criar a receita.

## Funcionalidades
- Adicionar Ingredientes: O usuário pode adicionar vários ingredientes que deseja utilizar na receita.
- Remover Ingredientes: Os ingredientes podem ser removidos conforme necessário.
- Gerar Receita: Ao submeter os ingredientes, uma receita é gerada e exibida na tela, formatada em HTML.
## Estrutura do Projeto
- HTML (index.html): Estrutura a interface do usuário, permitindo a inserção de ingredientes e a visualização da receita gerada.
- CSS (style.css): Estiliza a interface, proporcionando uma experiência de usuário agradável.
- JavaScript (script.js): Manipula as interações do usuário, como adicionar ou remover ingredientes, e faz a requisição ao backend para gerar a receita.
- Backend (app.py): Utiliza o Flask para criar uma API que recebe os ingredientes, comunica-se com o modelo generativo para criar a receita, e retorna o resultado em formato HTML.
## Como Executar
### Requisitos
- Python 3.x
- Flask
- Flask-CORS
- Google Generative AI (Biblioteca gemini)
## Passos para Configuração
- Clone o repositório:
git clone https://github.com/usuario/projeto-gerador-receitas.git
cd projeto-gerador-receitas

- Instale as dependências do Python:
pip install flask flask-cors google-generativeai

- Gere sua chave de API em: https://aistudio.google.com/app/u/1/apikey
- Adicione sua chave API do Google Generative AI no arquivo app.py na linha:
gemini.configure(api_key="SUA_CHAVE_API_AQUI")

- Execute a aplicação Flask:
python api.py

- Abra o arquivo index.html no navegador:
Utilize um servidor local, como Live Server no VS Code, ou abra o arquivo diretamente em seu navegador.

## Uso
- Insira pelo menos três ingredientes no formulário da aplicação.
- Clique em "Gerar Receita".
- A receita gerada será exibida na tela.
## Licença
Este projeto é licenciado sob a Licença MIT.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests.

## Contato
Para mais informações, entre em contato pelo email: netootavio223@outlook.com
