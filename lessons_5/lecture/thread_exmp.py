3333from threading import Thread
import time


def io_bound(id_, sec):
    print(f'{id_} Уснула')
    time.sleep(sec)
    print(f'{id_} Проснулась')


start = time.time()
t1 = Thread(target=io_bound, args=(1, 1), name='Thread-One', daemon=True)
t2 = Thread(target=io_bound, args=(2, 2), name='Thread-Two', daemon=True)
t3 = Thread(target=io_bound, args=(3, 3), name='Thread-Three', daemon=True)
t1.start()
t1.join()
t2.start()
t2.join()
t3.start()
t3.join()

print(int(time.time()-start))