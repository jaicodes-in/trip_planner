from utils.model_loader import ModelLoader
from prompt_library.prompt import SYSTEM_PROMPT
from langgraph.graph import StateGraph, START,END, MessagesState
from langgraph.prebuilt import tools_condition,ToolNode
from tools.arithmetic_operation_tools import CurrencyConverterTool
from tools.expense_calculator_tool import CalculatorTool
from tools.place_search_tool import PlaceSearchTool
from tools.weather_info_tool import WeatherToolInfo


from dotenv import load_dotenv
load_dotenv()

class GraphBuilder():

    def __init__(self,model_provider:str ='groq'):
        
        self.model_loader = ModelLoader(model_provider=model_provider)
        self.llm = self.model_loader.load_llm()

        self.tools=[]
        self.weather_tools=WeatherToolInfo()
        self.place_search_tools=PlaceSearchTool()
        self.calculator_tools=CalculatorTool()
        self.currency_convertor_tools=CurrencyConverterTool()
        
        self.tools.extend
        

        self.llm_with_tools=self.llm.bind_tools(tools=self.tools)

        self.system_prompt = SYSTEM_PROMPT
        self.graph = None

    def agent_function(self,state:MessagesState)->MessagesState:
        
        """Main agent function"""
        user_question=state['messages']
        input_question=[self.system_prompt] + user_question 
        response=self.llm_with_tools.invoke(input_question)
        return {'messages':[response]}

    def build_graph(self):
        
        graph_builder=StateGraph(state_schema=MessagesState)
        
        graph_builder.add_node('agent',self.agent_function)
        graph_builder.add_node('tools',ToolNode(tools=self.tools))
        
        graph_builder.add_edge(START,'agent')
        graph_builder.add_conditional_edges('agent',tools_condition)
        graph_builder.add_edge("tools","agent")
        graph_builder.add_edge('agent',END)

        self.graph=graph_builder.compile()
        return self.graph
        

    def __call__(self, *args, **kwds):
        return self.build_graph()
    
