from flask import (
    Flask,
)

import config

from db import (
    admin,
    db,
    migrate,
)

app = Flask(__name__)

app.config.from_object(config)

admin.init_app(app)
db.init_app(app)
migrate.init_app(app, db)

@app.route("/")
def index():
    return "Test"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="8000")
#

# Get
#@app.route("/api/search/", methods=["GET"])
#def search(query):
    #if request.method == "GET":
        #service = build("customsearch", "v1", developerKey = API_KEY)
        #res = service.cse().list(q=query, cx=cse_id, 10).execute()
    # TODO : Finished Well, call result(query result)

# Post
#@app.route("/api/result/<results>", methods=["POST"])
#def result(results):
    #links = []
    #for result in results:
    #    links.append(result['link'])
    #return jsonify(links)

