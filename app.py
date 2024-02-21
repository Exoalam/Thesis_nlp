from flask import Flask, jsonify, request, render_template, send_from_directory
from text_generator import Generator
from tokenizer import Tokenizer
generator =  Generator()
tokenz = Tokenizer()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/banglagpt')
def banglagpt():
    return render_template('banglagpt.html')

@app.route('/tokenizer')
def tokenzier():
    return render_template('token.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.json['message'] 
    
    response_message = generator.generate_text(user_message)
    return jsonify({'message': response_message})

@app.route('/asktoken', methods=['POST'])
def asktoken():
    corpus = request.json['message'] 

    tokens = str(tokenz.tokenize_text(corpus))
    
    return jsonify({'message': tokens})

@app.route('/datasets')
def datasets():
    return render_template('datasets.html')

@app.route('/dataset_token')
def dataset_token():
    # Assuming the text file is named example.txt and located in the static folder
    return send_from_directory('static', 'tokens.txt')

@app.route('/dataset_wiki')
def dataset_wiki():
    # Assuming the text file is named example.txt and located in the static folder
    return send_from_directory('static', 'wiki.txt')
@app.route('/dataset_convo')
def dataset_convo():
    # Assuming the text file is named example.txt and located in the static folder
    return send_from_directory('static', 'conv.txt')
if __name__ == '__main__':
    
    app.run(debug=True)
