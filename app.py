from flask import Flask, render_template, request, jsonify
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

client = genai.Client(api_key="your_api_key_here")  # Replace with your actual API key

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    message = request.json.get("message")

    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=message
        )

        return jsonify({ "reply": response.text })

    except Exception as e:
        return jsonify({"reply": str(e)})
    
if __name__ == "__main__":
    app.run(debug=True)