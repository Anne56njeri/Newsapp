from flask import render_template,request,url_for
from . import main
from .. requests import
from ..models import Sources

@main.route('/')
def index():
    business_source = get_sources('business')
    print(business_source)
    title = 'Home - welcome to Newsapp'
    return render_template('index.html' title= title ,business = business_source)
