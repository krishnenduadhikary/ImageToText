from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from ocr import extract_text
from datetime import datetime

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp', 'bmp'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    text = None
    timestamp = None
    if request.method == 'POST':
        file = request.files['image']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path)
            text = extract_text(path)
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        else:
            text = "Invalid file type. Please upload a JPG, PNG, WEBP, or BMP image."
    return render_template('index.html', text=text, timestamp=timestamp)

if __name__ == '__main__':
    app.run(debug=True)
