import pandas as pd
t = 0
def find_sums(request, numlist, depth=0, numbers=None):
    global t
    numbers = [0 for _ in numlist] if numbers is None else numbers
    if depth == len(numlist):
        txt = ""
        for i in numbers:
            txt += str(i)+'.'
        t += 1
        if t % 1000 == 0:
            print(t)
        return [txt, abs(sum(numbers) - request)]
    else:
        sums = pd.DataFrame(columns=['Combination', 'Difference'])
        for i in numlist[depth]:
            numbers[depth] = i
            func = find_sums(request, numlist, depth + 1, numbers)
            if type(func) == type(pd.DataFrame()):
                sums = pd.concat([func, sums])
            else:
                df2 = pd.DataFrame([func], columns=['Combination', 'Difference'])
                sums = pd.concat([df2, sums])

        return sums


def main():
    import utils # imports my customized utils module, with a test and timing function. https://GitHub.com/BBernYY/FancyCoding
    req = 'Mini-Turbo'
    source = {
          "d": pd.read_csv('Mario_Kart_8_Deluxe_drivers.csv'),
          "k": pd.read_csv('Mario_Kart_8_Deluxe_bodies_karts.csv'),
          "g": pd.read_csv('Mario_Kart_8_Deluxe_gliders.csv'),
          "t": pd.read_csv('Mario_Kart_8_Deluxe_tires.csv')
        }
    lists = []
    for k, v in source.items():
        lists.append(list(v[req]))
    df = find_sums(1000, lists)



if __name__ == '__main__': # checks if the code is ran as a file
    main() # starts the main function
