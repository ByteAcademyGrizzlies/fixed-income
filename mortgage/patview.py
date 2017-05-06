import matplotlib.pyplot as plt
class plotter:
    def __init__():
        pass

    def print_basic(mortgage_metric_holder):
        print(mortgage_metric_holder.total_payments_in_mortgage)

    def print_advanced(mortgage_metric_holder):
        list_of_months = []
        cumulative_payment = []
        for month in mortgage_metric_holder.amoritization_schedule:
            list_of_months.append(month.current_month)
            cumulative_payment.append(month.cumulative_principal)
        plt.plot(list_of_months, cumulative_payment)
        plt.xlabel("Month")
        plt.ylabel("Cumulative Principal")
        plt.title("pat just printed some shit")
        plt.grid(True)
        plt.axis([0, 360, 0, 33000])
        # Display the graph
        plt.show()
