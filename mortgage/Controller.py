from calculator import *
from model import *
#from view.print_view import PrintView
#from view.graph_view import GraphView


class Controller:
    """The Controller class for the mortgage calculator"""

    def __init__(self):
        self.calculator = Mortgage_Calculator()

    def calculate_mortgage_schedule(self, principal, annual_interest_rate, term_in_years):
        self.calculator.calculate(principal, annual_interest_rate, term_in_years)

controller = Controller()
controller.calculate_mortgage_schedule(200000, 6.5, 30)
