import gpxpy

def parse_gpx(
        path
):
    '''
    Parse a .GPX file
    :param path: path of the .GPX file
    :return: parsed file
    '''
    with open(path, "r") as gpx_file:
        gpx = gpxpy.parse(gpx_file)

    return gpx


def get_points_from_gpx(
        gpx
):
    '''
    Fetch a list of point coordinates and time from a parsed .GPX file
    :param gpx: a parsed .GPX file
    :return: a dict of points
    '''
    points = {}

    for t, track in enumerate(gpx.tracks):
        for s, segment in enumerate(track.segments):
            for p, point in enumerate(segment.points):
                points[f"{t}_{s}_{p}"] = {
                    "longitude": point.longitude,
                    "latitude": point.latitude,
                    "elevation": point.elevation,
                    "time": point.time.strftime("%Y_%m_%d,%H:%M:%S"),
                }

    return points


if __name__ == "__main__":
    print(get_points_from_gpx(parse_gpx("example_data/2020_11_23.gpx")))
