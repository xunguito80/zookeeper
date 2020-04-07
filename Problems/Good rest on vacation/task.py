# put your python code here
days = int(input("days? "))
food_cost = int(input("cost food per day?"))
flight = int(input("flight? "))
hotel = int(input("hotel? "))
print((days*(food_cost+hotel)-hotel)+flight*2)