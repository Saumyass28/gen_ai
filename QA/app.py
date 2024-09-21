from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os
from pinecone import Pinecone, ServerlessSpec

app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)

# Initialize Pinecone
pc = Pinecone(api_key='your-pinecone-api-key')  # Replace with your actual API key
index_name = 'qa-bot-index'

# Check if index exists, create if it doesn't
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=768,
        metric='cosine',
        spec=ServerlessSpec(cloud='aws', region='us-east-1')
    )

index = pc.Index(index_name)

def get_query_embedding(query):
    # Placeholder for embedding generation logic
    return [0.1] * 768  # Example embedding of size 768

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    user_query = request.json.get('query')
    query_embedding = get_query_embedding(user_query)
    results = index.query(vector=query_embedding, top_k=5, include_values=True)
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
