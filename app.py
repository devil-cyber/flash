from flash import Flash

app = Flash()

@app.route("/home")
def home(req,resp):
    print('Manikant')
    print(resp)
    resp.text = "Hello world!"