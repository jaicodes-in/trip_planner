from utils.expense_calculator import Calculator
from langchain_core.tools import tool

class CalculatorTool:

    def __init__(self):
        self.calculator=Calculator()

        self.calculator_tool_list=self._setup_tools()

        @tool
        def estimate_total_hotel_cost(price_per_night:float,total_days:float)->float:
            """Calculate the total hotel cost"""
            return self.calculator.multiply(a=price_per_night,b=total_days)
        
        @tool
        def calcaulate_total_expenses(*costs:float)->float:
            """Calculate total expense of the trip"""

            return self.calculator.calculate_total(*costs)
        
        @tool
        def calculate_daily_budget_expense(total_cost:float,days:int)->float:
            """Calculate daily expense"""
            return self.calculator.calculate_daily_budget(total=total_cost,days=days)
        
        return [estimate_total_hotel_cost,calcaulate_total_expenses,calculate_daily_budget_expense]