class Sources:
    '''
    sources class to define the newssources objects
    '''
    def __init__(self,id,name,url,category,country,description):
        self.id=id
        self.name=name
        self.url=url
        self.category=category
        self.country=country
        self.description=description
class Articles:
    '''
    an article class to define the article objects
    '''
    def __init__(self,name,publishedAt,title,url,urlToImage,description,id= None,author=None):
        self.id=id
        self.name=name
        self.author=author
        self.publishedAt=publishedAt
        self.title=title
        self.url=url
        self.urlToImage=urlToImage
        self.description=description
