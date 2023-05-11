from langchain import LLMChain, OpenAI, PromptTemplate

API_KEY = "YOUR API KEY"
template = """質問：{question}
回答：段階的に考えましょう。
"""
prompt = PromptTemplate(template=template, input_variables=["question"])
llm_chain = LLMChain(
    prompt=prompt, llm=OpenAI(temperature=0, openai_api_key=API_KEY), verbose=True
)

question = "関ヶ原の戦いはいつ起きた？"

answer = llm_chain.predict(question=question)
print(answer)
