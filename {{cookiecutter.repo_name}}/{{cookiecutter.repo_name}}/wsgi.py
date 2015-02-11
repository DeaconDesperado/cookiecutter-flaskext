from {{cookiecutter.repo_name}}.app import create_app
import os
os.environ['APP_CONFIG'] = "ProductionConfig"

app = create_app()
