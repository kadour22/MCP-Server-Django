TOOLS = [
    {
        "name": "task_create",
        "description": "Create a task",
        "input_schema": {
            "type": "object",
            "properties": {
                "title": {"type": "string"}
            },
            "required": ["title"]
        }
    },
    {
        "name": "task_list",
        "description": "List tasks",
        "input_schema": {"type": "object", "properties": {}}
    },
    {
        "name": "task_get",
        "description": "Get task by id",
        "input_schema": {
            "type": "object",
            "properties": {"id": {"type": "integer"}},
            "required": ["id"]
        }
    },
    {
        "name": "task_update",
        "description": "Update a task",
        "input_schema": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "title": {"type": "string"},
                "completed": {"type": "boolean"}
            },
            "required": ["id"]
        }
    },
    {
        "name": "task_delete",
        "description": "Delete a task",
        "input_schema": {
            "type": "object",
            "properties": {"id": {"type": "integer"}},
            "required": ["id"]
        }
    }
]
