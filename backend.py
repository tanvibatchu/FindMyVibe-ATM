import os
import time
from flask import Flask, request, jsonify
from pymongo import MongoClient
from google import genai
from dotenv import load_dotenv

# 1. SETUP & CONFIGURATION
load_dotenv(".env.local")

app = Flask(__name__)

# Intialise Gemini and mongoDB client
gemini_client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
mongo_client = MongoClient(os.getenv("MONGODB_URI"))

# Create Databses and Collections
db = mongo_client[os.getenv("MONGO_DB_NAME")]
movies_col = db[os.getenv("MONGO_COLLECTION_NAME")]
cache_col = db["query_cache"]  # New collection to save API calls

# Start creating the core functions
def get_embedding(text):
    # Check has someone searched this exact string before
    cached_result = cache_col.find_one({"query_text": text.lower().strip()})
    if cached_result:
        #If input in the cache already skip API call and return the previous answer
        print("Cache Hit! Skipping API call.")
        return cached_result["embedding"]

    # If its not in cache
    print("Calling Gemini API for embedding...")
    try:
        #Getting Gemini Data
        result = gemini_client.models.embed_content(
            model="text-embedding-004",
            contents=text
        )
        #Storing it as current vector
        vector = result.embeddings[0].values
        
        # Save the query to the cache incase called again - Reducing API calls
        cache_col.insert_one({
            "query_text": text.lower().strip(),
            "embedding": vector,
            "timestamp": time.time()
        })
        #Return the vector given
        return vector
    except Exception as e:
        print(f"Gemini Error: {e}")
        return None

# Make a function that does the vector search
def vector_search(user_query_vector):
    # Objective is to perform a vector search in mongoDB
    
    # Use mongoDB steps to find
    pipeline = [
        {
            "$vectorSearch": {
                "index": "vector_index", # MUST match the index name in Atlas
                "path": "plot_embedding",
                "queryVector": user_query_vector,
                "numCandidates": 100,
                "limit": 5
            }
        },
        {
            "$project": {
                "title": 1,
                "plot": 1,
                "genres": 1,
                "poster": 1,
                "score": {"$meta": "vectorSearchScore"}
            }
        }
    ]
    # Return a list of movies
    return list(movies_col.aggregate(pipeline))

# 3. THE API ENDPOINT
@app.route('/search', methods=['POST'])
def search():
    data = request.json
    user_input = data.get("vibe", "")

    if not user_input:
        return jsonify({"error": "No vibe provided"}), 400

    # Step 1: Get Vector (Either from Cache or Gemini)
    vector = get_embedding(user_input)
    
    if not vector:
        return jsonify({"error": "AI Processing Failed"}), 500

    # Step 2: Search MongoDB
    results = vector_search(vector)

    # Step 3: Clean up MongoDB _id for JSON response
    for res in results:
        res["_id"] = str(res["_id"])

    return jsonify(results)

if __name__ == "__main__":
    app.run(port=5001, debug=True)