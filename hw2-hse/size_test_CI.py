from main import _mult
a = [int(i) for i in open('/home/runner/work/hse-tz2-2022/hse-tz2-2022/hw2-hse/t5.txt').readline().split()]

answer = _mult(a)
import sys
answer_size = sys.getsizeof(answer)
result = "Для " + str(len(a)) + " чисел" + ' - ' + str(answer_size) + ' byte'
print(result)
with open("results_size.txt" , 'a') as file:
    file.write('\n' + result )


