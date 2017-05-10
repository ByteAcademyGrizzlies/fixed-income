from model import *
import math

class Mortgage_Calculator:

    @staticmethod
    #class level function. So, we can call it WITHOUT instantiating it.
    #remove all
    def calculate(principal, annual_interest_rate, term_in_years):
        term_in_months = (term_in_years * 12) + 1
        object_array = []
        outstanding_principal = principal
        cumulative_interest = 0
        for month in range(1, term_in_months):
            holder = Monthly_Mortgage_Details()
            holder.principal_balance = outstanding_principal
            holder.current_month = month
            holder.mortgage_month = Mortgage_Calculator.calculate_mortgage_term(term_in_years)
            holder.monthly_mortgage_payment = Mortgage_Calculator.calculate_monthly_mortgage_payment(principal, annual_interest_rate, term_in_years)
            holder.interest_component = Mortgage_Calculator.calculate_interest_componet(holder.principal_balance, annual_interest_rate)
            holder.principal_component = Mortgage_Calculator.calculate_principal_component(holder.monthly_mortgage_payment, holder.interest_component)
            cumulative_interest += holder.interest_component
            holder.cumulative_interest = cumulative_interest
            holder.cumulative_principal = Mortgage_Calculator.calculate_cumulative_principal(holder.principal_component, holder.current_month)
            holder.cumulative_payment = Mortgage_Calculator.calculate_cumulative_payment(holder.monthly_mortgage_payment, holder.current_month)
            outstanding_principal -= holder.principal_component
            object_array.append(holder)
        #create new instance of mortgage_level_metrics object
        mortgage_metric_holder = Mortgage_Level_Metrics()
        #calculate subsequent downstream morgage level metrics
        mortgage_metric_holder.total_payments_in_mortgage = Mortgage_Calculator.calculate_total_payments_in_mortgage(object_array)
        #set a field in this instance equal to object arrray returned above
        mortgage_metric_holder.amoritization_schedule = object_array
        return mortgage_metric_holder

    def calculate_mortgage_term(term_in_years):
        return term_in_years * 12

    def calculate_monthly_mortgage_payment(principal, annual_interest_rate, term_in_years):
        monthly_interest_rate = annual_interest_rate / (100*12)
        term_in_months = term_in_years * 12
        monthly_mortgage_payment = principal * \
            (monthly_interest_rate/(1-math.pow((1+monthly_interest_rate), (-term_in_months))))
        return monthly_mortgage_payment

    def calculate_interest_componet(principal_balance, annual_interest_rate):
        monthly_interest_rate = annual_interest_rate / (100*12)
        interest_component = principal_balance * monthly_interest_rate
        return interest_component

    def calculate_principal_component(monthly_mortgage_payment, interest_component):
        principal_component = monthly_mortgage_payment - interest_component
        return principal_component

    #correct this - keep running tab
    def calculate_cumulative_principal(principal_component, current_month):
        return principal_component * current_month

    def calculate_principal_balance(principal, principal_component, current_month):
        return principal - (principal_component * current_month)

    def calculate_cumulative_payment(monthly_mortgage_payment, current_month):
        return monthly_mortgage_payment * current_month

    def calculate_total_payments_in_mortgage(object_array):
        total_payments_in_mortgage = 0
        for holder in object_array:
            total_payments_in_mortgage += holder.monthly_mortgage_payment
        return total_payments_in_mortgage
