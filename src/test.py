import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"), organization="org-GPDJJQ8LUt6Px5RrkzmU6onv")

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
)

print(completion.choices[0].message)


# text_splitter = RecursiveCharacterTextSplitter(
#     chunk_size=1000, chunk_overlap=200, add_start_index=True
# )
# all_splits = text_splitter.split_documents(docs)
#
# vectorstore = Chroma.from_documents(documents=all_splits,
#                                     embedding=OpenAIEmbeddings(openai_api_key=setUp.OPENAI_API_KEY))
#
# retriever = vectorstore.as_retriever()
# prompt = hub.pull('rlm/rag-prompt')
#
#
# def format_docs(docs):
#     return "\n\n".join(doc.page_content for doc in docs)
#
#
# rag_chain = (
#         {"context": retriever | format_docs, "question": RunnablePassthrough()}
#         | prompt
#         | setUp.llm
#         | StrOutputParser()
# )
#
# # for chunk in rag_chain.stream("What is Task Decomposition?"):
# #     print(chunk, end="", flush=True)
#
# rag_chain.invoke("What is Task Decomposition?")
