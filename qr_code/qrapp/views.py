import qrcode
import io
import time
from django.shortcuts import render
from django.http import StreamingHttpResponse


def generate_qr_code(token):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(token)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    buffer = io.BytesIO()
    img.save(buffer)
    buffer.seek(0)
    return buffer


def qr_code_view(request):
    token = 'https://t.me/AlabugaQRBot'

    def stream_response():
        while True:
            time.sleep(1)
            new_qr_code_data = generate_qr_code(token).getvalue()
            yield b'--frame\r\n'
            yield b'Content-Type: image/png\r\n\r\n'
            yield new_qr_code_data
            yield b'\r\n\r\n'

    response = StreamingHttpResponse(stream_response(), content_type='multipart/x-mixed-replace; boundary=frame')
    return response


def home(request):
    return render(request, 'home.html')
