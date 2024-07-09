def fibonacci(num_index):
    previous = 0
    current = 1
    if num_index > 0:
        for _ in range(1, num_index):
            next_value = previous + current
            previous = current
            current = next_value
    else:
        return 0
    return current

# 0 1 1 2 3 5 8

# The Fibonacci next numbers are obtained when we add previous and current two numbers together.

0# 0 
1# 1

# Previous1 = 0
# Current1 = 1

2# 1     (next1 = previous1 + current1)

# Previous2 = 1  (current1)
# Current2 = 1   (next1)

3# 2     (next2 = previous2 + current2)

# Previous3 = 1 (current2)
# Current3 = 2 (next2)

4# 3   (next3 = previous3 + current3)

# Previous4 = 2 (current3)
# Current4 = 3 (next3)

5# 5   (next4 = previous4 + current4)

# Previous5 =  3 (current4)
# Current5 = 5 (next4)

6# 8   (next5 = previous5 + current5)

# PAIR PARTNERS - MOSES OLARA and SARAH AGEMO 
