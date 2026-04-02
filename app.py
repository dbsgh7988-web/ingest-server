from flask import Flask, request

app = Flask(__name__)

@app.route("/ingest", methods=["GET", "POST"])
def ingest():
    text = ""

    # 1️⃣ JSON
    if request.is_json:
        data = request.get_json()
        text = data.get("text", "")

    # 2️⃣ form 방식
    elif request.form:
        text = request.form.get("text", "")

    # 3️⃣ GET 방식
    elif request.args:
        text = request.args.get("text", "")

    # 4️⃣ raw
    else:
        text = request.data.decode("utf-8")

    print("📩 수신:", text)

    if "입금" in text:
        print("💰 입금 감지!")

    return {"status": "ok"}

@app.route("/")
def home():
    return "SERVER RUNNING"
