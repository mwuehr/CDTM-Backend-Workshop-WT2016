NOTFOUND = '404'


class Error:
    def __init__(self, status, text):
        self.status = status
        self.text = text