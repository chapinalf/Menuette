from flask import Blueprint, request, jsonify, make_response
import json
from src import db
from flask import current_app

blogger = Blueprint('blogger', __name__)


# Gets restaurant name, ad header, target audience, and ad description
@blogger.route('/ads', methods=['GET'])
def get_Ads():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT r.name AS RestaurantName, a.header AS Header, f.name AS TargetAudience, '
                   'a.description AS Description FROM Advertisements a JOIN Restaurant r '
                   'ON a.restId = r.id JOIN Filters f ON a.targetAudience = f.id')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# Gets all users that are bloggers
@blogger.route('/operatingAs', methods=['GET'])
def get_operating_as():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT id as value, username as label FROM User WHERE type = "Blogger"')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response
