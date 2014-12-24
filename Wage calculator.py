'''This is a calculator that works out how
much you will get paid a day for working'''
print ("This is a wage calulator!")

def wage(hours,weekly,monthly,yearly):
   print ("This is what you earn without taking away Tax")
    #You can change the sum depending on how much you earn
   hourEarning = float(input("How much do you earn an hour?"))
   a = hourEarning * hours
   b = hourEarning * hours * weekly
   c = hourEarning * hours * weekly * monthly
   d = hourEarning * hours * weekly * monthly * yearly
   return a,b,c,d

