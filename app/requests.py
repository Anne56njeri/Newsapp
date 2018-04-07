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
    get_sources_url =base_url.format(sources,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
         get_sources_data =url.read()
         get_sources_reponse= json.loads(get_sources_data)

        sources_results = None
        if get_sources_reponse['results']:
            sources_results_list = get_sources_reponse['results']
            sources_results = process_sources(sources_results_list)
    return sources_results
def process_sources(sources_results):
    sources_results = []
    for source_item in sources_results:
        id = source_item.get('id')
        title= source_item.get('title')
        overview = source_item.get('overview')
        image = source_item.get('image_path')
        if image:
            source_object= Sources(id,title,overview,image)
            sources_results.append(source_object)
    return sources_results        
