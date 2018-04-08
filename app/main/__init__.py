#Registering a blueprint
#A blue print collection of views,temlates and static files that can be applied to an app
#we use blueprints for components that are diffrent in nature for each to do a certain task
from flask import Blueprint
# intializing the blueprint class
main =Blueprint('main',__name__)
from . import views,errors
