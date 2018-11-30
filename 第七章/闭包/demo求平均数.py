def make_average():
    count = 0
    total = 0

    def average(new_value):
        nonlocal count, total
        total += new_value
        count += 1
        return total / count

    return average


avg = make_average()
avg(10)
avg(11)
print(avg(12))
