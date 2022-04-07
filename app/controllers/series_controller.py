import json
from flask import jsonify, request
from app.models.series_model import Series


def series():

    all_series=Series.series()

    series_columns = ['id','serie','seasons','released_date','genre','imdb_rating']

    serialized_series = [dict(zip(series_columns, serie)) for serie in all_series]

    return jsonify(serialized_series)

def get_series_by_id(series_id):

    series_by_id=Series.select_by_id(series_id)

    series_columns = ['id','serie','seasons','released_date','genre','imdb_rating']
    serialized_series = [dict(zip(series_columns,serie))for serie in series_by_id]


    return jsonify(serialized_series)


def create():

    data=request.get_json()

    series = Series(**data)

    insert_one = series.create_series()

    series_columns = ['id','serie','seasons','released_date','genre','imdb_rating']
    serialized_series = [dict(zip(series_columns, insert_one))]


    return jsonify(serialized_series),201