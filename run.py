from app import create_app, db
from app.models import Product, Shop, Receipt

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Product': Product, 'Shop': Shop, 'Receipt': Receipt}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')