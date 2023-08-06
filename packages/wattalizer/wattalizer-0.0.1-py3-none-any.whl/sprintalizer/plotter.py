import plotly.offline as po
import plotly.graph_objects as go
import numpy as np
import datetime as dt

NTHCOLOR  = "orangered"
MAXCOLOR  = NTHCOLOR
THISCOLOR = "limegreen"
CURCOLOR  = "magenta"

class SprintMeasure:
    def __init__(self, timestamp, power, duration):
        self.timestamp = timestamp
        self.duration = duration
        allSamples = moving_average(power, duration)
        self.watts = np.max(allSamples)
        idx = np.where(allSamples == self.watts)[0][0]
        # allSamples is 'duration' shorter than power because we can't
        # get a moving average until we have a full window so we must
        # subtract 'duration' from the index
        self.start = idx # - duration + duration
        self.power = np.array(power)[self.start:self.start + duration]

def moving_average(a, n) :
    ret = np.cumsum(a, dtype = float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

def get_maindata(sprints, current, season, samples = None):
    cdt = dt.datetime.combine(current['date'], current['time'])
    data = []
    for (k, v) in sprints.items():
        if k.date() < season['start'][0]:
            continue
        if k.date() >= season['end'][0]:
            continue
        if k == cdt:
            continue
        data.append(v)

    if not data:
        return None

    alltime = [sorted(c, key = lambda x: x.watts) if c else [0] * len(samples)
               for c in [[pw[d - 1] for pw in data] for d in samples]]
    thistime = [list(filter(lambda x: x.timestamp < cdt, c)) for c in alltime]

    n = min(10, len(alltime[0]))

    maxDates =  [str(p[-1].timestamp.date()) for p in alltime]
    nthDates =  [str(p[-n].timestamp.date()) for p in alltime]
    thisDates = [str(p[-1].timestamp.date()) for p in thistime]
    maxW = [p[-1].watts for p in alltime]
    nthW = [p[-n].watts for p in alltime]
    thisW = [p[-1].watts for p in thistime]
    currW = [c.watts for c in sprints[cdt]]
    return {'seconds': samples,
            'maxW': maxW, 'maxDates': maxDates,
            'nthW': nthW, 'nthDates': nthDates,
            'thisW': thisW, 'thisDates': thisDates,
            'currentW': currW, 'current': current,
            'all': alltime, 'this': thistime}

def get_subdata(data, second, season):
    maxW = data['all'][second][-1]
    maxName = "%dW Max %s (%s)" % (
        maxW.watts, season['name'][0], maxW.timestamp.date())
    thisW = data['this'][second][-1]
    thisName = "%dW Local Max (%s)" % (thisW.watts, thisW.timestamp.date())
    curW = data['current'][second]
    curName = "%dW Current effort (%s)" % (curW.watts, curW.timestamp.date())
    subdata = {
        'seconds': list(range(1, second + 1)),
        'maxW': maxW.power,
        'maxName': maxName,
        'thisW': thisW.power,
        'thisName': thisName,
        'currentW': curW.power,
        'currentName': curName,
    }
    return subdata


def main_fig(data, current, season):
    title = current['Workout_Code']
    layout = go.Layout(title = go.layout.Title(text = title))
    fig = go.Figure(layout = layout)

    scNth = go.Scatter(x = data['seconds'], y = data['nthW'],
                       mode = 'lines', name = '', hoverinfo = "y+text",
                       line = {'width': 0, 'color': NTHCOLOR},
                       text = data['nthDates'])
    scMax = go.Scatter(x = data['seconds'], y = data['maxW'],
                       mode = 'lines', name = "%s Max" % season['name'][0],
                       hoverinfo = "y+text", fill = "tonexty",
                       line = {'width': 0, 'color': MAXCOLOR},
                       text = data['maxDates'])
    scThis = go.Scatter(x = data['seconds'], y = data['thisW'],
                        mode = 'lines', name = "Local Max",
                        hoverinfo = "y+text", line = {'color': THISCOLOR},
                        text = data['thisDates'])
    scCur = go.Scatter(x = data['seconds'], y = data['currentW'],
                       mode = 'lines', hoverinfo = "y",
                       line = {'color': CURCOLOR}, name = str(current['date']))

    fig.add_trace(scNth)
    fig.add_trace(scMax)
    fig.add_trace(scThis)
    fig.add_trace(scCur)

    return fig

def sub_fig(data):
    title = "%d seconds effort" % data['seconds'][-1]
    sfig = None
    if sfig is None:
        layout = go.Layout(title = go.layout.Title(text = title))
        sfig = go.Figure(layout = layout)

        scMax = go.Scatter(x = data['seconds'], y = data['maxW'],
                           mode = 'lines', name = data['maxName'],
                           line = {'color': MAXCOLOR})
        scThis = go.Scatter(x = data['seconds'], y = data['thisW'],
                            mode = 'lines', name = data['thisName'],
                           line = {'color': THISCOLOR})
        scCur = go.Scatter(x = data['seconds'], y = data['currentW'],
                           mode = 'lines', name = data['currentName'],
                           line = {'color': CURCOLOR})
        sfig.add_trace(scMax)
        sfig.add_trace(scThis)
        sfig.add_trace(scCur)
    else:
        sfig.update_traces(x = data['seconds'], y = data['maxW'],
                           name = data['maxName'],
                           selector = dict(line = {'color': MAXCOLOR}))
        sfig.update_traces(x = data['seconds'], y = data['thisW'],
                           name = data['thisName'],
                           selector = dict(line = {'color': THISCOLOR}))
        sfig.update_traces(x = data['seconds'], y = data['currentW'],
                           name = data['currentName'],
                           selector = dict(line = {'color': CURCOLOR}))


    return sfig

