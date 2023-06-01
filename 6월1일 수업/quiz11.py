time = int(input("Enter hour: "))
ap = int(input("am(1) or pm(2)"))
ahead = int(input("How many hours ahead?"))
total = time+ahead
if ap == 1:
    ap = "am"
    if total > 12:
        ap = "pm"
        result = total - 12
elif ap == 2:
    ap = "pm"
    if total > 12:
        ap = "am"
        result = total - 12
print(f"New hour: {result} {ap}")