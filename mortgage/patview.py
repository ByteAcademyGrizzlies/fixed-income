import matplotlib.pyplot as plt
class plotter:
    def __init__():
        pass

    def print_basic(mortgage_metric_holder):
        for month in mortgage_metric_holder.amoritization_schedule:
            if month.current_month < 5:
                print("monthly mortgage payment", month.monthly_mortgage_payment)
                print("current month", month.current_month)
                print("interest component", month.interest_component)
                print("principal component", month.principal_component)
                print("cumulative payment", month.cumulative_payment)
                print("cumulative interestt", month.cumulative_interest)
                print("cum principal", month.cumulative_principal)
                print("loan balance", month.principal_balance)

    def print_advanced(mortgage_metric_holder):
        list_of_months = []
        cumulative_payment = []
        cumulative_principal = []
        cumulative_interest = []
        outstanding_principal = []
        outstanding_principal = []
        for month in mortgage_metric_holder.amoritization_schedule:
            list_of_months.append(month.current_month)
            cumulative_payment.append(month.cumulative_payment)
            cumulative_interest.append(month.cumulative_interest)
            cumulative_principal.append(month.cumulative_principal)
            outstanding_principal.append(month.principal_balance)
        plt.plot(list_of_months, cumulative_payment)
        plt.plot(list_of_months, cumulative_interest)
        plt.plot(list_of_months, cumulative_principal)
        plt.plot(list_of_months, outstanding_principal)
        plt.xlabel("Month")
        plt.ylabel("Many a thing")
        plt.title("pat just printed some shit")
        plt.grid(True)
        plt.axis([0, 360, -100000, 200000])
        # Display the graph
        plt.show()
