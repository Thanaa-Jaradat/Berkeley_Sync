
import multiprocessing
from multiprocessing import Pipe
import random

def node1(r):
    clock1 = random.randint(1, 5)
    print("Clock Before synchronization: " + str(clock1), end = "\n\n")
    dc = r.recv()
    diff = dc - clock1
    r.send(diff)
    clock1 = r.recv()
    print("Clock after synchronization: " + str(clock1), end = "\n\n")

def node2(r):
    clock2 = random.randint(1, 5)
    print("Clock Before synchronization: " + str(clock2), end = "\n\n")
    dc = r.recv()
    diff = dc - clock2
    r.send(diff)
    clock2 = r.recv()
    print("Clock after synchronization: " + str(clock2), end = "\n\n")


def daemon(s1, s2):
    diffs_list = []
    clock = random.randint(1, 5)
    print("Clock at daemon before sync is: ", str(clock), end = "\n\n")
    s1.send(clock)
    s2.send(clock)
    diffs_list.append(s1.recv())
    diffs_list.append(s2.recv())
    sum = 0
    for i in range(len(diffs_list)):
        sum += diffs_list[i]
    avg_diff = int(sum / 3)
    clock = clock + avg_diff
    print("Clock at daemon after sync is: " + str(clock), end = "\n\n")
    s1.send(clock)
    s2.send(clock)

    


if __name__ == '__main__':
    s1, r1 = Pipe() # s1 end is for daemon to communicate with node1,
    #r1 end is for node1 to communicate with the daemon
    s2, r2 = Pipe()
    master = multiprocessing.Process(target = daemon, args = (s1, s2,))
    proc2 = multiprocessing.Process(target = node1, args = (r1,))
    proc3 = multiprocessing.Process(target = node2, args = (r2,))
    master.start()
    proc2.start()
    proc3.start()