from flask import Flask,Blueprint
from app.controllers.series_controller import series,create,get_series_by_id


bp=Blueprint("series", __name__,url_prefix="/series")


bp.get("")(series)
bp.get("/<series_id>")(get_series_by_id)
bp.post("")(create)