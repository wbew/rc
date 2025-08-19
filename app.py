from flask import Flask, abort, request


class Database:
    def __init__(self):
        self.db = {}

    def set(self, key, value):
        self.db[key] = value

    def get(self, key):
        return self.db.get(key)


db = Database()
app = Flask(__name__)


@app.get("/")
def index():
    return {"status": "OK"}


@app.post("/set")
def set_kv():
    if len(request.args) == 0:
        return {"error": "A key=value pair in query params is required"}, 400

    saved = {}
    for k, v in request.args.items():
        db.set(k, v)
        saved[k] = v

    return {"success": True, "saved": saved}


@app.get("/get")
def get_kv():
    key = request.args.get("key")
    if not key:
        return {"error": "Key is required"}, 400

    return {"value": db.get(key)}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)
