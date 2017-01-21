""" If use flask, imports this
from flask import (
    Flask,
    request,
)

import config

from db import (
    admin,
    db,
    migrate,
)
"""
import json
#from google import add_routes as add_google_routes
from google import search
#from naver import add_routes as add_naver_routes
from naver import (
    searchNotebook,
    searchSmartphone,
)

""" Also add this.
>>> app = Flask(__name__)

>>> app.config.from_object(config)

>>> admin.init_app(app)
>>> db.init_app(app)
>>> migrate.init_app(app, db)

>>> add_google_routes(app)
>>> add_naver_routes(app)
"""

#@app.route("/api/getDB/", methods=["GET", "POST"])
def makeDB():
    iteminfos = []
    #if request.method == "GET":
    iteminfos.append(searchSmartphone())
    iteminfos.append(searchNotebook())
    for i in range(len(iteminfos[0])):
        iteminfos[0][i]['reviews'] = search(iteminfos[0][i]['name'])
    for i in range(len(iteminfos[1])):
        iteminfos[1][i]['reviews'] = search(iteminfos[1][i]['name'])
    #index()
    #else:
    return json.dumps(iteminfos)

#if __name__ == "__main__":
#    app.run(debug=True, host="0.0.0.0", port=8000)
#
makeDB()
