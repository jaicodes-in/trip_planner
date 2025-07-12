import os
from dotenv import load_dotenv
from typing import List,Literal,Optional,Any
from pydantic import BaseModel, Field
from langchain_groq import ChatGroq
from utils.config_loader import load_config
load_dotenv()

class ConfigLoader():
    
    def __init__(self):
        print('loading config file')
        self.config=load_config()

    def __getitem__(self,key):
        return self.config[key]

class ModelLoader(BaseModel):
    
    model_provider:Literal['groq','openai'] = 'groq'
    config: Optional[ConfigLoader]=Field(default=None,exclude=True)

    def model_post_init(self, __context:Any):
        self.config=ConfigLoader()

    class Config:
        arbitrary_types_allowed = True

    def load_llm(self):
        """
        Load and return the model
        """
        print('LLM loading')

        if self.model_provider == "groq":
            print('--------loading LLM---------')
            groq_api_key=os.getenv("GROQ_API_KEY")
            model_name=self.config["llm"]["groq"]["model_name"]
            llm=ChatGroq(model=model_name,api_key=groq_api_key)

        return llm


        
    

        
        
