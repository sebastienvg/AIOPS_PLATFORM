'''
    IndexPage.py Lib
    Written By Kyle Chen
    Version 20190401v1
'''

# import buildin pkgs
import os
from flask import render_template, Response
from flask_restful import Resource
from flask_login import login_required

## Index Class
class IndexPage(Resource):
    ## get method
    @login_required
    def get(self):
        return(Response(render_template('Index.html')))
