import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello World!</h1>"


@app.route('/shops/<int:id', methods=['GET'])
def get_shops(id):
    pass


@app.route('/sales/<int:id>', methods=['GET'])
def get_sales(id):
    pass


@app.route('/receipt/<int:id', methods=['GET'])
def get_receipt(id):
    pass