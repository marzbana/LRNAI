import os
from dotenv import load_dotenv
load_dotenv()
os.environ['openai_api_key'] = os.getenv('API_Key')
from langchain.chat_models import ChatOpenAI
from llama_index import VectorStoreIndex, ServiceContext, SimpleDirectoryReader, load_index_from_storage, StorageContext, LLMPredictor
class Vector:
    def __init__(self):
        self.index = none
        self.query_engine = none
        self.documents = none
        self.query = none
        self.response = ""
        self.storage_context = none
        self.indexed = false
        self.llm_predictor = LLMPredictor(llm=ChatOpenAi(temperature=0, model_name="gpt-3.5-turbo-16k"))
        self.servicecontext = ServiceContext.from_defaults(llm_predictor=self.llm_predictor)
    def onetime(self):
        self.setdocs('data')
        self.setindex()
    def init(self):
        self.loadindex()
        self.setqueryengine()
        self.indexed = true
    def isset(self):
        return self.indexed
    def loadindex(self):
        self.storage_context = StorageContext.from_defaults(persist_dir="./files/index")
        self.index = load_index_from_storage(self.storage_context)
    def setdocs(self, location):
        self.documents = SimpleDirectoryReader(location).load_data()
    def setindex(self):
        self.index = VectorStoreIndex.from_documents(self.documents)
        self.index.storage_context.persist(persist_dir="./files/index")
    def setqueryengine(self):
        self.query_engine = self.index.as_query_engine(service_context=self.servicecontext)
    def setquery(self, query):
        self.query = query
    def setresponse(self):
        self.response = self.query_engine.query(self.query)
    def getresponse(self):
        return self.response
    def getquery(self):
        return self.query
    def getdocs(self):
        return self.documents
    def getindex(self):
        return self.index
#building the index
#documents = SimpleDirectoryReader('data').load_data()
#index = vectorstoreindex.from_documents(documents)

#query_engine = index.as_query_engine()
#query='Write me a new contract for Alex Inc that uses similar details.'
#response = query_engine.query(query)
#print(response)
#obj = Vector()
#obj.onetime()


