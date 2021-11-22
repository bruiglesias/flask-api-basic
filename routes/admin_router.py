# -*- coding: utf-8 -*-

from flask import render_template


def create_admin_routes(app):

    @app.route('/admin')
    def main():
        return render_template('one_template.html', title="Página Administrativa") 
