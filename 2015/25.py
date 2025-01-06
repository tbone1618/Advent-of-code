#Enter the code at row 3010, column 3019.
# Solution sourced online. My original solution had the rows and columns swapped in the calculation, providing an incorrect result. 

def next_code(cur_code):
	return (cur_code * 252533) % 33554393

def get_code_count(row, column):
	return sum(range(row + column - 1)) + column

first_code = 20151125
code_coords = (3010, 3019)

code_count = get_code_count(*code_coords)
cur_code = first_code
for i in range(code_count - 1):
	cur_code = next_code(cur_code)
print(cur_code)