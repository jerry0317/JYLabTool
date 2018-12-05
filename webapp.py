import JYL
from flask import Flask, url_for, render_template, request, Response, json
import os
import JYL.methods.filem as jflm
import JYL.plot as jplt

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from io import StringIO

import numpy as np

app = Flask(__name__)
app.template_folder = "html-templates"

dataset = JYL.JYLDataSet()

@app.route("/")
def render_index():
    return render_template('index.html')

@app.route("/api/<para>", methods=['POST'])
def api_post(para):
    global dataset
    if para == "democsv":
        returndic = {}
        try:
            dataset = jflm.openFromCSV(file=StringIO(request.files['democsv-file'].stream.read().decode("UTF8"), newline=None))
        except Exception as e:
            returndic["status"] = 400
            returndic["msg"] = "Failed to read the csv file. Error message: {}".format(e)
        else:
            returndic["status"] = 200
            returndic["imgurl"] = "/img/twoWP.png"
        return json.dumps(returndic)
    else:
        return "BAD"

@app.route("/img/twoWP.png")
def render_twoWP_png():
    global dataset
    names = list(dataset.dataNames)
    fig, output = jplt.twoWayPlot(dataset, names[0], names[1], httpimg=True, show=False)

    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

if __name__ == "__main__":
    app.run(port=5000)
