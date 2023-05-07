from flask import render_template, jsonify, Blueprint
from flaskr.services.check_piece import CheckPiece
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
        imagens, number_read=ListImages().execute()
        return render_template(
            'inicial.html',
            titulo='inicial',
            lista_images=imagens,
            number_read=number_read
        )

    @staticmethod
    @bp.route('/amount-characters', methods=['GET'])
    def amount_characters():
        return jsonify(CheckPiece().amount_characters())

    @staticmethod
    @bp.route('/five-characters-less', methods=['GET'])
    def five_characters_less():
        return jsonify(CheckPiece().five_characters_less())
