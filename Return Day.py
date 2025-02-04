#Patric Natindim
#2 Feb 2025

#Computes the day you will return from stay

start_day = int(input("Start day number: "))
length_stay = int(input("Length of stay: "))

return_day = (start_day + length_stay) % 7

print("Return day number: " + str(return_day))
