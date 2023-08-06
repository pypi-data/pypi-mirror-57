from .webserver import start
from .plotter import get_maindata

srv = None

def find_sprints(GC, sprints, samples = None):
    if samples is None:
        samples = list(range(1, 91))
    for a in GC.activities():
        if a not in sprints:
            pwr = GC.series(GC.SERIES_WATTS, activity = a)
            if not pwr:
                continue
            sprints[a] = [SprintMeasure(a, pwr, d) for d in samples]

def refresh_goldencheetah(GC):
    global srv
    if srv is None:
        srv = start()
        srv.sprints = {}

    find_sprints(GC, srv.sprints)

    # Only the main python-thread can use the GC object so we refresh
    # the data here
    srv.season = GC.season()
    srv.current = GC.activityMetrics()
    srv.data = get_maindata(srv.sprints, srv.current)
    GC.webpage("http://%s:%d/powergraph" % (srv.server_host, srv.server_port))
