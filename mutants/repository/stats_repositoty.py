import json
from flask import make_response, request, jsonify
from flask_restful import Resource, reqparse
from sqlalchemy import func
from mutants import app, db
from mutants.models import human, stat_dna_verification




class DnaVerification(Resource):
    def get(self):
        try:
            count_mutant_dna = db.session.query(func.count(human.Human.dna)).select_from(human.Human).filter_by(mutant=True).scalar()
            count_human_dna = db.session.query(func.count(human.Human.dna)).select_from(human.Human).filter_by(mutant=False).scalar()
            stats = stat_dna_verification.StatDnaVerification(count_mutant_dna, count_human_dna)
            schema = stat_dna_verification.StatDnaVerificationSchema()
            result = schema.dumps(stats).data
            return make_response(result,200)
        except Exception as e:
            return make_response(jsonify("Unexpected Error Try Again Later."),403)

