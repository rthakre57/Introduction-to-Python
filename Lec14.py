# Printing the amount received on an investement under compound interest every year for 10 year.

principal = 20000
rate = 5.0
for years in range(1,11):
	amount = principal*(1+rate/100)**years
	print(f'Amounnt after {years}yr. is Rs.{amount:.4f}')

Output:
Amounnt after 1yr. is Rs.21000.0000
Amounnt after 2yr. is Rs.22050.0000
Amounnt after 3yr. is Rs.23152.5000
Amounnt after 4yr. is Rs.24310.1250
Amounnt after 5yr. is Rs.25525.6313
Amounnt after 6yr. is Rs.26801.9128
Amounnt after 7yr. is Rs.28142.0085
Amounnt after 8yr. is Rs.29549.1089
Amounnt after 9yr. is Rs.31026.5643
Amounnt after 10yr. is Rs.32577.8925
