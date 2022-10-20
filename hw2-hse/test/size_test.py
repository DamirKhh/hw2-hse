def open_file():
    file = input('Введите название файла: ')
    with open(file,'r') as f:
        a = [int(i) for i in f.read().splitlines()[0].split()]
    return a
a = open_file()



def _mult(a):
    answer = 1
    for i in range(len(a)):
        answer = answer * a[i]
    return answer
answer = _mult(a)

import sys
answer_size = sys.getsizeof(answer)
result = "Для " + str(len(a)) + " чисел" + ' - ' + str(answer_size) + ' byte'
print(result)
with open("results_size.txt" , 'a') as file:
    file.write('\n' + result )


