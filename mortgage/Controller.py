from calculator import *
from model import *
from patview import *

class Controller:
    """The Controller class for the mortgage calculator"""

    def __init__(self):
        #self.plotter = Plotter_array()
        self.plotter = Plotter_graph()

    def calculate_mortgage_schedule(self, principal, annual_interest_rate, term_in_years):
        mortgage_metric_holder = Mortgage_Calculator.calculate(principal, annual_interest_rate, term_in_years)
        self.plotter.printshit(mortgage_metric_holder)

controller = Controller()
controller.calculate_mortgage_schedule(100000, 7.5, 30)
