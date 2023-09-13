from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # URL da API que você deseja consumir
    api_url = 'http://127.0.0.1:5000/lessons'

    try:
        # Faz uma solicitação GET para a API
        response = requests.get(api_url)

        # Verifica se a solicitação foi bem-sucedida (código de status 200)
        if response.status_code == 200:
            # Converte a resposta JSON em um dicionário Python (ou ajuste para o formato da sua API)
            data = response.json()
            # Renderiza uma página HTML com os dados da API
            return render_template('index.html', data=data)
        else:
            # Se a solicitação não foi bem-sucedida, retorna uma mensagem de erro
            return 'Erro ao buscar dados da API'
    except Exception as e:
        # Se ocorrer algum erro na solicitação, retorna uma mensagem de erro
        return f'Shuster esteve aqui Erro: {str(e)}'

if __name__ == '__main__':
    app.run(debug=True)
