from flask import Flask, render_template, request

app = Flask(__name__)

history = []

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    error = None

    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operation = request.form["operation"]

            if operation == "add":
                result = num1 + num2
                expression = f"{num1} + {num2} = {result}"

            elif operation == "subtract":
                result = num1 - num2
                expression = f"{num1} - {num2} = {result}"

            elif operation == "multiply":
                result = num1 * num2
                expression = f"{num1} * {num2} = {result}"

            elif operation == "divide":
                if num2 == 0:
                    error = "Cannot divide by zero!"
                else:
                    result = num1 / num2
                    expression = f"{num1} / {num2} = {result}"

            if result is not None:
                history.insert(0, expression)
                if len(history) > 5:
                    history.pop()

        except ValueError:
            error = "Invalid input!"

    return render_template("index.html", result=result, history=history, error=error)

if __name__ == "__main__":
    app.run(debug=True)
