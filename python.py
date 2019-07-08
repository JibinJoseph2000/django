
def calculate(total_amt,discount_amt):
    
#total_amt=int(input())
#discount_amt=int(input())
#print(calculate(total_amt,discount_amt))
    if not (type (total_amt) == int and type (discount_amt) == int):
        return ("Invalid")
    if total_amt<=0:
        return("Total amount cannot be zero")
    return (discount_amt/total_amt)*100