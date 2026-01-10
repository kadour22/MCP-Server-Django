<!-- Tasks list json format -->
{
  "name": "task_list",
  "arguments": {}
}
NB : expected Response => 
{
  "content": [
    {
      "type": "json",
      "data": [
        {
          "id": 1,
          "title": "Test MCP with Postman",
          "completed": false,
          "created_at": "..."
        }
      ]
    }
  ]
}

<!-- Create task json format -->
{
  "name": "task_create",
  "arguments": {
    "title": "Test MCP with Postman"
  }
}

NB : expected Response => 
{
  "content": [
    {
      "type": "json",
      "data": {
        "id": 1,
        "title": "Test MCP with Postman",
        "completed": false,
        "created_at": "2026-01-10T10:15:00Z"
      }
    }
  ]
}

<!-- Delete task json format -->
{
  "name": "task_delete",
  "arguments": {
    "id": 1
  }
}
NB : expected Response => 
{
  "content": [
    {
      "type": "json",
      "data": {
        "deleted": true
      }
    }
  ]
}


<!-- Update task json format -->
{
  "name": "task_update",
  "arguments": {
    "id": 1,
    "completed": true
  }
}
