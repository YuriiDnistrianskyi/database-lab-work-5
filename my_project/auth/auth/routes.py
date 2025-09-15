from http import HTTPStatus
from flask_jwt_extended import create_access_token
from flask import Blueprint, request, Response, make_response, jsonify
from my_project.auth.domain.orders.Park import Park

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.post("/login")
def login() -> Response:
    data = request.get_json()
    park = Park.query.filter_by(name=data["name"]).first()
    print("Ok")
    if park is not None and park.password == data['password']:
        access_token = create_access_token(identity=str(park.id))
        return make_response(jsonify({'access_token': access_token}), HTTPStatus.OK)

    return make_response(jsonify({"message": f"Not found Park {data['name']} or bad password"}), HTTPStatus.NOT_FOUND)
