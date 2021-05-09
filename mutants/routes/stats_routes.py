from mutants import api
from mutants.repository import stats_repositoty

api.add_resource(stats_repositoty.DnaVerification,"/stats/")