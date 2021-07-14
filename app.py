from Flash import Flash

app = Flash()

@app.route("/home")
def home(resp,req):
    resp.text = "Hello world!"