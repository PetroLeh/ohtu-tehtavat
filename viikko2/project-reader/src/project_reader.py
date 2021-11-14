from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        parsed = toml.loads(content)
        print(parsed["tool"]["poetry"])
        poetry = parsed["tool"]["poetry"]
        name = poetry["name"]
        description = poetry["description"]
        dependencies = poetry["dependencies"].keys()
        dev_dependencies = poetry["dev-dependencies"].keys()
        return Project(name, description, dependencies, dev_dependencies)
