from flask import current_app, jsonify, request
from app.auth import bp, service
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from app.auth.dto import LoginDto, TokenResponseDto
from pydantic import ValidationError

@bp.route("/auth", methods=["POST"])
def post_auth():
    """
    Autenticación de usuario
    ---
    tags:
      - Autenticación
    parameters:
      - name: body
        in: body
        required: true
        description: Credenciales de usuario
        schema:
          $ref: '#/definitions/LoginDto'
    responses:
      200:
        description: Token de acceso generado exitosamente
        schema:
          $ref: '#/definitions/TokenResponseDto'
      400:
        description: Datos de entrada inválidos
        schema:
          $ref: '#/definitions/ErrorResponse'
      401:
        description: Credenciales inválidas
      500:
        description: Error interno del servidor
    """
    try:
        # Validar datos de entrada con Pydantic
        login_data = LoginDto(**request.json)
        
        # Autenticar usuario
        user = service.signin(login_data.model_dump())
        
        # Generar token
        access_token = create_access_token(identity=user["username"])
        
        # Crear respuesta usando DTO
        token_response = TokenResponseDto(
            access_token=access_token,
            expires_in=current_app.config.get("JWT_ACCESS_TOKEN_EXPIRES")
        )
        
        return jsonify(token_response.model_dump())
    except ValidationError as e:
        return jsonify({"statusCode": 400, "message": "Datos inválidos", "errors": e.errors()}), 400

@bp.route("/users", methods=["GET"])
@jwt_required()
def get_users():
    """
    Obtener lista de usuarios
    ---
    tags:
      - Usuarios
    security:
      - Bearer: []
    responses:
      200:
        description: Lista de usuarios obtenida exitosamente
        schema:
          type: array
          items:
            $ref: '#/definitions/UserDto'
      401:
        description: Token inválido o no proporcionado
      500:
        description: Error interno del servidor
    """
    current_user = get_jwt_identity()
    print(current_user)

    users = service.get_users()

    return jsonify(users)