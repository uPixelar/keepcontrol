from flask import Flask, render_template
from flask_socketio import SocketIO
import os, socket
from pynput.mouse import Controller as MouseController, Button

HOST_NAME = socket.gethostname()
MOUSE_ACCELERATION = 0.5

def create_app(root_dir):
    app = Flask(
        __name__,
        template_folder=os.path.join(root_dir, "templates"),
        static_folder=os.path.join(root_dir, "static"),
        static_url_path="/",
    )
    app.config["SECRET_KEY"] = "mysecretkey"

    socketio = SocketIO(app, async_mode="eventlet")
    
    mouse = MouseController()

    # Flask routes
    @app.route("/")
    def index():
        return render_template("index.html", hostname=HOST_NAME)

    # Socket routes
        
    @socketio.on("cursorMove")
    def handle_cursor(data):
        deltaX = data.get("deltaX", 0)
        deltaY = data.get("deltaY", 0)
        
        dx = deltaX + deltaX * abs(deltaX) * MOUSE_ACCELERATION
        dy = deltaY + deltaY * abs(deltaY) * MOUSE_ACCELERATION
        
        mouse.move(deltaX, deltaY)
        
    @socketio.on("mouseClick")
    def handle_click(data):
        action = data.get("action")
        button = data.get("button")
        
        if button == "left":
            if action == "press":
                mouse.press(Button.left)
            elif action == "release":
                mouse.release(Button.left)
            elif action == "click":
                mouse.click(Button.left)
        elif button == "right":
            if action == "press":
                mouse.press(Button.right)
            elif action == "release":
                mouse.release(Button.right)

    return app, socketio

