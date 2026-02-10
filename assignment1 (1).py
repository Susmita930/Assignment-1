
# Assignment 1 - Data Analytics (Dictionary)

# Q1: Why are dictionary keys required to be immutable in Python? Explain with a small example
d = {(1,2): "value"}
print("Q1:", d)

# Q2 : Write a program that takes a list of elements and creates a dictionary showing the frequency of each element
def frequency_dict(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return freq

print("Q2:", frequency_dict([1,2,2,3,3,3,4]))

# Q3 : What is the difference between dict.get(key) and dict[key]? Write a code example where get() is safer. 
d = {"a": 10}
print("Q3 get:", d.get("b"))

# Q4 : Write a program to merge two dictionaries and resolve common keys by keeping the larger value. 
def merge_dict(d1, d2):
    result = d1.copy()
    for k, v in d2.items():
        if k in result:
            result[k] = max(result[k], v)
        else:
            result[k] = v
    return result

print("Q4:", merge_dict({"a":10,"b":20},{"b":25,"c":5}))

# Q5 : Using a dictionary comprehension, create a dictionary from a list of integers where keys are numbers and values are their cubes, but only for odd numbers 
nums = [1,2,3,4,5,6,7]
cube_dict = {n: n**3 for n in nums if n % 2 != 0}
print("Q5:", cube_dict)
