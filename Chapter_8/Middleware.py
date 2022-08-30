from flask import Request
from Services.JWTService import JWTService
from werkzeug import exceptions


class Middleware:
    def __init__(self, jwt_service: JWTService):
        self.unauthenticated_route_names = {"/api/auth/login", "/api/auth/sing_up"}
        self.jwt_service = jwt_service

    def auth(self, request: Request):
        is_route_unauthenticated = request.path in self.unauthenticated_route_names

        if is_route_unauthenticated:
            return None

        if "token" in request.headers:
            token = request.headers['token']
            is_valid = self.jwt_service.is_valid(token)
            if is_valid:
                return None
            else:
                return exceptions.Unauthorized()

        return exceptions.Unauthorized()
