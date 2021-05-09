import json
from flask import make_response, request, jsonify
from flask_restful import Resource, reqparse
from mutants import app, db
from mutants.models import human




class Mutant(Resource):
    def post(self):
        try:
            req_json = request.get_json() #  '{"dna":["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"] }'
            dna = json.dumps(req_json)
            suspicious_human = human.Human(dna=dna)
            human_check = suspicious_human.is_mutant()
            db.session.add(suspicious_human)
            db.session.commit()
            db.session.flush()
            schema = human.HumanSchema()
            result = schema.dumps(suspicious_human).data
            if human_check:
                return make_response(result,200)
            else:
                return make_response(result,403)
        except Exception as e:
            return make_response(jsonify("Unexpected Error Try Again Later."),403)

