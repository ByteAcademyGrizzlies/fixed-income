from .base_view import BaseView
import matplotlib.pyplot as plt


class GraphView(BaseView):
    """docstring for GraphView"""

    def __init__(self):
        super(GraphView, self).__init__()

    def display_schedule(self, schedule):
        """Graphs out the details of the schedule using matplotlib"""

