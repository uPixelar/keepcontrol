from server.app import create_app
import os, socket, qrcode, io

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("1.1.1.1", 80))
    return s.getsockname()[0]

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

app, socketio = create_app(ROOT_DIR)

TEXT_ART = """
  
  ██╗  ██╗███████╗███████╗██████╗  ██████╗ ██████╗ ███╗   ██╗████████╗██████╗  ██████╗ ██╗     
  ██║ ██╔╝██╔════╝██╔════╝██╔══██╗██╔════╝██╔═══██╗████╗  ██║╚══██╔══╝██╔══██╗██╔═══██╗██║     
  █████╔╝ █████╗  █████╗  ██████╔╝██║     ██║   ██║██╔██╗ ██║   ██║   ██████╔╝██║   ██║██║     
  ██╔═██╗ ██╔══╝  ██╔══╝  ██╔═══╝ ██║     ██║   ██║██║╚██╗██║   ██║   ██╔══██╗██║   ██║██║     
  ██║  ██╗███████╗███████╗██║     ╚██████╗╚██████╔╝██║ ╚████║   ██║   ██║  ██║╚██████╔╝███████╗
  ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝      ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝                                                                                             
"""

print(TEXT_ART, end="")
qr = qrcode.QRCode()
qr.add_data(f"http://{get_ip_address()}:9680")
f = io.StringIO()
qr.print_ascii(f)
f.seek(0)
print(f.read(), end="")
print("Scan the qrcode to control the PC or")
print(f"Enter 'http://{get_ip_address()}:9680' on your browser")

socketio.run(app, "0.0.0.0", 9680)