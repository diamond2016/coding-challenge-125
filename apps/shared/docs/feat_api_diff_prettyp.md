Create an API in backend

Supported by fastApi infrasttucture,

POST
/api/diff/
body
diff-request: {"string_a": "content_of_string_a", "string_b": "content_of_string_b"}

Returns 
diff-response: {"diff": "content of myers_diff.dif_prettyp(string_a, string_b)"}

{
    "string_a": "content_of_string_a",
    "string_b": "content_of_string_b"
}
{
    "diff": "content of myers_diff.dif_prettyp(string_a, string_b)"
}

Uses Pydantic models for automatic request/response validation
Returns None if no diff is found (empty strings)
The diff is ANSI color-coded:
Red (\033[31m) for deleted characters
Green (\033[32m) for inserted characters
Cyan (\033[36m) for equal characters

curl -X POST http://localhost:8000/api/diff/ \
  -H "Content-Type: application/json" \
  -d '{"string_a": "ABCD", "string_b": "ABECD"}'

The API will start on http://localhost:8000 and you can also access the Swagger UI at http://localhost:8000/docs to test it interactively

http://localhost:8000/docs swagger