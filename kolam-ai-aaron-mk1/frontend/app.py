import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ai_agent.ai_agent import generate_response

from flask import Flask, render_template, request, jsonify
from backend.models import init_db

app = Flask(__name__)
init_db()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send_message", methods=["POST"])
def send_message():
    user_message = request.form.get("message", "").strip()
    if not user_message:
        return jsonify({"response": "Please enter a valid message."})

    try:
        response_text = generate_response(user_message)
        if not response_text:
            response_text = "I'm sorry, I didn't get that. Could you please rephrase?"
    except Exception as e:
        print(f"Error in generate_response: {e}")
        response_text = "Oops! Something went wrong while processing your message."

    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run(debug=True)