import arrow

# Hint:  use Google to find python function

####a) 
date_start_a = '01-02-2013'  
date_stop_a = '07-28-2015'   

####b)  
date_start_b = '12312013'  
date_stop_b = '05282015'  

####c)  
date_start_c = '15-Jan-1994'  
date_stop_c = '14-Jul-2015'  

# days between, takes as input two string dates and a string format
# outputs number of days between them
def days_between(d1, d2, date_format):
    d1 = arrow.get(d1, date_format)
    d2 = arrow.get(d2, date_format)
    return abs((d2 - d1).days)


answer_a = days_between(date_start_a, date_stop_a, 'MM-DD-YYYY')
answer_b = days_between(date_start_b, date_stop_b, 'MMDDYYYY')
answer_c = days_between(date_start_c, date_stop_c, 'DD-MMM-YYYY')
print(answer_a, answer_b, answer_c)

