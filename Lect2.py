#Suppose we want to print:The return with simple interest at 5.5% after 5 years is 25500.We can use ‘print’ function with F-string
P = 20000
r = 5.5
t = 5
Amount1 = P+ P*r*t/100
Amount2 = P*(1+ r/100)**t
print(Amount1)
print(Amount2)
print(f'The return with simple interest at {r}% after {t} years is Rs.{Amount1}.')
print(f'The return with compound interest at {r}% after {t} years is Rs.{Amount2}.')
print(f'The return with compound interest at {r}% after {t} years is Rs.{Amount2:6f}.')
print(f'The return with compound interest at {r}% after {t} years is Rs.{Amount2:.10}.')

Output:
25500.0
26139.200128187495
The return with simple interest at 5.5% after 5 years is Rs.25500.0.
The return with compound interest at 5.5% after 5 years is Rs.26139.200128187495.
The return with compound interest at 5.5% after 5 years is Rs.26139.200128.
The return with compound interest at 5.5% after 5 years is Rs.26139.20013.
