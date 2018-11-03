from flask import Flask, make_response, send_file,request
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'
arg = True

CONTENT_TYPE_ARG= {
    'htm':'text/html',
    'html':'text/html',
    'gif':'image/gif',
    'txt':'text/html',
    'jpe':'image/jpeg',
    'jpeg':'image/jpeg',
    'jpg':'image/jpeg',
    'png':'image/png',
    'json':'application/json',
    'jsonp':'application/jsonp',
    'pdf':'application/pdf',
    'doc':'application/msword',
}

@app.route('/static/<filename>')
def upload_file(filename):
    if arg:

        TYPE = filename.split('.')[-1].lower()
        if TYPE in CONTENT_TYPE_ARG.keys():
            CONTENT_TYPE = CONTENT_TYPE_ARG[TYPE]
        else:
            CONTENT_TYPE = 'application/octet-stream'

        response = make_response()
        response.headers['Content-Type'] = CONTENT_TYPE
        response.headers['X-Accel-Redirect'] = '/data/{}'.format(filename)
        return response
    else:
        return 'no permissons!'

if __name__ == '__main__':
    app.run(debug=True)
