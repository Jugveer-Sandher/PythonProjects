# This is the user interface where your name will be said back to you.
name = input("Enter your name:")
print("Hello", name)

# adding the two numbers together x and y.
x = 5
y = 10
xy_sum = x + y
print(x, "+", y, "=", xy_sum)

# multiplying two numbers together a_value and b_value.
a_value = 10.5
b_value = 4.0
c_value = a_value * b_value
print(a_value, "*", b_value, "=", c_value)

print(int(c_value) - xy_sum)

# If you do not convert c_value into a integer than the sum will get printed as a floating point.
# Indicates the program is over.
print("This program is done")