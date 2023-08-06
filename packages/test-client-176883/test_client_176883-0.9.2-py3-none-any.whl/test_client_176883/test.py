import test_client_176883.client
from test_client_176883.api_request import add_item

item = add_item.AddItem('3', '1')
# print(item.get_body_parameters())
c = client.Client("1", "1")
print(c.send(item))