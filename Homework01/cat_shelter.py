number_of_cats = 59
cats_per_carrier = 3

# Question 1
carriers_filled = number_of_cats // cats_per_carrier
print("Number of carriers that can be completely filled:", carriers_filled)

# Question 2
cats_remaining = number_of_cats % cats_per_carrier
print("Cats remaining:", cats_remaining)

# Question 3
total_carriers_needed = carriers_filled + 1
print("Total carriers needed to transport all cats:", total_carriers_needed)

# Question 4
total_carriers_owned = 15
carriers_to_purchase = total_carriers_needed - total_carriers_owned
print("Number of carriers that need to be purchased:", carriers_to_purchase)

# Question 5
price_of_carrier = 20
total_cost = price_of_carrier * carriers_to_purchase
print("Cost of buying the additional carriers:", total_cost)

# Question 6
carrier_tax_rate = 0.05
total_cost_with_tax = total_cost * (1 + carrier_tax_rate)
print("Total cost of the additional carriers after tax:", total_cost_with_tax)