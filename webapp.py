import JYL
from flask import Flask, url_for, render_template, request, Response, json, send_file
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
    returndic = {}
    if para == "democsv":
        try:
            dataset = jflm.openFromCSV(file=StringIO(request.files['democsv-file'].stream.read().decode("UTF8"), newline=None))
        except Exception as e:
            returndic["status"] = 400
            returndic["msg"] = "Failed to read the csv file. Error message: {}".format(e)
        else:
            returndic["status"] = 200
            returndic["dataNames"] = list(dataset.dataNames)
    elif para == "democsv-twplot":
        try:
            xName = request.form['xName']
            yName = request.form['yName']
        except Exception as e:
            returndic["status"] = 400
            returndic["msg"] = "Failed to process. Error message: {}".format(e)
        else:
            returndic["status"] = 200
            returndic["imgurl"] = "/img/twoWP-{0}vs{1}.png".format(xName, yName)
    elif para == "democsv-alldata":
        returndic["dataNames"] = list(dataset.dataNames)
        returndic["length"] = dataset.length
        returndic["allData"] = dataset.acsList
        returndic["status"] = 200
    else:
        returndic["msg"] = "BAD"

    return json.dumps(returndic)

@app.route("/img/twoWP-<x>vs<y>.png")
def render_twoWP_png(x,y):
    global dataset
    try:
        fig, output = jplt.twoWayPlot(dataset, x, y, httpimg=True, show=False)
        FigureCanvas(fig).print_png(output)
        return Response(output.getvalue(), mimetype='image/png')
    except Exception as e:
        return send_file("img_error.png", mimetype='image/png')

@app.route("/file/example.csv")
def example_csv():
    return send_file("sT.csv", mimetype='text/csv')

if __name__ == "__main__":
    app.run(port=5000)
