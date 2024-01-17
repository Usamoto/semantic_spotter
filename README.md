# Semantic Spotter

## Project Overview

Semantic Spotter is an advanced text analysis tool designed to process and analyze insurance policy documents. Utilizing state-of-the-art natural language processing techniques, it can read through extensive policy texts and provide insights or answers to specific queries. This tool leverages technologies such as PDF processing, text chunking, sentence embeddings, and Flask for web interfacing.

## Features

- **PDF Text Extraction**: Reads and extracts text from insurance policy documents.
- **Text Chunking**: Splits large texts into manageable chunks for better processing.
- **Text Embeddings**: Generates embeddings for text chunks to capture semantic meanings.
- **Query Processing**: Analyzes user queries and finds the most relevant text chunk.
- **Web Interface**: Simple and user-friendly web interface for interacting with the tool.

## Getting Started
https://github.com/Usamoto/semantic_spotter
### Prerequisites

- Python 3.x
- Virtual Environment (recommended)

### Installation

1. Clone the repository:
2. Navigate to the project directory:
3. Create and activate a virtual environment (optional):
4. Install the required dependencies:


### Running the Application

1. Run the Flask application:
2. Open a web browser and navigate to `http://127.0.0.1:5000/`.

## Usage

Enter your query related to the insurance policy in the web interface and submit. The tool processes your query and returns the most relevant section from the policy document.

## Project Structure

- `src/`: Source code for the project.
- `app.py`: Flask application.
- `pdf_processor.py`: Handles PDF reading and text chunking.
- `embedding_generator.py`: Generates embeddings for text chunks.
- `query_handler.py`: Processes user queries and finds relevant text.
- `response_generator.py`: (If applicable) Generates response based on query.
- `templates/`: HTML templates for the web interface.
- `static/`: CSS and static files for the web interface.
- `requirements.txt`: List of dependencies for the project.

## Contributions

Contributions to the Semantic Spotter project are welcome. Please ensure to follow the project's code style and contribution guidelines.

## License



## Acknowledgments

- Sentence Transformers Library
- pdfplumber Library
- Flask Framework
- [Any other libraries or resources used]

---

