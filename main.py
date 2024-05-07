import quart, json, quart_cors
from typing import Any
from quart import request
from wellknown import generate_wellknown_config
from openapi import generate_openapi

app = quart_cors.cors(quart.Quart(__name__))

# Keep track of todo's. Does not persist if Python session is restarted.
_TODOS: Any = {}


# curl -X POST "http://0.0.0.0:5003/todos/test" -d '{"todo": "hello"}'
@app.post("/todos/<string:username>")
async def add_todo(username):
    request = await quart.request.get_json(force=True)
    if username not in _TODOS:
        _TODOS[username] = []
    _TODOS[username].append(request["todo"])
    return quart.Response(response="OK", status=200)


@app.get("/todos/<string:username>")
async def get_todos(username):
    return quart.Response(response=json.dumps(_TODOS.get(username, [])), status=200)


@app.delete("/todos/<string:username>")
async def delete_todo(username):
    _TODOS[username] = []
    return quart.Response(response="OK", status=200)


@app.get("/")
async def index():
    html = [
        "<h1>ChatGPT Plugin Example</h1>",
        "<a href='/.well-known/ai-plugin.json'>/.well-known/ai-plugin.json</a>",
        "<a href='/openapi.yaml'>/openapi.yaml</a>",
    ]
    return quart.Response("<br>".join(html), mimetype="text/html")


@app.get("/logo.png")
async def plugin_logo():
    filename = "logo.png"
    return await quart.send_file(filename, mimetype="image/png")


@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    base = f"{request.scheme}://{request.headers['Host']}"
    text: str = generate_wellknown_config(base)
    return quart.Response(text, mimetype="text/json")


@app.get("/openapi.yaml")
async def openapi_spec():
    base = f"{request.scheme}://{request.headers['Host']}"
    text: str = generate_openapi(base)
    return quart.Response(text, mimetype="text/yaml")


def main():
    app.run(debug=True, host="0.0.0.0", port=5003)


if __name__ == "__main__":
    main()
