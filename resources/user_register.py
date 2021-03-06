from flask_restful import Resource, reqparse
from models.user_model import UserModel
import sqlite3


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help="Username required!")
    parser.add_argument('password', type=str, required=True, help="Password required!")

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message': "User already exists!"}, 400

        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "INSERT INTO users VALUES (NULL, ?, ?)"
        # cursor.execute(query, (data['username'], data['password']))
        #
        # connection.commit()
        # connection.close()

        user = UserModel(**data)
        user.insert_into_db()

        return {"message": "User created successfully"}, 201
