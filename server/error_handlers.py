from werkzeug.exceptions import NotFound, BadRequest
from flask import make_response

#  e => exception raised, triggering the handler to be called

# capture any 404s detected by Flask app, and return a message provided in the response body
@app.errorhandler(NotFound)
def handle_not_found(e):
    response_body = "Not Found: The requested resource does not exist."
    response = make_response(
        response_body, 404
    )
    return response


# werkzeug.exceptions.NotFound class - the exception that is raised when a 404 is detected.
# register it to handler

# 400
@app.errorhandler(BadRequest)
def handle_bad_request(e):
    response_body = "Bad Request: The requested cannot be handled"
    response = make_response(
        response_body, 400
    )
    return response