from time import sleep
from json import dumps
from kafka import KafkaProducer
from app.models import Shop, Product
from app import create_app
from sqlalchemy import func
import datetime
import snowflake.connector
import random

USER=''
PASSWORD=''
ACCOUNT=''
WAREHOUSE=''
DATABASE=''
SCHEMA=''

app = create_app()
app.app_context().push()

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

conn = snowflake.connector.connect(
                user=USER,
                password=PASSWORD,
                account=ACCOUNT,
                warehouse=WAREHOUSE,
                database=DATABASE,
                schema=SCHEMA
                )

cs = conn.cursor()


while True:
    shop_id = Shop.query.order_by(func.random()).first().id
    cdatetime = datetime.datetime.now()
    product_id = Product.query.order_by(func.random()).first().id
    value = round(random.uniform(0.5, 40),2)
    qty = random.randint(1, 20)
    data = {
        'shop_id': shop_id,
        'datetime': cdatetime,
        'product_id': product_id,
        'value': value,
        'qty': qty
    }
    producer.send('numtest', value=dumps(data, indent=4, default=str))
    sleep(1)
