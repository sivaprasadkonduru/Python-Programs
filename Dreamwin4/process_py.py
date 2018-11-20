import multiprocessing as mp


def add(*args):
    val = '-'.join([str(i) if not isinstance(i, str) else i for i in args])
    print('{} is the current process running and its pid is {} and value is {}'.format(
        mp.current_process().name, mp.current_process().pid, val))


if __name__ == '__main__':
    p = mp.Process(target=add, args=(3, 4, 5))
    p1 = mp.Process(target=add, args=('hello', 'python', 7, 8, 9))


    p.start()
    p1.start()

    p.join()
    p1.join()

    print('{} is the current process running and its pid is {}'.format(
            mp.current_process().name, mp.current_process().pid))
    print('Processing')
