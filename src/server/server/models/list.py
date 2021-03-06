class List:
    '''Represents one List'''

    def __init__(self, title, id='', inbox=False, revision=1):
        self.id = id
        self.title = title
        self.revision = revision
        self.inbox = inbox

    @staticmethod
    def fromDict(dict):
        try:
            l = List(
                dict['title'],
                id=dict['id'],
                revision=int(dict['revision']),
                inbox=dict['inbox'] != 0  # if 0 then False
            )
            return l
        except Exception as e:
            return None