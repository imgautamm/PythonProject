#indexing

credit_number = "1234-5678-9012-3456"

#result = (credit_number[4])
#result = (credit_number[:8])
#result = (credit_number[5:])
#result = (credit_number[-2])
#result = (credit_number[::2])
#result = (credit_number[-4:])
#result = (credit_number[0:4] + "xxxx" + credit_number[8:12])
result = (credit_number.replace(credit_number[4:8], "xxxx"))

print(result)