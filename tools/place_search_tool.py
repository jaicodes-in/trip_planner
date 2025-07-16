from utils.place_info_search import GooglePlaceSearchTool,TavilyPlaceSearchTool
import os
from typing import Annotated,List,Literal
from langchain_core.tools import tool
from dotenv import load_dotenv
class PlaceSearchTool:

    def __init__(self):
        load_dotenv()
        self.google_api_key=os.environ.get("GPLACES_API_KEY")
        self.google_search_places=GooglePlaceSearchTool(api_key=self.google_api_key)
        self.tavily_search=TavilyPlaceSearchTool()
        self.place_search_tool_list=self._setup_tools()

    def _setup_tools(self)->List:
        """Setup all tools for the place search tool"""

        @tool
        def search_attraction(place:str)->str:
            """Searches attraction of the place provided"""

            try:
                attraction_result=self.google_search_places.google_search_attractions(place=place)
                if attraction_result:
                    return f'following are the attraction of the {place} as suggested bby google: {attraction_result}'
            except Exception as e:
                tavily_result=self.tavily_search.tavily_search_attractions(place=place)
                return f'''Google cannot find the details due to {e}. \n 
                            following are the attraction of the {place} as suggested by tavily :{tavily_result}'''

        @tool
        def search_restaurants(place:str)->str:
            """Searches restaurants of the place provided"""

            try:
                restaurant_result=self.google_search_places.google_search_restaurants(place=place)
                if restaurant_result:
                    return f'following are the attraction of the {place} as suggested bby google: {restaurant_result}'
            except Exception as e:
                tavily_result=self.tavily_search.tavily_search_restaurants(place=place)
                return f'''Google cannot find the details due to {e}. \n 
                            following are the restaurants of the {place} as suggested by tavily :{tavily_result}''' 
        
        @tool
        def search_activity(place:str)->str:
            """Searches activity of the place provided"""

            try:
                activity_result=self.google_search_places.google_search_activity(place=place)
                if activity_result:
                    return f'following are the activity of the {place} as suggested by google: {activity_result}'
            except Exception as e:
                tavily_result=self.tavily_search.tavily_search_activity(place=place)
                return f'''Google cannot find the details due to {e}. \n 
                            following are the activity of the {place} as suggested by tavily :{tavily_result}''' 
        
        @tool
        def search_transportation(place:str)->str:
            """Searches transportation of the place provided"""

            try:
                transportation_result=self.google_search_places.google_search_transportation(place=place)
                if transportation_result:
                    return f'following are the transportation of the {place} as suggested by google: {transportation_result}'
            except Exception as e:
                tavily_result=self.tavily_search.tavily_search_transportation(place=place)
                return f'''Google cannot find the details due to {e}. \n 
                            following are the transportation of the {place} as suggested by tavily :{tavily_result}''' 
            
        return [search_activity,search_attraction,search_restaurants,search_transportation]

    