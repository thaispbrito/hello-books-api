from flask import Blueprint, abort, make_response, request, Response
from app.models.book import Book
from .route_utilities import validate_model, create_model, get_models_with_filters
from ..db import db

bp = Blueprint("books_bp", __name__, url_prefix="/books")

# CREATE A BOOK RECORD
@bp.post("")
def create_book():
    request_body = request.get_json()
    return create_model(Book, request_body)

# READ ALL BOOK RECORDS
@bp.get("")
def get_all_books():
    return get_models_with_filters(Book, request.args)

# READ A BOOK RECORD
@bp.get("/<book_id>")
def get_one_book(book_id):

    book = validate_model(Book, book_id)

    return book.to_dict()

# UPDATE A BOOK RECORD
@bp.put("/<book_id>")
def update_book(book_id):

    book = validate_model(Book, book_id)
    request_body = request.get_json()

    book.title = request_body["title"]
    book.description = request_body["description"]
    db.session.commit()

    return Response(status=204, mimetype="application/json")

# DELETE A BOOK RECORD
@bp.delete("/<book_id>")
def delete_book(book_id):

    book = validate_model(Book, book_id)
    db.session.delete(book)
    db.session.commit()

    return Response(status=204, mimetype="application/json")


