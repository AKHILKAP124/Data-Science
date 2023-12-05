"""You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length.
If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles. 
Calculate and print the cost using python 
(Hint: Use power operator ** to find area of a square)"""

len_of_tile = 5.5
area_of_tile = len_of_tile**2

cost_per_sq_feet = 500

total_cost = area_of_tile*cost_per_sq_feet
print("The total cost for replacing all tiles is",total_cost,"rs.")