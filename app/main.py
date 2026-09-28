"""Flask web layer that exposes the calculator over HTTP."""

from flask import Flask, jsonify, request

from app import __version__
from app.calculator import OPERATIONS


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/")
    def index():
        return jsonify(
            message="Welcome to the Calculator API",
            version=__version__,
            operations=list(OPERATIONS),
        )

    @app.get("/health")
    def health():
        return jsonify(status="ok")

    @app.get("/calculate/<operation>")
    def calculate(operation: str):
        func = OPERATIONS.get(operation)
        if func is None:
            return jsonify(error=f"Unknown operation '{operation}'"), 404

        try:
            a = float(request.args["a"])
            b = float(request.args["b"])
        except KeyError:
            return jsonify(error="Query params 'a' and 'b' are required"), 400
        except ValueError:
            return jsonify(error="'a' and 'b' must be numbers"), 400

        try:
            result = func(a, b)
        except ValueError as exc:
            return jsonify(error=str(exc)), 400

        return jsonify(operation=operation, a=a, b=b, result=result)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
