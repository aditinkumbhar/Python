asset_costs = [850.,900.0,550.50,450.90,700.70,650.40,560.40]
asset_costs.sort(reverse=True)
print("Top 3 priciest asset:")
for price in asset_costs[:3]:
    print(f"{price:2f}")
