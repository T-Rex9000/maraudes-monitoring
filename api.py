from flask import Flask
from flask_restful import Resource, Api, fields, marshal_with, abort
from flask_sqlalchemy import SQLAlchemy

# from gpx_utils import parse_gpx, get_points_from_gpx
from os.path import join, dirname, abspath
from create_db import MaraudeModel, VolunteerModel
from arg_parsers import volunteer_put_arg_parser, maraude_put_arg_parser

# Create API and load DB
app = Flask(__name__)
api = Api(app)

BASE_DIR = dirname(abspath(__file__))
db_path = join(BASE_DIR, "database.db")

app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
db = SQLAlchemy(app)

# Define how to serialize resources' outputs
volunteer_resource_fields = {
    "id": fields.Integer,
    "surname": fields.String,
    "forename": fields.String
}

maraude_resource_fields = {
    "id": fields.Integer,
    "volunteer_0": fields.Integer,
    "volunteer_1": fields.Integer,
    "volunteer_2": fields.Integer,
    "volunteer_3": fields.Integer,
}


# Define Resources
class VolunteerResource(Resource):
    '''
    The marshal_with decorator is here to describe how to serialize the volunteer object
    '''

    @marshal_with(volunteer_resource_fields)
    def get(self, volunteer_id):
        volunteer = VolunteerModel.query.filter_by(id=volunteer_id).first()
        if not volunteer:
            abort(404, message="Can not find the requested volunteer id")
        return volunteer, 200

    @marshal_with(volunteer_resource_fields)
    def put(self, volunteer_id):
        volunteer = VolunteerModel.query.filter_by(id=volunteer_id).first()
        if volunteer:
            abort(409, message="Volunteer id already exists")

        args = volunteer_put_arg_parser.parse_args()

        volunteer = VolunteerModel(
            id=volunteer_id,
            forename=args["forename"],
            surname=args["surname"],
        )
        db.session.add(volunteer)
        db.session.commit()
        return volunteer, 201

    def delete(self):
        pass


class MaraudeResource(Resource):
    @marshal_with(maraude_resource_fields)
    def get(self, maraude_id):
        maraude = MaraudeModel.query.filter_by(id=maraude_id).first()
        if not maraude:
            abort(404, message="Can not find the requested maraude id")
        return maraude, 200

    @marshal_with(maraude_resource_fields)
    def put(self, maraude_id):
        maraude = MaraudeModel.query.filter_by(id=maraude_id).first()
        if maraude:
            abort(409, message="Maraude id already exists")

        args = maraude_put_arg_parser.parse_args()

        maraude = MaraudeModel(
            id=maraude_id,
            volunteer_0=args["volunteer_0"],
            volunteer_1=args["volunteer_1"],
            volunteer_2=args["volunteer_2"],
            volunteer_3=args["volunteer_3"]
        )
        db.session.add(maraude)
        db.session.commit()
        return maraude, 201

    def delete(self):
        pass


# Add ressources to the API
api.add_resource(VolunteerResource, '/volunteer/<string:volunteer_id>')
api.add_resource(MaraudeResource, '/maraude/<string:maraude_id>')

if __name__ == '__main__':
    app.run(debug=True)
