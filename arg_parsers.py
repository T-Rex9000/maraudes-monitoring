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

maraude_put_arg_parser = reqparse.RequestParser()
maraude_put_arg_parser.add_argument(
    name="volunteer_0",
    type=int,
    help="Volunteer id of the first volunteer",
    required=True
)
maraude_put_arg_parser.add_argument(
    name="volunteer_1",
    type=int,
    help="Volunteer id of the second volunteer",
    required=False
)
maraude_put_arg_parser.add_argument(
    name="volunteer_2",
    type=int,
    help="Volunteer id of the third volunteer",
    required=False
)
maraude_put_arg_parser.add_argument(
    name="volunteer_3",
    type=int,
    help="Volunteer id of the fourth volunteer",
    required=False
)
