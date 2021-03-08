from flask import Flask
from flask_restful import Resource, Api, fields, marshal_with, abort
from flask_sqlalchemy import SQLAlchemy

from gpx_utils import get_date
from os.path import join, dirname, abspath
from create_db import MaraudeModel, VolunteerModel, ParticipationModel, HomelessModel, EncounterModel
from arg_parsers import volunteer_put_arg_parser, participation_put_arg_parser, homeless_put_arg_parser, \
    encounter_put_arg_parser

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

homeless_resource_fields = {
    "id": fields.Integer,
    "surname": fields.String,
    "forename": fields.String
}

maraude_resource_fields = {
    "id": fields.Integer,
    "year": fields.Integer,
    "month": fields.Integer,
    "day": fields.Integer,
}

participation_resource_fields = {
    "id": fields.Integer,
    "volunteer_id": fields.Integer,
    "maraude_id": fields.Integer,
}

encounter_resource_fields = {
    "id": fields.Integer,
    "homeless_id": fields.Integer,
    "maraude_id": fields.Integer,
    "longitude": fields.Float,
    "latitude": fields.Float,
    "hour": fields.Integer,
    "minute": fields.Integer,
    "comment": fields.String,
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


class HomelessResource(Resource):
    @marshal_with(homeless_resource_fields)
    def get(self, homeless_id):
        homeless = HomelessModel.query.filter_by(id=homeless_id).first()
        if not homeless:
            abort(404, message="Can not find the requested homeless id")
        return homeless, 200

    @marshal_with(homeless_resource_fields)
    def put(self, homeless_id):
        homeless = HomelessModel.query.filter_by(id=homeless_id).first()
        if homeless:
            abort(409, message="Homeless id already exists")

        args = homeless_put_arg_parser.parse_args()

        homeless = HomelessModel(
            id=homeless_id,
            forename=args["forename"],
            surname=args["surname"],
        )
        db.session.add(homeless)
        db.session.commit()
        return homeless, 201

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

        date = get_date()

        maraude = MaraudeModel(
            id=maraude_id,
            year=int(date.year),
            month=int(date.month),
            day=int(date.day)
        )
        db.session.add(maraude)
        db.session.commit()
        return maraude, 201

    def delete(self):
        pass


class ParticipationResource(Resource):
    @marshal_with(participation_resource_fields)
    def get(self, participation_id):
        participation = ParticipationModel.query.filter_by(id=participation_id).first()
        if not participation:
            abort(404, message="Can not find the requested participation id")
        return participation, 200

    @marshal_with(participation_resource_fields)
    def put(self, participation_id):
        participation = ParticipationModel.query.filter_by(id=participation_id).first()
        if participation:
            abort(409, message="Participation id already exists")

        args = participation_put_arg_parser.parse_args()

        participation = ParticipationModel(
            id=participation_id,
            volunteer_id=args["volunteer_id"],
            maraude_id=args["maraude_id"]
        )
        db.session.add(participation)
        db.session.commit()
        return participation, 201

    def delete(self):
        pass


class EncounterResource(Resource):
    @marshal_with(encounter_resource_fields)
    def get(self, encounter_id):
        encounter = EncounterModel.query.filter_by(id=encounter_id).first()
        if not encounter:
            abort(404, message="Can not find the requested encounter id")
        return encounter, 200

    @marshal_with(encounter_resource_fields)
    def put(self, encounter_id):
        encounter = EncounterModel.query.filter_by(id=encounter_id).first()
        if encounter:
            abort(409, message="Encounter id already exists")

        date = get_date()

        args = encounter_put_arg_parser.parse_args()

        encounter = EncounterModel(
            id=encounter_id,
            homeless_id=args["homeless_id"],
            maraude_id=args["maraude_id"],
            latitude=args["latitude"],
            longitude=args["longitude"],
            comment=args["comment"],
            hour=int(date.hour),
            minute=int(date.minute)
        )
        db.session.add(encounter)
        db.session.commit()
        return encounter, 201

    def delete(self):
        pass


# Add ressources to the API
api.add_resource(VolunteerResource, '/volunteer/<string:volunteer_id>')
api.add_resource(MaraudeResource, '/maraude/<string:maraude_id>')
api.add_resource(ParticipationResource, '/participation/<string:participation_id>')
api.add_resource(HomelessResource, '/homeless/<string:homeless_id>')
api.add_resource(EncounterResource, '/encounter/<string:encounter_id>')

if __name__ == '__main__':
    app.run(debug=True)
