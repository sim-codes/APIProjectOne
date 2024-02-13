# API ProjectOne

This API is built using Django Rest Framework for retrieving data based on name and language parameters.

## Endpoint

The endpoint for accessing this API is: 
```
http://127.0.0.1:8000/api/
```


## Query Parameters

- **name**: The name of the data you want to retrieve.
- **language**: The language of the data you want to retrieve.

Example usage:
```
http://127.0.0.1:8000/api/?name=Test Name&language=python
```


## Response Format

The response format for a successful request is a JSON object with the following fields:

- **name**: The name of the data.
- **current_day**: The current day.
- **utc_time**: The current UTC time.
- **language**: The language of the data.
- **github_file_url**: The URL to the specific file on GitHub.
- **github_repo_url**: The URL to the GitHub repository.
- **status_code**: The HTTP status code (200 for success).

Example response:
```
json
{
    "name": "Test Name",
    "current_day": "Tuesday",
    "utc_time": "2024-02-13T22:16:59Z",
    "language": "Java",
    "github_file_url": "https://github.com/sim-codes/APIProjectOne/blob/main/api/data.py",
    "github_repo_url": "https://github.com/sim-codes/APIProjectOne",
    "status_code": 200
}
```

## Errors
In case of errors, the API will respond with an appropriate HTTP status code and an error message in the response body.