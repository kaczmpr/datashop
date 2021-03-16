from kafka import KafkaConsumer
from json import loads
from app.models import Receipt
from app import db, create_app
import ast

app = create_app()
app.app_context().push()

consumer = KafkaConsumer('numtest', bootstrap_servers=['localhost:9092'], auto_offset_reset='earliest',
                         enable_auto_commit=True, group_id='my-group-snowflake',
                         value_deserializer=lambda x: loads(x.decode('utf-8')))


for message in consumer:
    message = message.value
    data = ast.literal_eval(message)
    receipt = Receipt(data.get('shop_id'), data.get('datetime'), data.get('product_id'), data.get('value'),
                      data.get('qty'))
    db.session.add(receipt)
    db.session.commit()