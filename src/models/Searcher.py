import hydra
from omegaconf import DictConfig
from langchain import LLMChain, OpenAI, PromptTemplate


class LLMTeacher:
    """This is the interface of the concrete searchers(implemented in ./components/)"""

    def __init__(self, cfg: DictConfig) -> None:
        self.model = hydra.utils.instantiate(cfg.components)
        template = """
        # 質問
        {question}
        # 該当ページ
        "{information}"
        # 回答
        """
        self.prompt = PromptTemplate(
            template=template, input_variables=["question", "information"]
        )
        self.llm_chain = LLMChain(prompt=self.prompt, llm=OpenAI(), verbose=False)

    def search(self, api_key, query):
        self.model.setup(api_key)
        result = self.model.search(query)
        return result

    def answer(self, api_key, query):
        information = self.search(api_key, query)
        answer = self.llm_chain.predict(question=query, information=information)
        return answer
