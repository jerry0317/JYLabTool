import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

def setPlotStyle(pyplot=True):
    if pyplot is False:
        fig = Figure(dpi=300)
    else:
        import matplotlib.pyplot as plt
        fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.tick_params(axis="both",which="both", direction="in")
    return fig, ax

def twoWayPlot(dataset, xName, yName, xErrorBar=True, yErrorBar=True, xError=None, yError=None, show=True, httpimg=False):
    xData = dataset.values[xName]
    yData = dataset.values[yName]
    if xError is None:
        xError = dataset.uncertainties[xName]
    if yError is None:
        yError = dataset.uncertainties[yName]

    if show is True:
        fig, ax = setPlotStyle(pyplot=True)
    else:
        fig, ax = setPlotStyle(pyplot=False)

    ax.errorbar(xData, yData, fmt='ko', xerr=(0 if (xErrorBar is None) else xError), yerr=(0 if (yErrorBar is None) else yError), markersize=4, elinewidth=1)
    ax.set_xlabel(xName)
    ax.set_ylabel(yName)
    if show is True:
        import matplotlib.pyplot as plt
        plt.show()
    if httpimg is True:
        output = io.BytesIO()
        return fig, output
