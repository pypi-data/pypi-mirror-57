class AddItem():
    def __init__(self, item_id, cat_id):
        """
        Required parameters
        """

        self.item_id = item_id
        self.cat_id = cat_id
        self.method = "POST"
        self.path =  "/reze/v1/item"
    
    def get_body_parameters(self):
        p = dict()
        p['itemId'] = self.item_id
        p['catId'] = self.cat_id
        return p