no_terms = int(input(""))


n1, n2 = 0, 1 #define first two terms, can add as user input as well
count = 0

if  no_terms == 1: #special case where no_terms = 1
   print(n1)
else:
   while count <  no_terms: #incrementer as count to limit
       print(n1)
       sum = n1 + n2
       n1 = n2 #updating values for n1 and n2
       n2 = sum
       count += 1 #incrementing count