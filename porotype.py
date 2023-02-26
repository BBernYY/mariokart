import pandas as pd

numbers1 = list(range(10))
numbers2 = list(range(10))
numbers3 = list(range(10))

def find_sums(request, numlist, depth=0, numbers=None):
    numbers = [0 for _ in numlist] if numbers is None else numbers
    if depth == len(numlist):
        txt = ""
        for i in numbers:
            txt += str(i)+'.'
        return [txt, abs(sum(numbers) - request)]
    else:
        sums = pd.DataFrame(columns=['Combination', 'Difference'])
        for i in numlist[depth]:
            numbers[depth] = i
            func = find_sums(request, numlist, depth + 1, numbers)
            if type(func) == type(list()):
                sums.loc[-1] = func
            else:
                df2 = pd.DataFrame(func)
                sums = pd.concat(pd.Series(df2), sums)
        return sums



# request = 23
# results = {}
# for n1 in numbers1:
#     for n2 in numbers2:
#         current = n1 + n2
#         for n3 in numbers3:
# for 
print(find_sums(18, [[2, 4, 9],[3, 7, 2],[2, 5, 8], [3, 4, 5]]).sort_values(('Difference')).head())