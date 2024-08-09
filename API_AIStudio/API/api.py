from flask import Flask, jsonify, request
from flask_cors import CORS
import google.generativeai as gemini

app = Flask(__name__)
CORS(app)

gemini.configure(api_key="AIzaSyD1EuGAVO9wiLMlqdVIgJuoTwpejIM4M6Y")
model = gemini.GenerativeModel('gemini-1.5-flash')

@app.route('/receita', methods=['POST'])
def make_receita():
    try:
        dados = request.json
        ingredientes = dados.get('ingredientes')

        prompt = f""" 
    Crie uma receita somente com os seguintes ingredientes: (ingredientes).
    Apresente a receita no formato html com codificação UTF-8, sem o header,
    com o título em hl, subtítulos em h2, tempo de preparo em parágrafo
    acompanhado de um ícone de relógio, rendimento em porções em parágrafo
    acompanhado de um ícone de pratos, a lista de ingredientes em lista não
    ordenada, modo de preparo com passos em lista ordenada, sugestão para
    servir em parágrafo.
    """
        
        resposta = model.generate_content(prompt)
        print(resposta)

        receita = resposta.text.strip().split('\n')

        return (receita), 200
    except Exception as e:
        return jsonify({"Erro": str(e)}), 300
    


if __name__ == '__main__':
    app.run(debug=True)