import yaml


def generate_openapi(base_endpoint: str) -> str:
    obj = {
        "components": {
            "schemas": {
                "addTodoRequest": {
                    "required": ["todo"],
                    "properties": {
                        "todo": {
                            "type": "string",
                            "description": "The todo to add to the list.",
                        }
                    },
                    "type": "object",
                },
                "getTodosResponse": {
                    "properties": {
                        "todos": {
                            "description": "The list of todos.",
                            "items": {"type": "string"},
                            "type": "array",
                        }
                    },
                    "type": "object",
                },
            }
        },
        "info": {
            "description": 'A plugin that allows the user to create and manage a TODO list using ChatGPT. If you do not know the user\'s username, ask them first before making queries to the plugin. Otherwise, use the username "global".',
            "title": "TODO Plugin",
            "version": "v1",
        },
        "openapi": "3.0.1",
        "paths": {
            "/todos/{username}": {
                "delete": {
                    "operationId": "deleteTodo",
                    "parameters": [
                        {
                            "description": "The name of the user.",
                            "in": "path",
                            "name": "username",
                            "required": True,
                            "schema": {"type": "string"},
                        }
                    ],
                    "responses": {"200": {"description": "OK"}},
                    "summary": "Delete a todo from the list",
                },
                "get": {
                    "operationId": "getTodos",
                    "parameters": [
                        {
                            "description": "The name of the user.",
                            "in": "path",
                            "name": "username",
                            "required": True,
                            "schema": {"type": "string"},
                        }
                    ],
                    "responses": {
                        "200": {
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/getTodosResponse"
                                    }
                                }
                            },
                            "description": "OK",
                        }
                    },
                    "summary": "Get the list of todos",
                },
                "post": {
                    "operationId": "addTodo",
                    "parameters": [
                        {
                            "description": "The name of the user.",
                            "in": "path",
                            "name": "username",
                            "required": True,
                            "schema": {"type": "string"},
                        }
                    ],
                    "requestBody": {
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/addTodoRequest"
                                }
                            }
                        },
                        "required": True,
                    },
                    "responses": {"200": {"description": "OK"}},
                    "summary": "Add a todo to the list",
                },
            }
        },
        "servers": [{"url": base_endpoint}],
    }

    return yaml.dump(obj, Dumper=yaml.CDumper)


if __name__ == "__main__":
    print(generate_openapi("http://127.0.0.1"))
