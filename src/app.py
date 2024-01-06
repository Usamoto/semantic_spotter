from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    user_query = request.form.get('query')
    # Logik zur Verarbeitung der Anfrage und Generierung der Antwort
    response = "Antwort auf die Anfrage: " + user_query  # Ersetzen Sie dies durch Ihre Antwortlogik
    return render_template('index.html', query=user_query, response=response)

if __name__ == '__main__':
    app.run(debug=True)
