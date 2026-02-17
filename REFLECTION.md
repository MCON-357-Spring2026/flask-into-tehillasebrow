What does the @app.route() decorator actually do?
It connects the URL to function. It’s basically a dictionary of routes.

How does Flask know which function to call when a request arrives?
It checks the URL, the HTTP method, and it calls the matching function

What's the difference between route parameters (<name>) and query parameters (?key=value)?
route parameters are part of the url structure and Flask extracts it automatically. Query parameters are optional and its used for filtering or options and sent after a '?'

Why do we need to use request.get_json() for POST requests but request.args.get() for GET?
Because the data is stored differently. In a GET request, the data is part of the url. Flask stores it in request.args. In POST, the data is in the request body, not the URL, so you have to parse it using request.get_json()


What happens if you try to access request.args outside a request context?
You'll get a RuntimeError: Working outside of request context. Outside a route, there is no active request.
