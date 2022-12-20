from flask import render_template, jsonify, Blueprint
from flaskr.services.list_images import ListImages
from flaskr.utils.config import Config

bp = Blueprint(
    'inical',
    __name__,
    template_folder='templates' 
)

class InicialCtrl:
    @bp.route('/', methods=['GET'])
    def inicial_template():
        imagens=ListImages().execute()
        return render_template(
            'inicial.html',
            titulo='inicial',
            lista_images=imagens,
            qtd=len(imagens),
        )

    @bp.route('/json', methods=['GET'])
    def inicial_json():
        return jsonify({'pagina':'inicial'})
