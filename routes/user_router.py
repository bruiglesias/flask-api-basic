# -*- coding: utf-8 -*-

from flask import request, render_template
import json

from functions import np_encoder


def create_user_routes(app):

    @app.route('/')
    def home():
        return render_template('one_template.html', title="Página Administrativa") 

    @app.route('/main_route', methods=['POST'])
    def main_route():
        
        content = request.json
        try:
            text = content['text']
        except:
            return json.dumps({'error': "JSON mal formatado", 'route': '/main_route'}, default=np_encoder)

        if not type(text) == str:
            return json.dumps({'error': "A rota requer text que deve ser do tipo string", 'route': '/main_route'}, default=np_encoder)
        
        else:
            try:
                result = "OK"
                return json.dumps(result, default=np_encoder)
            except Exception as exception:
                return json.dumps({'error': str(exception), 'route': '/main_route'}, default=np_encoder)