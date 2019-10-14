class News:
    '''
    News class to  define object
    '''
    def __init__(self, author, title, description, url, urlToImage, content):
        self.author = author 
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.content = content

class Sources:
    '''
    Sources class to define object
    '''

    def __init__(self, id, name, description, url, category):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category