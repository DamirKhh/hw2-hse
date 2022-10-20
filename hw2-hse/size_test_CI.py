from main import _mult
a = [int(i) for i in open('/home/runner/work/hw2-hse/hw2-hse/hw2-hse/t5.txt').readline().split()]

answer = _mult(a)
import sys
answer_size = sys.getsizeof(answer)
result = "Для " + str(len(a)) + " чисел" + ' - ' + str(answer_size) + ' byte'
print(result)
with open("results_size.txt" , 'a') as file:
    file.write('\n' + result )


