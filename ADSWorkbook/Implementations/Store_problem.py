queue = [x for x in range(1,21)]
print("Initial Queue:\n", queue)
print(f"\nThe Solaris Store has a queue of {len(queue)} people.\nTo deal with the rush, they have opened another counter to speed up the process.\nHow should the queue be split to ensure that the customers waiting time is only decreased?\nAssume that the reordering takes negligible time compared to the time to process each person.")
queue1 = queue[::2]
queue2 = queue[1::2]
print("First Queue:\n", queue1)
print("Second Queue:\n", queue2)
