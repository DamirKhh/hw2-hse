def open_file():
    file = input('Введите название файла: ')
    with open(file,'r') as f:
        a = [int(i) for i in f.read().splitlines()[0].split()]
    return a
a = open_file()


from datetime import datetime
import time
start_time = datetime.now()
def _mult(a):
    answer = 1
    for i in range(len(a)):
        answer = answer * a[i]
    return answer
answer4 = _mult(a)
result = "Для " + str(len(a)) + " чисел" + ' - ' + str(datetime.now()-start_time)
print(datetime.now()-start_time)
with open("results.txt" , 'a') as file:
    file.write('\n' + result )

