import numpy as np
import pandas as pd

# Q1
arr = np.arange(11, 30, 2)
print(arr)
print("Dimensions:", arr.ndim)
print("Total elements:", arr.size)

# Q2
arr = np.linspace(5, 35, 7)
print(arr)

# Q3
arr = np.full((4, 3), 9)
arr[2, 1] = 0
print(arr)

# Q4
a = np.array([6, 12, 18, 24])
print(a % 5)

# Q5
arr = np.array([14, 28, 42, 56, 70, 84])
print(arr[1:6:2])

# Q6
arr = np.array([-16, 25, -36, 49])
abs_arr = np.abs(arr)
print(abs_arr)
print(np.sqrt(abs_arr))

# Q7
m = np.arange(7, 13).reshape(3, 2)
print(m)
print("Shape before:", m.shape)
print(m.T)
print("Shape after:", m.T.shape)

# Q8
temperatures = np.array([18, 22, 27, 31, 24, 19])
print("Range:", temperatures.max() - temperatures.min())
print("Median:", np.median(temperatures))

# Q9
values = np.array([4, 9, 4, 2, 9, 7, 2, 4])
u = np.unique(values)
print(u)
print("Distinct values:", len(u))

# Q10
speed = np.array([35, 62, 48, 81, 55])
result = np.where(speed >= 60, "Fast", "Normal")
print(result)

# Q11
books = pd.Series([24, 31, 19, 27], index=["Monday", "Tuesday", "Wednesday", "Thursday"])
print(books)

# Q12
prices = pd.Series([45000, 18000, 22000], index=["Laptop", "Tablet", "Phone"])
print(prices["Tablet"])

# Q13
rainfall = pd.Series([12, 0, 18, 5, 23])
print(rainfall[rainfall > 10])

# Q14
d = {'Gold': 7200, 'Silver': 95, 'Copper': 850}
s = pd.Series(d)
print(s.index)
print(s.values)

# Q15
ratings = pd.Series([3.5, 4.2, 2.8, 4.7])
ratings.name = "Customer Ratings"
ratings.index.name = "Review ID"
print(ratings)

# Q16
s = pd.Series([11, 22, 33], index=['X1', 'X2', 'X3'])
print('X2' in s.index)
print('X4' not in s.index)

# Q17
stock = pd.Series([16, 28, 12], index=['Keyboard', 'Mouse', 'Monitor'])
print(stock.to_dict())

# Q18
marks = {'Hindi': 78, 'English': 84, 'Computer': 91}
s = pd.Series(marks, index=['Computer', 'Hindi', 'Art', 'English'])
print(s)
print("Missing entry:", s[s.isnull()].index[0])

# Q19
expenses = pd.Series([1200, None, 850, None, 600])
print(expenses.isnull())
print(expenses.notnull())

# Q20
a = pd.Series([8, 15, 22], index=['P', 'Q', 'R'])
b = pd.Series([4, 6, 10], index=['R', 'P', 'Q'])
print(a + b)
print("Pandas adds by matching labels, not by position. P = 8 + 6 = 14, Q = 15 + 10 = 25, R = 22 + 4 = 26.")

# Q21
sales = np.array([
    [120, 150, 180],
    [140, 160, 175],
    [135, 155, 190],
    [150, 170, 200]
])
print("Total sales per day:", sales.sum(axis=1))
print("Total sales per product:", sales.sum(axis=0))
print("Day with highest combined sales: Day", sales.sum(axis=1).argmax() + 1)

# Q22
arr = np.arange(10, 46).reshape(6, 6)
print(arr)
sub = arr[2:6, 1:5]
print(sub)
print("Mean:", sub.mean())

# Q23
weights = np.array([48, 62, 75, 81, 54, 69, 90])
print(weights[weights > 70])
new_weights = np.where(weights < 55, 55, weights)
print(new_weights)
print(weights)

# Q24
quantity = np.array([3, 5, 2, 7])
price = np.array([120, 80, 250, 60])
total_cost = quantity * price
bill = total_cost.sum()
percent = total_cost / bill * 100
print("Total cost of each product:", total_cost)
print("Overall bill:", bill)
print("Percentage contribution:", np.round(percent, 2))

# Q25
arr = np.array([[2, 4, 6, 8],
                [1, 3, 5, 7],
                [10, 20, 30, 40]])
print("Row variance:", arr.var(axis=1))
print("Row std:", arr.std(axis=1))
print("Column variance:", arr.var(axis=0))
print("Column std:", arr.std(axis=0))
print("axis=0 works down the rows, so it gives one result for each column. axis=1 works across the columns, so it gives one result for each row.")

# Q26
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8], [9, 10], [11, 12]])
print(A @ B)
try:
    print(A * B)
except ValueError as err:
    print("Error:", err)
print("Matrix multiplication needs columns of A (3) = rows of B (3), so the result is 2x2. Element-wise multiplication needs both arrays to have the same shape (or be broadcastable), but (2,3) and (3,2) are not.")

# Q27
np.random.seed(42)
nums = np.random.randint(10, 100, 25)
print(nums)
sorted_nums = np.sort(nums)
print(sorted_nums)
print("Five largest:", sorted_nums[-5:][::-1])
print("Unique observations:", len(np.unique(nums)))

# Q28
a = np.array([5, 10, 15, 20, 25, 30])
b = a[1:5]
c = a[1:5].copy()
b[1] = 99
c[2] = 77
print("a =", a)
print("b =", b)
print("c =", c)
print("b is a view, so it shares memory with a and changing b[1] also changed a[2]. c is an independent copy, so changing c does not affect a.")

# Q29
dept_a = pd.Series({'Jan': 250, 'Feb': 310, 'Mar': 290})
dept_b = pd.Series({'Mar': 180, 'Jan': 210, 'Apr': 260})
total = dept_a + dept_b
print(total)
print("Missing labels:", list(total[total.isnull()].index))
print("Index alignment: Pandas matches the values by label. If a label is present in only one Series, the result is NaN.")

# Q30
attendance = pd.Series([82, 67, 91, 74, 58], index=['S101', 'S102', 'S103', 'S104', 'S105'])
low = attendance[attendance < 75]
print(low)
print(list(low.index))
print("Count:", len(low))

# Q31
inventory = {'Pen': 50, 'Pencil': 80, 'Eraser': 40, 'Scale': 25}
labels = ['Scale', 'Pen', 'Marker', 'Eraser']
s = pd.Series(inventory, index=labels)
print(s)
print("Missing value: Marker (NaN)")
print("Pencil does not appear because it is not in the labels list. Only the labels given in index are taken from the dictionary.")

# Q32
s1 = pd.Series([100, 200, 300], index=['North', 'South', 'East'])
s2 = pd.Series([10, 20, 30], index=['South', 'West', 'North'])
result = s1 - s2
print(result)
print(result.notnull())
print(result[result.notnull()])
print("Subtraction is label-based, so North is subtracted from North and South from South whatever the position is. East and West are present in only one Series, so they become NaN.")

# Q33
consumption = pd.Series([180, 310, 275, 220, 390], index=['House1', 'House2', 'House3', 'House4', 'House5'])
high = consumption[consumption > 250]
print(high)
d = high.to_dict()
print(d)
new_series = pd.Series(d)
print(new_series)

# Q34
s = pd.Series({'A': 45, 'B': 70, 'C': 55}, index=['C', 'D', 'A', 'B'])
s.name = 'Performance'
s.index.name = 'Group'
print(s[s >= 50])
print(s.isnull())
print("Series name:", s.name)
print("Index name:", s.index.name)

# Q35
np.random.seed(42)
marks = np.random.randint(20, 101, size=(12, 4))
print(marks)
print("Student average:", np.round(marks.mean(axis=1), 2))
print("Test mean:", np.round(marks.mean(axis=0), 2))
print("Test std:", np.round(marks.std(axis=0), 2))
passed_all = (marks >= 40).all(axis=1)
print("Students passing all four tests:", passed_all.sum())
avg = marks.mean(axis=1)
print("Students with average >= 75:", np.where(avg >= 75)[0] + 1)
print("Test with greatest variation: Test", marks.std(axis=0).argmax() + 1)
print("Numbering convention: students are numbered 1 to 12 (row index + 1) and tests are numbered 1 to 4 (column index + 1).")

# Q36
m = np.arange(21, 46).reshape(5, 5)
print(m)
center = m[1:4, 1:4]
print(center, center.shape)
t = center.T
print(t, t.shape)
prod = center @ t
print(prod, prod.shape)
row_sums = prod.sum(axis=1)
print("Row-wise sums:", row_sums)
print("Maximum:", prod.max())
print("Positions of maximum:", np.argwhere(prod == prod.max()).tolist())
print("Dimensions: 5x5 matrix -> central 3x3 -> transpose 3x3 -> product (3x3)@(3x3) = 3x3 -> row sums shape (3,).")

# Q37
np.random.seed(7)
qty = np.random.randint(5, 31, size=(6, 4))
unit_price = np.array([150, 240, 90, 320])
print(qty)
daily_revenue = (qty * unit_price).sum(axis=1)
print("Daily revenue:", daily_revenue)
product_revenue = (qty * unit_price).sum(axis=0)
print("Revenue per product:", product_revenue)
print("Highest revenue day: Day", daily_revenue.argmax() + 1)
total_qty = qty.sum(axis=0)
print("Total quantity per product:", total_qty)
print("Best-selling product by quantity: Product", total_qty.argmax() + 1)
new_price = np.where(total_qty > 100, unit_price * 0.9, unit_price)
print("New prices:", new_price)
print("Original prices:", unit_price)
print("Revenue per product after discount:", (qty * new_price).sum(axis=0))
print("Total revenue after discount:", (qty * new_price).sum())

# Q38
np.random.seed(10)
data = np.random.normal(50, 12, 100)
outside = ((data < 30) | (data > 70)).sum()
print("Values outside 30-70:", outside)
cleaned = np.where(data < 30, 30, np.where(data > 70, 70, data))
print("Original -> mean:", round(data.mean(), 2), "var:", round(data.var(), 2), "std:", round(data.std(), 2), "min:", round(data.min(), 2), "max:", round(data.max(), 2))
print("Cleaned  -> mean:", round(cleaned.mean(), 2), "var:", round(cleaned.var(), 2), "std:", round(cleaned.std(), 2), "min:", round(cleaned.min(), 2), "max:", round(cleaned.max(), 2))
print("Replacing the extreme values with the boundaries pulls them towards the centre, so the variance and standard deviation go down and the min and max become 30 and 70. The mean changes only a little because values were cut on both sides.")

# Q39
branch_a = pd.Series({'Q1': 120, 'Q2': 145, 'Q4': 180})
branch_b = pd.Series({'Q2': 110, 'Q3': 135, 'Q4': 155})
branch_c = pd.Series({'Q1': 95, 'Q3': 125, 'Q4': 140})
total = branch_a + branch_b + branch_c
print(total)
print("Missing values come because each quarter is missing in at least one branch except Q4, and NaN + number = NaN.")
common = branch_a.index.intersection(branch_b.index).intersection(branch_c.index)
print("Common quarters:", list(common))
print("Combined earnings of common quarters:", total[common].to_dict())
total_zero = branch_a.add(branch_b, fill_value=0).add(branch_c, fill_value=0)
print(total_zero)
print("With fill_value=0 the missing branch records are treated as zero earnings, so every quarter gets a total. In the first result NaN means the data is unknown, while here it means the branch earned nothing.")

# Q40
scores = {'R101': 78, 'R102': 65, 'R104': 92, 'R105': 48}
required = ['R105', 'R103', 'R101', 'R106', 'R104', 'R102']
s = pd.Series(scores, index=required)
print(s)
print("Missing student records:", list(s[s.isnull()].index))
valid = s[s >= 70]
print(valid)
d = valid.to_dict()
print(d)
rebuilt = pd.Series(d)
print(rebuilt)
print("Labelled values match:", all(valid[k] == rebuilt[k] for k in rebuilt.index))
print("A missing record means the score is not available (absent, not entered, or not yet checked), which is different from a student scoring 0. Treating it as zero would give wrong averages and unfair results.")
