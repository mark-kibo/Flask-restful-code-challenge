#!/usr/bin/env python3

from flask import Flask, jsonify, make_response
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db, Hero, HeroPower, Power

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = True

migrate = Migrate(app, db)

db.init_app(app)

CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

api = Api(app)

@app.route('/')
def home():
    return ''


class Heroes(Resource):
    def get(self):
        heroes=Hero.query.all()
        heros_to_pass=[]
        for hero in heroes:
            hero_dict={
                "id": hero.id,
                "name":hero.name,
                "super_name": hero.super_name 
            }
            heros_to_pass.append(hero_dict)
        return make_response(jsonify(heros_to_pass), 200)
    
api.add_resource(Heroes, "/heroes")

if __name__ == '__main__':
    app.run(port=5555, debug=True)
