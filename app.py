from flask import Flask, request, send_from_directory
import qrcode
import PIL.Image as img
import gunicorn

app = Flask(__name__)
@app.route('/')
def home():
    return '<h1> Hello There! </h1>'
@app.route('/<data>')
def generate_qr(data):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=2)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save('image/qrcode.png')
    return send_from_directory(directory='./image', filename='qrcode.png', as_attachment=True)
    
if __name__ == "__main__":
    app.run()