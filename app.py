from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.json['message'] 

    response_message = "Response from the model will go here"
    return jsonify({'message': response_message})

if __name__ == '__main__':
    app.run(debug=True)
