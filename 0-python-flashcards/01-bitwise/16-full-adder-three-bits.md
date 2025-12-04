# Q: How do I add three bits: a + b + carry_in?

# A: Sum bit = XOR all three
#    Carry out = any two or more are 1

```python
sum_bit = a ^ b ^ carry_in

carry_out = (a & b) | (a & carry_in) | (b & carry_in)
# Translation: carry if (a AND b) OR (a AND carry) OR (b AND carry)
```

**Practice this truth table:**
```
a  b  cin | sum  cout
0  0  0   | 0    0
0  0  1   | 1    0
0  1  0   | 1    0
0  1  1   | 0    1
1  0  0   | 1    0
1  0  1   | 0    1
1  1  0   | 0    1
1  1  1   | 1    1
```
