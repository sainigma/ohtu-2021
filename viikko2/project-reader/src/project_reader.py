from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        
        result = toml.loads(content)
        poetryInfo = result['tool']['poetry']
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(poetryInfo['name'], poetryInfo['description'], poetryInfo['dependencies'], poetryInfo['dev-dependencies'])
