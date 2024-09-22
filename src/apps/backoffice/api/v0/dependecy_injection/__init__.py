import os

from ditainer.container import Container
from ditainer.loader.yaml_loader import YAMLLoader


container = Container()
loader = YAMLLoader(container)

loader.load(os.path.join(os.path.dirname(__file__), "imports.yaml"))
