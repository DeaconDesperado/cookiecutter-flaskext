from flask import Flask
from {{cookiecutter.repo_name}} import {{cookiecutter.ext_name|title}}

app = Flask(__name__)
ext = {{cookiecutter.ext_name|title}}(app)

app.debug = True
app.run(use_debugger=True, use_reloader=True)
