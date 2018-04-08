import urllib.request,json
from .models import Sources
from .models import Articles
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
    source_url=app.config['NEWS_SOURCES_URL']

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
def get_artlicles(id):
    '''
    we create a function that gets the articles that takes in a source's id
    '''
    get_article_url = source_url.format(id,apikey)
    with urllib.request.urlopen(get_article_url) as url:
        articles_data=url.read()
        article_details_response=json.loads(articles_data)
        articles_results = None
        if article_details_response ['articles']:
            '''
            we process the results  in response that have the articles to get details on those articles
            '''
            articles_result_list =article_details_response['articles']
            articles_results= process_articles(articles_result_list)
    return articles_results
def process_articles(article_list):
    articles_results = []
    '''
    stored information about every source
    '''
    source_dictionary ={}
    for results in articles_results:
        '''
        we loop through the articles results and get the source_item then get the source id and store it in a dictionary
        '''
        '''
        we pass in the keys using the get() to access the values
        '''
        source_id = results['source_item']
        source_dictionary['id']=source_id['id']
        source_dictionary['name']=source_id['name']
        id= source_dictionary['id']
        name= source_dictionary['name']
        author=results.get('author')
        publishedAt=results.get('publishedAt')
        title=results.get('title')
        url=result.get('url')
        urlToimage=results.get('urlToimage')
        description=results.get('description')
        '''
        to avoid errors we first check if it has a url to the image to avoid errors
        '''

        if urlToimage:
            source_object =Articles(id,name,author,publishedAt,title,url,urlToimage,description)
            articles_results.append(source_object)
    return articles_results
