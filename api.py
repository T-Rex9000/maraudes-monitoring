from flask import Flask, request
from flask_restful import Resource, Api, reqparse, abort

from gpx_utils import parse_gpx, get_points_from_gpx
from os.path import join, isfile

app = Flask(__name__)
api = Api(app)

maraude_path_get_arg_parser = reqparse.RequestParser()
maraude_path_get_arg_parser.add_argument(
    name="data_path",
    type=str,
    help="Path to the example data",
    required=True
)


def abort_check(data_path, maraude_id):
    if not isfile(join(data_path, f"{maraude_id}.gpx")):
        abort("This maraude_id does not exist")


class MaraudePath(Resource):
    def get(self, maraude_id):
        args = maraude_path_get_arg_parser.parse_args()
        abort_check(data_path=args["data_path"], maraude_id=maraude_id)
        points = get_points_from_gpx(parse_gpx(join(args["data_path"], f"{maraude_id}.gpx")))

        return points, 200

    def put(self):
        pass

    def delete(self):
        pass


api.add_resource(MaraudePath, '/maraude_path/<string:maraude_id>')

if __name__ == '__main__':
    app.run(debug=True)
