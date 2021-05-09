from mutants import api
from mutants.repository import human_dna_check_repository

api.add_resource(human_dna_check_repository.Mutant,"/mutant/")