from flask import render_template,request,url_for
from . import main
from .. request import get_sources
from ..models import Sources

@main.route('/')
def index():
    business = get_sources('us', 'business')
    sports =get_sources('us','sports')
    entertainment=get_sources('us','entertainment')
    health=get_sources('us','health')

    title = 'Home - welcome to Newsapp'
    return render_template('index.html', title = title ,business = business, sports=sports,entertainment=entertainment,health=health)
