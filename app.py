from flask import Flask, request

app = Flask(__name__)

@app.route("/ingest", methods=["POST"])
def ingest():
    data = request.json
    text = data.get("text", "")

    print("📩 수신:", text)

    if "입금" in text:
        print("💰 입금 감지!")

    return {"status": "ok"}

@app.route("/")
def home():
    return "SERVER RUNNING"
