### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

Python is a backend language, JS is mainly one of the frontend languages.



- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

One way to try to get a missing key without crashing the program is to use the get() method of the dictionary. For example, you can use dictionary.get("c") which will return None if the key "c" is not found in the dictionary.

Another way is to use a try-except block to catch the KeyError that would be raised if the key is not found. For example:

try:
    value = dictionary["c"]
except KeyError:
    value = None



- What is a unit test?
  
This is testing a unit of a code seperately and independently (for example a function).



- What is an integration test?
  
This is a testing if different parts of the code work together as expected.



- What is the role of web application framework, like Flask?
  
Flask makes it easier to create a web application by providing tools and libraries.



- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

The URL parameter is a subject of the page and the query parmeter is a specified way. If for example there are a lot of different options of food it's better to use the query parmeter because this way we dont have to set a lot of different routes, we can just set it as parameters.



- How do you collect data from a URL placeholder parameter using Flask?
  
@app.route('/foods/<food_type>')
def show_food(food_type):
    return f"You selected {food_type}"



- How do you collect data from the query string using Flask?
  
For a url like '/search?term=fun'
@app.route("/search")
def search():
    term = request.args.get("term")
    return f"<h1>Searching for {term}</h1>"


    

- How do you collect data from the body of the request using Flask?
  
@app.route("/add-comment", methods=["POST"])
def add_comment():
    comment = request.form["comment"]
    return f'<h1>Received "{comment}".</h1>'




- What is a cookie and what kinds of things are they commonly used for?
  
A cookie is name/value pair that is stored in the browser. It is used to save the information so the next time when the user goes to a website, the browser remembers where the user stopped and what he did.




- What is the session object in Flask?
  
In Flask, the session object is a built-in part of the Flask framework that allows you to store data that is associated with a specific user's session.




- What does Flask's `jsonify()` do?

Flask's jsonify() is a function that is used to convert Python dictionaries and other objects into JSON (JavaScript Object Notation) format and create a Flask response object with the appropriate Content-Type header for JSON.
