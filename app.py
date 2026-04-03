from flask import Flask, jsonify, request
from environment import InterviewEnv

app = Flask(__name__)
env = InterviewEnv()

@app.route("/")
def home():
    return "Running 🚀"

@app.route("/reset", methods=["GET", "POST"])
def reset():
    state = env.reset()
    return jsonify(state)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
