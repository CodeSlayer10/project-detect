from flask import Flask
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from pyzoom import ZoomClient
from datetime import datetime as dt
import dateutil.parser as parser

db_connect = create_engine("sqlite:///Project_Alert.db")
app = Flask(__name__)
api = Api(app)




class UpdateBool(Resource):
    @staticmethod
    def get(id, Data):
        conn = db_connect.connect()
        conn.execute("UPDATE isHuman SET {} where id={}".format(Data, id))
        query = conn.execute("select * from isHuman ")
        return {id: [i for i in query.cursor.fetchall()]}




class ShowId(Resource):
    @staticmethod
    def get():
        conn = db_connect.connect()  # connect to database
        query = conn.execute("select * from isHuman ")  # This line performs query and returns json result
        return {'id': [i[1] for i in query.cursor.fetchall()]}


class ShowBool(Resource):
    @staticmethod
    def get():
        conn = db_connect.connect()  # connect to database
        query = conn.execute("select * from isHuman ")  # This line performs query and returns json result
        return {'bool': [i[0] for i in query.cursor.fetchall()]}

@app.route('/Create/<string:api>/<string:apiC>/<string:name>/<int:duration>/<string:password>/<string:dateTime>', methods=['POST']) # Route_4
class Create(Resource):
    @staticmethod
    def get(api, apiC, name, duration, password, dateTime):
        date = parser.parse(dateTime).isoformat()
        client = ZoomClient(api, apiC)
        meeting = client.meetings.create_meeting(type_=2, topic=name, start_time=date, duration_min=duration, password=password)
        return {meeting.id: meeting.id}


api.add_resource(UpdateBool, '/ID/<string:id>/<string:Data>')  # Route_1
api.add_resource(ShowId, '/SID')  # Route_2
api.add_resource(ShowBool, '/SB')  # Route_3


if __name__ == '__main__':
     app.run()
