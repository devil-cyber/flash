# Welcome to Flash 👋
![Version](https://img.shields.io/badge/version-1-blue.svg?cacheSeconds=2592000)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](#)

> Flash is a Python based web framework that has been created to 
learn how web framework work under the hood

## Quick Start

Install it:

```bash
pip install flash-web-framework-1.0.0
```

Basic Usage:

```python
# app.py
from flash import Flash

app = Flash()


@app.route("/")
def home(req, resp):
    resp.text = "Hello, this is a home page."


@app.route("/about")
def about_page(req, resp):
    resp.text = "Hello, this is an about page."


@app.route("/{age:d}")
def tell_age(req, resp, age):
    resp.text = f"Your age is {age}"


@app.route("/{name:l}")
class GreetingHandler:
    def get(self, req, resp, name):
        resp.text = f"Hello, {name}"


@app.route("/show/template")
def handler_with_template(req, resp):
    resp.html = app.template("example.html", context={"title": "Awesome Framework", "body": "welcome to the future!"})


@app.route("/json")
def json_handler(req, resp):
    resp.json = {"this": "is JSON"}


@app.route("/custom")
def custom_response(req, resp):
    resp.body = b'any other body'
    resp.content_type = "text/plain"
```

Start:

```bash
gunicorn app:app
```

## Handlers

If you use class based handlers, only the methods that you implement will be allowed:

```python
@app.route("/{name:l}")
class GreetingHandler:
    def get(self, req, resp, name):
        resp.text = f"Hello, {name}"
```

This handler will only allow `GET` requests. That is, `POST` and others will be rejected. The same thing can be done with
function based handlers in the following way:

```python
@app.route("/", methods=["get"])
def home(req, resp):
    resp.text = "Hello, this is a home page."
```

Note that if you specify `methods` for class based handlers, they will be ignored.

## Unit Tests

The recommended way of writing unit tests is with [pytest](https://docs.pytest.org/en/latest/). There are two built in fixtures
that you may want to use when writing unit tests with Flash. The first one is `app` which is an instance of the main `Flash` class:

```python
def test_route_overlap_throws_exception(app):
    @app.route("/")
    def home(req, resp):
        resp.text = "Welcome Home."

    with pytest.raises(AssertionError):
        @app.route("/")
        def home2(req, resp):
            resp.text = "Welcome Home2."
```

The other one is `client` that you can use to send HTTP requests to your handlers. It is based on the famous [requests](http://docs.python-requests.org/en/master/) and it should feel very familiar:

```python
def test_parameterized_route(app, client):
    @app.route("/{name}")
    def hello(req, resp, name):
        resp.text = f"hey {name}"

    assert client.get(url("/matthew")).text == "hey matthew"
```

Note that there is a `url()` function used. It is used to generate the absolute url of the request given a relative url. Import it before usage:

```python
from flash.utils.tests import url
```

## Templates

The default folder for templates is `templates`. You can change it when initializing the main `Flash()` class:

```python
app = Flash(templates_dir="templates_dir_name")
```

Then you can use HTML files in that folder like so in a handler:

```python
@app.route("/show/template")
def handler_with_template(req, resp):
    resp.html = app.template("example.html", context={"title": "Awesome Framework", "body": "welcome to the future!"})
```

## Static Files

Just like templates, the default folder for static files is `static` and you can override it:

```python
app = Flash(static_dir="static_dir_name")
```

Then you can use the files inside this folder in HTML files:

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <title>{{title}}</title>

  <link href="/static/main.css" rel="stylesheet" type="text/css">
</head>

<body>
    <h1>{{body}}</h1>
    <p>This is a paragraph</p>
</body>
</html>
```

## Custom Exception Handler

Sometimes, depending on the exception raised, you may want to do a certain action. For such cases, you can register an exception handler:

```python
def on_exception(req, resp, exception):
    if isinstance(exception, HTTPError):
        if exception.status == 404:
            resp.text = "Unfortunately the thing you were looking for was not found"
        else:
            resp.text = str(exception)
    else:
        # unexpected exceptions
        if app.debug:
            debug_exception_handler(req, resp, exception)
        else:
            print("These unexpected exceptions should be logged.")

app = Flash(debug=False)
app.add_exception_handler(on_exception)
```

This exception handler will catch 404 HTTPErrors and change the text to `"Unfortunately the thing you were looking for was not found"`. For other HTTPErrors, it will simply
show the exception message. If the raised exception is not an HTTPError and if `debug` is set to True, it will show the exception and its traceback. Otherwise, it will log it.

## Middleware

You can create custom middleware classes by inheriting from the `flash.middleware.Middleware` class and override its two methods
that are called before and after each request:

```python
from flash import Flash
from flash.middleware import Middleware

app = Flash()


class SimpleCustomMiddleware(Middleware):
    def process_request(self, req):
        print("Before dispatch", req.url)

    def process_response(self, req, res):
        print("After dispatch", req.url)


app.add_middleware(SimpleCustomMiddleware)
```

### ORM

Flash has a built-in ORM. Here is how you can use it:


```python
# connect to database
from flash.orm import Database

db = Database("./test.db")

# define tables
class Author(Table):
    name = Column(str)
    age = Column(int)

class Book(Table):
    title = Column(str)
    published = Column(bool)
    author = ForeignKey(Author)

# create tables
db.create(Author)
db.create(Book)

# create an instance and insert a row
greg = Author(name="George", age=13)
db.save(greg)

# fetch all rows
authors = db.all(Author)

# get a specific row
author = db.get(Author, 47)

# save an object with a foreign key
book = Book(title="Building an ORM", published=True, author=greg)
db.save(book)

# fetch an object with a forein key
print(Book.get(55).author.name)

# update an object
book.title = "How to build an ORM"
db.update(book)

# delete an object
db.delete(Book, id=book.id)
```

## Features

- WSGI compatible
- Built-in ORM
- Parameterized and basic routing
- Class based handlers
- Test Client
- Support for templates
- Support for static files
- Custom exception handler
- Middleware

## Author

👤 **Manikant Kumar**

* Website: https://devil-cyber.github.io/CodingSpace/
* Github: [@devil-cyber](https://github.com/devil-cyber)
* LinkedIn: [@mani360](https://linkedin.com/in/mani360)

## Show your support

Give a ⭐️ if this project helped you!


