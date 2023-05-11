import hydra
from omegaconf import DictConfig


class Searcher:
    def __init__(self, cfg: DictConfig):
        self.model = hydra.utils.instantiate(cfg.components)

    def search(self, api_key, query):
        self.model.setup(api_key)
        result = self.model.search(query)
        return result
