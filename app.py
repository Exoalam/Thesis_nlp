from flask import Flask, jsonify, request, render_template
from text_generator import Generator
from tokenizer import Tokenzier
generator =  Generator()
tokenz = Tokenzier()
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

    tokens = str(tokenz.byte_pair_encode_bangla(corpus, 5))
    
    return jsonify({'message': tokens})

if __name__ == '__main__':
    
    app.run(debug=True)
