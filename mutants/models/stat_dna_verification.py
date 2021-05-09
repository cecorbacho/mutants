from mutants import ma
from marshmallow import fields


class StatDnaVerification():
    def __init__(self, count_mutant_dna, count_human_dna):
        self.count_mutant_dna = count_mutant_dna
        self.count_human_dna = count_human_dna
        self.ratio = self.count_mutant_dna if self.count_human_dna==0 else round(self.count_mutant_dna / self.count_human_dna , 2)


class StatDnaVerificationSchema(ma.Schema):
    count_mutant_dna = fields.Integer()
    count_human_dna = fields.Integer()
    ratio = fields.Float()
