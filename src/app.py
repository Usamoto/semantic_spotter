from flask import Flask, render_template, request
from pdf_processor import read_pdf, chunk_text
from embedding_generator import generate_embeddings
from query_handler import find_most_relevant_chunk

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    user_query = request.form.get('query')
    response = find_most_relevant_chunk(user_query, chunks, embeddings)
    return render_template('index.html', query=user_query, response=response)

if __name__ == '__main__':
    file_path = 'path_to_your_pdf.pdf'
    pdf_text = read_pdf(file_path)
    chunks = chunk_text(pdf_text)
    embeddings = generate_embeddings(chunks)
    app.run(debug=True)
