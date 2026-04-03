from flask import Flask, jsonify
from environment import InterviewEnv

app = Flask(__name__)
env = InterviewEnv()

@app.route("/")
def home():
    return "Running 🚀"

@app.route("/reset")
def reset():
    state = env.reset()
    return jsonify(state)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)