
def compound_growth(term, rate):
	#term is the length of time in years, rate is the growth rate
	unit_val = (1 + rate/100) ** term
	return unit_val

def future_value(principal, term, rate):
	#principal is the starting dollar amount
	#term is the length of the investment in years
	#rate is the growth rate or interest rate

	#future_value = float(principal) * (1 + (float(rate)/100)) ** float(term)
	future_value = principal * compound_growth(term, rate)
	return future_value

def min_present_value(future_value, term, rate):
	#calculate the present value required to meet a future value
	present_value = future_value / compound_growth(term, rate)
	return present_value


def annualized_growth(term, unit_val):
	annualized_unit_val = unit_val ** (1/term)
	return (annualized_unit_val - 1)*100

def cumulative_growth(start_val, end_val):
	cum = (end_val/start_val)
	return cum

def calc_yield(start_val, end_val, term):
	yld = annualized_growth(term, cumulative_growth(start_val, end_val))
	return yld

def bond_pv(principal, coupon, term, yld):
	#this function assumes:
	#coupon is a dollar amount (not a rate) 
	#yld is a percentage (not a decimal)

	present_value = 0
	for i in range(1 ,term):
		#print("i ", i)
		#print("discounted coupon ", coupon / (1 + yld/100) ** i)
		present_value += coupon / (1 + yld/100) ** i
		#print("new present val ", present_value)

	present_value += (principal + coupon) / (1 + yld/100) ** term

	return present_value
