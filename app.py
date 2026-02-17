from sys import excepthook

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.before_request
def before_request():
    print(request.method,request.path)
@app.after_request
def after_request(response):
    response.headers["X-Custom-Header"]="FlaskRocks"
    return response
@app.teardown_request
def teardown_request(exception):
    if exception is not None:
        print("Exception during request:", exception)
    else:
        print("Request finished OK")


@app.route("/", methods=["GET"])
def home():
    return "<h1>Welcome to My Flask API!</h1>"
@app.route("/about", methods=["GET"])
def about():
    return jsonify({"name": "Tehilla Sebrow", "course":"MCON-357", "semester":"Spring 2026"})

@app.route("/greet/<name>", methods=["GET"])
def greet(name):
    return f"<h1>Welcome {name}!</h1>"

@app.route('/calculate')
def calculate():
    num1 = float(request.args.get('num1', 0))
    num2 = float(request.args.get('num2', 0))
    operation = request.args.get('operation')
    try:
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2
        else:
            return jsonify({"error": "Invalid operation"}), 400
        return jsonify({"result": result, "operation": operation})
    except Exception as e:
        # Log the exception and return an error response
        print(f"Error occurred: {e}")
        return jsonify({"error": "An error occurred during calculation"}), 500


@app.route("/echo", methods=["POST"])
def echo():
    data=request.get_json() or {}
    data["echoed"]=True
    return jsonify(data)

@app.route("/status/<int:code>", methods=["GET"])
def status(code):
    message=f"Your application ran the {code} error"
    return jsonify({"message": message}), code

if __name__ == '__main__':
    app.run(debug=True)
@app.route('/debug/routes')
def show_routes():
    routes = []
    for rule in app.url_map.iter_rules():
        routes.append({
            'endpoint': rule.endpoint,
            'methods': list(rule.methods),
            'path': str(rule)
        })
    return jsonify(routes)