import urllib.request,json
from .models import Sources  
#Getting the NEWS_API_KEY
api_key = None
#Getting the news base_url
base_url =None
# a function that replaces the empty variables we created with the configuration objects we created and pass in the app instance
def  configure_request(app):
    #we make the variables global for them to be accessed by the whole application
    global api_key,base_url
    api_key= app.config['NEWS_API_KEY']
    base_url= app.config['NEWS_API_BASE_URL']

def get_sources(sources):
    '''
    function that gets the json response and converts to python dictionary
    '''
