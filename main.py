from flask import Flask, request, jsonify

app = Flask(__name__)

DATA = []

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "ok",
        "message": "Analiz sistemi aktif",
        "data": DATA
    })

@app.route("/ekle", methods=["POST"])
def ekle():
    gelen = request.json
    if gelen:
        DATA.append(gelen)
        return jsonify({"ok": True})
    return jsonify({"ok": False}), 400

if __name__ == "__main__":
    app.run()
