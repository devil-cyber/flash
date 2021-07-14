from flash import Flash

app = Flash(debug=True)

@app.route("/",methods=['get'])
def home(req,resp):
    data = {'messsage':'hello','status':200}
    # print('manikant',req)
    # resp.html = app.template("test.html", context={"title": "Flash Framework", "body": "welcome to the new framework"})
    resp.json = data
    print(req)
    # print(req.request)
    if req.method=="POST":
        print('POST request',req.POST['manikant'])
        resp.json=req.POST['manikant']
    if req.method=="GET":
        print('This is get request')