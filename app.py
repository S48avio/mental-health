from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.json['message']
    ai_replies = {
        "hello": "Hey there! 😊",
        "how are you": "I'm doing great! How about you?",
        "what's your name": "I'm Serenity, your AI assistant!",
        "bye": "Goodbye! Have a great day! 👋",
    }
    bot_response = ai_replies.get(user_message.lower(), "That's interesting! Tell me more. 🤔")
    return jsonify({"response": bot_response})

if __name__ == '__main__':
    app.run(debug=True)
