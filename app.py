

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return "<h1>Welcome to My Flask API!</h1>"
@app.route("/about", methods=["GET"])
def about():
    return jsonify({"name": "Tehilla Sebrow", "course":"MCON-357", "semester":"Spring 2026"})

@app.route("/greet/<name>", methods=["GET"])
def greet(name):
    return f"<h1>Welcome {name}!</h1>"

@app.route("/calculate", methods=["GET"])
def calculate():
    num1=float(request.args.get("num1"))
    num2=float(request.args.get("num2"))
    operation=request.args.get("operation")
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return jsonify({"error":"Cannot divide by 0"})
        else:
            result= num1 /num2
    return jsonify({"result": result})

@app.route("/echo", methods=["POST"])
def echo():
    data=request.get_json() or {}
    data["echoed"]=True
    return jsonify(data)

@app.route("/status/<int:code>", methods=["GET"])
def status(code):
    message=f"Your application ran the {code} error"
    return jsonify({"message": message}), code

