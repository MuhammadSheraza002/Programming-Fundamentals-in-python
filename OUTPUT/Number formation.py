# express in scientific notation
# 2e4 means 2 ^ 4 (2's power 4)
# 2e-4 means 2 ^ -4 (2's power -4)
number = 234763893.566448
#.2e will resitrict number don't go after 2 floats
print('234763893.566448: ', f"{number: e}")

#also use for built in function foramt

"""number = 234763893.566448
formated_number = format(number,'.2e')#.2e will resitrict number don't go after 2 floats
print('234763893.566448: ',formated_number)"""

number = 0.2347
formated_number = format(number,'E')
print('0.2347: ',formated_number)

print(f'100000000:,: {100000000:,}')
print(f'100000000:_: {100000000:_}')
print(f"10000000000:.2f  {10000000000:.2f}")  #give no till 2 floats
print(f".65:% {.65:%}")
print(f".65:.3%  {.65:.3%}")  #give no till 3 floats with percentage
print(f".65:+  {.65:+}")
print(f".65:+.3%  {.65:+.3%}")  #give no till 3 floats with percentage with sign
print(f"1000000000000000:+,.3%  {1000000000000000:+,.3%}")  # 4 formaters
