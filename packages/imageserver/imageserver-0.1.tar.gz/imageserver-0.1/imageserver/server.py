"""
Usage:
    app.py --dataroot=<> --port=<>

Options:

-h --help       Show this screen
--dataroot=<>   Path to images w.r.t root('/')
--port=<>       Port 
"""
import os
from flask import Flask, Response, request, abort, render_template_string, send_from_directory
from PIL import Image
from io import BytesIO
import docopt

args = docopt.docopt(__doc__)
dataroot = args["--dataroot"]
port = int(args["--port"])
app = Flask(__name__,static_folder="/")

WIDTH = 350
HEIGHT = 350

TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
<title></title>
<meta charset="utf-8" />
<style>
body {
    margin: 0;
    background-color: #333;
}

.image {
    display: block;
    margin: 2em auto;
    background-color: #444;
    box-shadow: 0 0 10px rgba(0,0,0,0.3);
}

.image_div {
    text-align: center;
    font-size: small;
    font-family: sans-serif;
}
img {
    display: block;
}



</style>
<script src="https://code.jquery.com/jquery-1.10.2.min.js" charset="utf-8"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/unveil/1.3.0/jquery.unveil.min.js" charset="utf-8"></script>
<script>
$(document).ready(function() {
    $('img').unveil();

});
</script>
</head>
<body>
    <table>
        <tr>
        {% for image in images %}
            <td>
            <div class="image_div">
                <a class="image" href="{{ image.src }}" style="width: {{ image.width }}px; height: {{ image.height }}px" target="_blank">
                    <img src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" data-src="{{ image.src }}?w={{ image.width }}&amp;h={{ image.height }}" width="{{ image.width }}" height="{{ image.height }}" /></a>
            <span>{{ image.id }}</span>
            </div>
        </td>
        {% if loop.index % 4 == 0: %}
        </tr>
        <tr>
        {% endif %}
        
        {% endfor %}
    </table>        
</body>
'''
@app.route('/images/<path:filename>')
def image(filename):
    filename = "/"+filename
    print("thumbnail called for filname {}".format(filename))
    try:
        w = int(request.args['w'])
        h = int(request.args['h'])
    except (KeyError, ValueError):
        #return Response(filename)
        im = Image.open(filename)
        io = BytesIO()
        im.save(io, format("JPEG"))
        return Response(io.getvalue(), mimetype='image/jpeg')
    # return send_from_directory('.', filename)

    try:
        im = Image.open(filename)
        im.thumbnail((w, h), Image.ANTIALIAS)
        io = BytesIO()
        im.save(io, format='JPEG')
        #return Response(filename)
        return Response(io.getvalue(), mimetype='image/jpeg')

    except IOError:
        abort(404)

        return send_from_directory('.', filename)

@app.route('/')
def index():
    images = []
    for root, dirs, files in os.walk(dataroot):
        for filename in [os.path.join(root, name) for name in files]:
            if not (filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('png')):
                continue
            im = Image.open(filename)
            w, h = im.size
    #        print("{}  {}   {}".format(filename,w,h))
        
            aspect = 1.0*w/h
            if aspect > 1.0:
                width = WIDTH#min(w, WIDTH)
                height = width/aspect
            else:
                height = HEIGHT#min(h, HEIGHT)
                width = height*aspect
            file_path = "/images"+ filename
            images.append({
                'width': int(width),
                'height': int(height),
                'src': file_path,
                'id': os.path.splitext(os.path.basename(filename))[0]
            })
    images = sorted(images, key= lambda x: x["height"])
    return render_template_string(TEMPLATE, **{
        'images': images
    })
def main():
    app.run(debug=True, host="0.0.0.0",port=port)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=port)
