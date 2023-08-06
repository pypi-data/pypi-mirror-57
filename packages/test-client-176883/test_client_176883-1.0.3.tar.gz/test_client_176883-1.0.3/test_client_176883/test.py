from test_client_176883 import client
from test_client_176883 import add_item

item = add_item.AddItem(item_id='3', cat_id='1')
# print(item.get_body_parameters())
c = client.Client(app_key="1", app_id="1")
print(c.send(item))
