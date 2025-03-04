from UI.UI import *

def run_app():
    melodi_repo = melodiRepo()
    melodi_repo.read_from_file()
    melodi_validator = melodiVali()
    melodi_service = melodiService(melodi_repo, melodi_validator)

    cosole = Console(melodi_service)
    cosole.run_app()


run_app()