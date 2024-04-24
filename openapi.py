import yaml


def generate_openapi(base_endpoint: str) -> str:
    obj = {
        "openapi": "3.0.1",
        "info": {
            "title": "TODO Plugin",
            "description": 'A plugin that allows the user to create and manage a TODO list using ChatGPT. If you do not know the user\'s username, ask them first before making queries to the plugin. Otherwise, use the username "global".',
            "version": "v1",
        },
        "servers": [{"url": base_endpoint}],
        "paths": {
            "/todos/{username}": {
                "get": {
                    "operationId": "getTodos",
                    "summary": "Get the list of todos",
                    "parameters": [
                        {
                            "in": "path",
                            "name": "username",
                            "schema": {"type": "string"},
                            "required": True,
                            "description": "The name of the user.",
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/getTodosResponse"
                                    }
                                }
                            },
                        }
                    },
                },
                "post": {
                    "operationId": "addTodo",
                    "summary": "Add a todo to the list",
                    "parameters": [
                        {
                            "in": "path",
                            "name": "username",
                            "schema": {"type": "string"},
                            "required": True,
                            "description": "The name of the user.",
                        }
                    ],
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/addTodoRequest"
                                }
                            }
                        },
                    },
                    "responses": {"200": {"description": "OK"}},
                },
                "delete": {
                    "operationId": "deleteTodo",
                    "summary": "Delete a todo from the list",
                    "parameters": [
                        {
                            "in": "path",
                            "name": "username",
                            "schema": {"type": "string"},
                            "required": True,
                            "description": "The name of the user.",
                        }
                    ],
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/deleteTodoRequest"
                                }
                            }
                        },
                    },
                    "responses": {"200": {"description": "OK"}},
                },
            }
        },
        "components": {
            "schemas": {
                "getTodosResponse": {
                    "type": "object",
                    "properties": {
                        "todos": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "The list of todos.",
                        }
                    },
                },
                "addTodoRequest": {
                    "type": "object",
                    "required": ["todo"],
                    "properties": {
                        "todo": {
                            "type": "string",
                            "description": "The todo to add to the list.",
                            "required": True,
                        }
                    },
                },
                "deleteTodoRequest": {
                    "type": "object",
                    "required": ["todo_idx"],
                    "properties": {
                        "todo_idx": {
                            "type": "integer",
                            "description": "The index of the todo to delete.",
                            "required": True,
                        }
                    },
                },
            }
        },
    }

    return yaml.dump(obj, Dumper=yaml.CDumper)


if __name__ == "__main__":
    print(generate_openapi("http://127.0.0.1"))
