def func_salary(sal_1):
    """method"""
    if 10000<= sal_1<=90000:
        return "Eligible"
    return "Not Eligible"
a=func_salary(10000)
print(a)
# if start <= x <= end: