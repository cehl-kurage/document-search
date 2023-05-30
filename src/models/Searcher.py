import hydra
from omegaconf import DictConfig


class Searcher:
    """This is the interface of the concrete searchers(implemented in ./components/)"""

    def __init__(self, cfg: DictConfig) -> None:
        self.model = hydra.utils.instantiate(cfg.components)

    def search(self, api_key, query):
        self.model.setup(api_key)
        result = self.model.search(query)
        return result
