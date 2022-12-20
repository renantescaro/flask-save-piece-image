from waitress import serve
from flaskr import create_app
from flaskr.utils.config import Config


app = create_app()
serve(
    app,
    host=Config.get('APPLICATION_IP'),
    port=Config.get('APPLICATION_PORT')
)
