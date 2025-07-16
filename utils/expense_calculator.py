class Calculator:

    @staticmethod
    def multiply(a:int,b:int)->int:

        """
        multiplication of two integers
        
        Args:
            a (int): The first integer
            b (int): The second integer
            
        Returns:
            int : The product of a and b"""
        
        return a*b  
    
    @staticmethod
    def calculate_total(*x:float)->float:

        """
        calculate sum of given list of numbers
        
        Args:
            x (list): List of floating numbers
            
        Returns:
            float: the sum of the numbers in the list x"""
        
        return sum(x)
    
    @staticmethod
    def calculate_daily_budget(total:float,days:int)->float:
        """
        calculate daily budget 
        
        Args:
            total (float): total cost
            days (int): total number of days
            
        Returns:
            float: Expense for a single day
        """

        return total/days if days>0 else 0
    
    