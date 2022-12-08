from flask import Blueprint, request, jsonify, make_response
import json
from src import db
from flask import current_app

owner = Blueprint('owner', __name__)


# Posts ad to table
@owner.route('/ownerAd', methods=['POST'])
def post_owner_ad():
    current_app.logger.info(request.form)
    cursor = db.get_db().cursor()
    rest_id = request.form['rest_id']
    header = request.form['header']
    duration = request.form['duration']
    target_audience = request.form['target_audience']
    description = request.form['description']
    query = f'INSERT INTO Advertisements (restId, header, duration, targetAudience, description) VALUES ' \
            f'(\"{rest_id}\", \"{header}\", \"{duration}\", \"{target_audience}\", \"{description}\")'
    cursor.execute(query)
    db.get_db().commit()
    return f'<h1>Added {rest_id} {header} {duration} {target_audience} {description}.</h1>'


# Get all ad durations and prices from the DB
@owner.route('/adDurations', methods=['GET'])
def get_durations():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT duration AS Duration, price AS Price FROM Durations')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# Get all filters from the DB
@owner.route('/targetAudience', methods=['GET'])
def get_targets():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT id AS value, name AS label FROM Filters')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# Gets all the restaurant reviews and responses
@owner.route('/reviews', methods=['GET'])
def get_reviews():
    cursor = db.get_db().cursor()
    cursor.execute(
        'SELECT rest.name AS Restaurant, re.id AS ReviewID, re.title AS title, re.description AS Description, '
        're.stars AS Stars, re.restaurantResp AS RestaurantResponse, re.date AS Date '
        'FROM Reviews re JOIN Restaurant rest ON re.restId = rest.Id')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# Gets all the restaurants
@owner.route('/operatingAs', methods=['GET'])
def get_operating_as():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT id as value, name as label FROM Restaurant')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# Tests that the ad post request is working correctly
@owner.route('/testAdPost', methods=['GET'])
def get_test():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Advertisements')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# Tests that the reviews request is working correctly
@owner.route('/testReviews', methods=['GET'])
def test_reviews():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Reviews')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# Updates restaurant reviews
@owner.route('/ownerResponse', methods=['POST'])
def post_owner_resp():
    current_app.logger.info(request.form)
    cursor = db.get_db().cursor()
    rest_resp = request.form['rest_resp']
    review_id = request.form['review_id']
    query = f'UPDATE Reviews SET restaurantResp = \"{rest_resp}\" WHERE id = \"{review_id}\"'
    cursor.execute(query)
    db.get_db().commit()
    return f'<h1>Added {rest_resp} for {review_id}.</h1>'
