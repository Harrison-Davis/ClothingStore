



class Cart():
    """
    A base Cart class, providing some default behaviors that can be inherited or overridden, as necessary
    """

    def __init__(self, request):  # when we create new instance of Cart, this function will be ran to either retreive users basket, or build a new one
        self.session = request.session  
        cart = self.session.get('skey')  
        if 'skey' not in request.session:
            cart = self.session['skey'] = {'number': 1231231}  
        self.cart = cart