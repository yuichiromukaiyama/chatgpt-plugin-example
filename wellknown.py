import json


def generate_wellknown_config(base_endpoint: str) -> str:
    obj = {
        "schema_version": "v1",
        "name_for_human": "TODO List (no auth)",
        "name_for_model": "todo",
        "description_for_human": "Manage your TODO list. You can add, remove and view your TODOs.",
        "description_for_model": "Plugin for managing a TODO list, you can add, remove and view your TODOs.",
        "auth": {"type": "none"},
        "api": {"type": "openapi", "url": f"{base_endpoint}/openapi.yaml"},
        "logo_url": f"{base_endpoint}/logo.png",
        "contact_email": "legal@example.com",
        "legal_info_url": "http://example.com/legal",
    }

    return json.dumps(obj, ensure_ascii=False)


if __name__ == "__main__":
    print(generate_wellknown_config("http://127.0.0.1"))
