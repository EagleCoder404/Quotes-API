from app import app
from flask import jsonify,request,abort,make_response
from app.models import Quote

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'not found'}),404)

@app.route("/")
def index():
    return "Hey"

# @app.route('/api/register',methods=['POST'])
# def register():
#     if request.method == "POST":
#         pass

@app.route('/api/quotes/<int:page_number>')
def get_all(page_number):
    q = Quote.query.paginate(page_number,5).items
    data = jsonify([{'author':x.author,'text':x.text} for x in q])
    return data

@app.route("/api/quote/<int:id>")
def get_id(id):
        q = Quote.query.get(int(id))
        if q is None:
            abort(404)
        return jsonify({'author':q.author,'text':q.text})

@app.route("/api/author/<string:author_name>/<int:page_number>")
def get_by_author(author_name,page_number):
    q = Quote.query.filter_by(author=author_name).paginate(page_number,5).items
    if q == [] or q is None:
        abort(404)
        
    data = jsonify([{'author':x.author,'text':x.text} for x in q])
    return data

@app.route("/api/authors/")
def authors():
    q = Quote.query.with_entities(Quote.author).all()
    return jsonify({'authors':[x[0] for x in q]})