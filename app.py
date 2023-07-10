import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://localhost:5000/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

@app.route('/hello', methods=['GET'])
def hello():
    name = request.args['name']
    return f"Hello {name}"

@app.route('/goodbye', methods=['POST'])
def goodbye():
    name = request.form['name'] # The value is 'Alice'

    # Send back a fond farewell with the name
    return f"Goodbye {name}!"

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    message = request.form['message']
    return f'Thanks {name}, you sent this message: "{message}"'

@app.route('/wave', methods=['GET'])
def wave():
    NAME = request.args['name']
    return f"I am waving at {NAME}"
# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

@app.route('/names', methods=['GET'])
def names():
    name = request.args['add']
    split_names = name.split(',')
    if len(split_names) == 1:
        names_list = "Julia, Alice, Karim"
        return f"{names_list}, {name}"
    else:
        names_list = "Julia,Alice,Karim"
        split_list = names_list.split(",")
        for name in split_names:
            split_list.append(name)
        print(split_list)
        sort_names = sorted(split_list)
        print(sort_names)
        return ", ".join(sort_names)

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

