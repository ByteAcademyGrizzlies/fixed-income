from calculator import *

class Monthly_Mortgage_Details:
    def __init__(self):
        self.current_month = None
        self.mortgage_month = None
        self.monthly_mortgage_payment = None
        self.interest_component = None
        self.principal_component = None
        self.cumulative_interest = None
        self.cumulative_principal = None
        self.principal_balance = None

class Mortgage_Level_Metrics:
    def __init__(self):
        self.amoritization_schedule = []
        self.total_payments_in_mortgage = None

'''
class mortgage_level_metrics:
    #insert the other thngs from readme
    #below will be arrray of objects - for each month
    self.amoritization_schedule = []
    #1 element - calculated at terminus of mortgage
    self.total_payments_in_mortgage =
    #calculate function for above:
    #for monthly_object in amoritization_Schedule:
                #sum some shit
'''
