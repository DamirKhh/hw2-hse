from main import _mult
a = [int(i) for i in open('/home/runner/work/hw2-hse/hw2-hse/hw2-hse/t5.txt').readline().split()]

from datetime import datetime
import time
start_time = datetime.now()

answer4 = _mult(a)
result = "Для " + str(len(a)) + " чисел" + ' - ' + str(datetime.now()-start_time)
print(datetime.now()-start_time)
with open("results.txt" , 'a') as file:
    file.write('\n' + result )

