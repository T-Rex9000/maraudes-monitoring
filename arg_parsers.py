from flask_restful import reqparse

volunteer_put_arg_parser = reqparse.RequestParser()
volunteer_put_arg_parser.add_argument(
    name="forename",
    type=str,
    help="Volunteer's forename",
    required=True
)
volunteer_put_arg_parser.add_argument(
    name="surname",
    type=str,
    help="Volunteer's surname",
    required=True
)

homeless_put_arg_parser = reqparse.RequestParser()
homeless_put_arg_parser.add_argument(
    name="forename",
    type=str,
    help="Forename",
    required=True
)
homeless_put_arg_parser.add_argument(
    name="surname",
    type=str,
    help="Surname",
    required=False
)

participation_put_arg_parser = reqparse.RequestParser()
participation_put_arg_parser.add_argument(
    name="volunteer_id",
    type=int,
    help="Id of the volunteer",
    required=True
)
participation_put_arg_parser.add_argument(
    name="maraude_id",
    type=int,
    help="Id of the maraude",
    required=True
)

encounter_put_arg_parser = reqparse.RequestParser()
encounter_put_arg_parser.add_argument(
    name="homeless_id",
    type=int,
    help="Id of the homeless person",
    required=True
)
encounter_put_arg_parser.add_argument(
    name="maraude_id",
    type=int,
    help="Id of the maraude",
    required=True
)
encounter_put_arg_parser.add_argument(
    name="longitude",
    type=float,
    help="Encounter longitude",
    required=True
)
encounter_put_arg_parser.add_argument(
    name="latitude",
    type=float,
    help="Encounter latitude",
    required=True
)
encounter_put_arg_parser.add_argument(
    name="comment",
    type=str,
    help="Comment about the encounter",
    required=False
)
