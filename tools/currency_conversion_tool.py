from utils.currency_convertor import CurrencyConverter
import os
from langchain_core.tools import tool
from typing import List
class CurrencyConverterTool:

    def __init__(self):
        
        self.api_key=os.getenv("EXCHANGE_RATE_API_KEY")
        self.currency_service=CurrencyConverter(api_key=self.api_key)
        self.currency_convertor_tool_list=self._setup_tools()

    def _setup_tools(self)->List:
        """Setup all tools for currency convertor tool"""

        @tool
        def convert_currency(amount:float,from_currency:str,to_currency:str):
            """convert amount from one currency to another"""
            return self.currency_service.convert(amount,from_currency,to_currency)
        
        return [convert_currency]
