import os
import requests
from behave import given, when, then

@given('a request url {endpoint}')
def step_given_request_url(context, endpoint):
    base_url = os.getenv('API_HOST', 'http://localhost:5000')
    context.request_url = f"{base_url}{endpoint}"

@given('a request json payload')
def step_given_request_json_payload(context):
    import json
    context.request_json = json.loads(context.text)

@when('the request sends GET')
def step_when_request_sends_get(context):
    response = requests.get(context.request_url)
    context.response = response

@when('the request sends POST')
def step_when_request_sends_post(context):
    response = requests.post(context.request_url, json=getattr(context, 'request_json', None))
    context.response = response

@then('the response status is {status}')
def step_then_response_status_is(context, status):
    status_map = {
        "OK": 200,
        "CREATED": 201,
        "NO_CONTENT": 204,
        "BAD_REQUEST": 400,
        "UNAUTHORIZED": 401,
        "FORBIDDEN": 403,
        "NOT_FOUND": 404,
        "CONFLICT": 409,
        "INTERNAL_SERVER_ERROR": 500
    }
    if status not in status_map:
        raise ValueError(f"Status '{status}' no está definido en status_map")
    expected_code = status_map[status]
    assert context.response.status_code == expected_code, \
        f"Expected {expected_code}, got {context.response.status_code}: {context.response.text}"