import urllib.request,json
from .models import Sources
#Getting the NEWS_API_KEY
api_key = None
#Getting the news base_url
base_url =None
# a function that replaces the empty variables we created with the configuration objects we created and pass in the app instance
source_url =None
def  configure_request(app):
    #we make the variables global for them to be accessed by the whole application
    global api_key,base_url
    api_key= app.config['NEWS_API_KEY']
    base_url= app.config['NEWS_API_BASE_URL']

def get_sources(country,category):
    '''
    function that gets the json response and converts to python dictionary
    '''
    get_sources_url =base_url.format(country,category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
         get_sources_data =url.read()
         get_sources_reponse= json.loads(get_sources_data)

         sources_results = None
         if get_sources_reponse['sources']:
             sources_results_list = get_sources_reponse['sources']
             sources_results = process_sources(sources_results_list)
    return sources_results
def process_sources(sources_list):
    sources_results = []
    for source_item in sources_list:
        id = source_item.get('id')
        name= source_item.get('name')
        description=source_item.get('description')
        url=source_item.get('url')
        category = source_item.get('category')
        country = source_item.get('country')
        '''
        we check if the source items have posters if they do the source object is created
        '''
        if url:
            source_object= Sources(id,name,description,url,category,country)
            sources_results.append(source_object)
    return sources_results
