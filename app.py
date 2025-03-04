from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def chatbot_response(message):
    responses = {
        "hello": "Hi there! How can I assist you?",
        "how are you": "I'm just a chatbot, but I'm here to help!",
        "bye": "Goodbye! Have a great day!",
    }
    return responses.get(message.lower(), "I'm sorry, I didn't understand that.")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.json.get("message")
    response = chatbot_response(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
