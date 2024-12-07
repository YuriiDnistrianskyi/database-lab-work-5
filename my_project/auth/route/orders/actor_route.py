from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import actor_controller
from my_project.auth.domain.orders.actor import Actor

actor_bp = Blueprint('Actor', __name__, url_prefix='/actor')

@actor_bp.get('')
def get_all_actor() -> Response:
    actors = actor_controller.find_all()
    actor_dto = [actor.put_into_dto() for actor in actors]
    return make_response(jsonify(actor_dto), HTTPStatus.OK)


@actor_bp.post('')
def create_actor() -> Response:
    data = request.get_json()
    actor = Actor.create_from_dto(data) #
    actor_controller.create_actor(actor)
    return make_response(jsonify(actor.put_into_dto()), HTTPStatus.CREATED )


@actor_bp.get('/<int:actor_id>')
def get_actor(actor_id: int) -> Response:
    actor = actor_controller.find_actor_by_id(actor_id)
    return make_response(jsonify(actor.put_into_dto()), HTTPStatus.OK)


@actor_bp.put('/<int:actor_id>')
def update_actor(actor_id: int) -> Response:
    data = request.get_json()
    actor = Actor.create_from_dto(data) #
    actor_controller.update_actor(actor_id, actor)
    return make_response(jsonify({"messange": "Actor updated"}), HTTPStatus.OK)


@actor_bp.delete('/<int:actor_id>')
def delete_actor(actor_id: int) -> Response:
    actor_controller.delete_actor(actor_id)
    return make_response(jsonify({"messange": "Actor deleted"}), HTTPStatus.OK)
