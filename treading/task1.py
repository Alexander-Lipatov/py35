import threading
import random

list = []

def fill(list):
    
    for _ in range(7):
        list.append(random.randint(0, 100))

def my_sum(list):
    print(sum(list))
def mid(list):
    print(sum(list)/len(list))


if __name__ == '__main__':
    t1 = threading.Thread(target=fill, args=('bob',), daemon=True)
    t2 = threading.Thread(target=my_sum, args=('alice',), daemon=True)
    t3 = threading.Thread(target=mid, args=('alice',), daemon=True)
    t1.start()
    t1.join()
    t2.start()
    t3.start()
    t2.join()
    t3.join()