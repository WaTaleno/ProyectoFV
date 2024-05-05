from flask import abort, render_template
from flask_socketio import send
from app import socketio

from app.models import Post
from . import public_bp


@public_bp.route("/")
def index():
    posts = Post.get_all()
    return render_template("public/index.html", posts=posts)


@public_bp.route("/p/<string:slug>/")
def show_post(slug):
    post = Post.get_by_slug(slug)
    if post is None:
        abort(404)
    return render_template("public/post_view.html", post=post)


# Esta ruta manejará los mensajes enviados desde el cliente a través de Socket.IO
@socketio.on("message")  # Decorador para manejar el evento "message"
def handle_message(message):
    print("Mensaje recibido: " + message)
    if message != "Usuario conectado!":
        send(message, broadcast=True)

@public_bp.route("/chat")
def chat():
    return render_template("public/chat.html")

