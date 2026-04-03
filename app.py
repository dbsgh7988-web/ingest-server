from flask import Flask, request

app = Flask(__name__)

@app.route("/ingest", methods=["GET", "POST"])
def ingest():
    text = ""

    if request.is_json:
        data = request.get_json()
        text = data.get("text", "")
    elif request.form:
        text = request.form.get("text", "")
    elif request.args:
        text = request.args.get("text", "")
    else:
        text = request.data.decode("utf-8")

    print("📩 수신:", text)

    if "입금" in text:
        print("💰 입금 감지!")

    return {"status": "ok"}


@app.route("/")
def home():
    return "SERVER RUNNING"


# 🔥 텔레그램 Webhook (수정 버전)
@app.route("/telegram_webhook", methods=["POST"])
def telegram_webhook():
    data = request.get_json()

    text = ""

    if "message" in data:
        text = data["message"].get("text", "")
    elif "channel_post" in data:
        text = data["channel_post"].get("text", "")

    print("📩 메시지 수신:", text)

    if "입금" in text:
        print("💰 입금 감지!")

    return {"ok": True}
