from flask import Flask, render_template, abort, session, request, redirect
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object("{{cookiecutter.repo_name}}.config.%s" % os.environ.get("APP_CONFIG","DevelopmentConfig"))
    return app


if __name__ == '__main__':
    app = create_app()
    app.debug = True
    app.run(use_reloader=True, use_debugger=True)
