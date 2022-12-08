from flask import Blueprint, request, jsonify, make_response
import json
from src import db
from flask import current_app

searcher = Blueprint('searcher', __name__)


# Gets all social groups
@searcher.route('/groups', methods=['GET'])
def get_groups():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT id AS value, name AS label FROM Social_Groups')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# Gets all the users that are searchers
@searcher.route('/operatingAs', methods=['GET'])
def get_operating_as():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT id as value, username as label FROM User WHERE type = "Searcher"')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# Adds names into social groups
@searcher.route('/addGroup', methods=['POST'])
def post_add_group():
    current_app.logger.info(request.form)
    cursor = db.get_db().cursor()
    name = request.form['name']
    query = f'INSERT INTO Social_Groups (name) VALUES (\"{name}\")'
    cursor.execute(query)
    db.get_db().commit()
    return f'<h1>Added {name}.</h1>'


# Adds user and group id into user groups
@searcher.route('/joinGroup', methods=['POST'])
def post_join_group():
    current_app.logger.info(request.form)
    cursor = db.get_db().cursor()
    user_id = request.form['user_id']
    group_id = request.form['group_id']
    query = f'INSERT INTO User_Groups (userId, groupId) VALUES (\"{user_id}\", \"{group_id}\")'
    cursor.execute(query)
    db.get_db().commit()
    return f'<h1>Added {group_id} and {user_id}.</h1>'


# Tests that the join user group request is working correctly
@searcher.route('/testJoinGroup', methods=['GET'])
def get_test_join():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM User_Groups')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# Tests that the add user group request is working correctly
@searcher.route('/testAddGroup', methods=['GET'])
def get_test_add():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Social_Groups')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response
