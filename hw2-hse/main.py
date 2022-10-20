def open_file():
    file = input('Введите название файла: ')
    with open(file,'r') as f:
        a = [int(i) for i in f.read().splitlines()[0].split()]
    return a
def _min(a):
    answer = a[0]
    for i in range(len(a)):
        if a[i]<answer:
            answer = a[i]
    return answer

def _max(a):
    answer = a[0]
    for i in range(len(a)):
        if a[i]>answer:
            answer = a[i]
    return answer

def _sum(a):
    answer = 0
    for i in range(len(a)):
        answer = answer + a[i]
    return answer

def _mult(a):
    answer = 1
    for i in range(len(a)):
        answer = answer * a[i]
    return answer
if __name__ == '__main__':
 a = open_file()
 print('Минимальное число:',_min(a))
 print('Макcимальное число:', _max(a))
 print('Сумма чисел в файле:', _sum(a))
 print('Произведение чисел в файле', _mult(a))
