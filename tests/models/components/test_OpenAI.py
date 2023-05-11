import os

from dotenv import load_dotenv

from src.models.components.OpenAI import OpenAISearcher

load_dotenv()
api_key = os.environ.get("API_KEY")


def test_OpenAI_searcher():
    # test of setup
    mod = OpenAISearcher()
    mod.setup(api_key=api_key)

    # test of search
    res = mod.search(query="a")
    assert res is not None
    assert res != ""
