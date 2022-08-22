from flask import Flask
app = Flask(__name__)

def make_bold(function):
    def wrapper_function():
        text = function()
        return f'<body><bold>{text}</bold></body>'

    return wrapper_function



@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is my first flask app!</p>' \
           '<img src="https://media.giphy.com/media/8OPbx53X3mFoWMw5aO/giphy.gif" width=200>'


@app.route("/bye")
@make_bold
def bye():
    return 'Bye!'

@app.route("/username/<path:name>")
def greeting(name):
    return f"Hello {name}!"

if __name__ == "__main__":
    app.run(debug=True)
