from flask import Blueprint, render_template, request, jsonify
from flask.helpers import flash
from flask_login import login_required, current_user
from .models import Note, Listing
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note is added', category='success')
    return render_template("home.html", user=current_user)

# created view definition of new listing to add
@views.route('/listings', methods=['GET', 'POST'])
def listings():
    if request.method == 'POST':
        listing = request.form.get('listings')
        print(listing)
        new_listing = Listing(data=listing, user_id=current_user)
        db.session.add(new_listing)
    # if request.method == 'POST':
        # listing = request.form.get('listing')
        # if len(listing) < 1:
        #     flash('Listing is too short!', category='error')
        # else:
            # new_listing = Listing(data=listing, user_id=current_user.id)
    flash('Listing is too short!', category='error')
    flash('Listing is added', category='success')
    return render_template("listings.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            return jsonify({'noteId': note})