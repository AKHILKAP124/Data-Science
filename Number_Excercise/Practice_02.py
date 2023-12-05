"""You bought 9 packets of potato chips from a store.
Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar.
Find out using python, how many dollars is the shopkeeper going to give you back?"""

no_of_packets = 9
cost_per_packet = 1.49
total_cost = no_of_packets * cost_per_packet

amount_given = 20

cash_back = str(amount_given - total_cost)
print("The shopkeeper will return", cash_back+str(" dollar"))