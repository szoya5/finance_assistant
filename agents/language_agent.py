from transformers import pipeline
from langchain.llms import HuggingFacePipeline
from langchain.chains import RetrievalQA
from agents.retriever_agent import create_vectorstore

def generate_brief(question):
    pipe = pipeline("text2text-generation", model="google/flan-t5-small")

    llm = HuggingFacePipeline(pipeline=pipe)

    vectordb = create_vectorstore()
    retriever = vectordb.as_retriever()

    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain.run(question)
