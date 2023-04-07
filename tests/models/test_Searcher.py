import os

import hydra
from dotenv import load_dotenv
from omegaconf import DictConfig

from src.models.Searcher import Searcher

cfg_dict = {
    "components": {
        "_target_": "src.models.components.OpenAI.OpenAISearcher",
        "chunk_size": 10000,
        "chunk_overlap": 0,
        "emb_model": "text-embedding-ada-002",
        "dir": "data/",
    }
}
cfg = DictConfig(cfg_dict)
load_dotenv()
api_key = os.environ.get("API_KEY")


def test_searcher():
    model = Searcher(cfg)
    assert model is not None

    res = model.search(api_key, "query")
    assert type(res) == str
