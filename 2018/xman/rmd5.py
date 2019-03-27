import multiprocessing
from concurrent import futures
import sys
import os
import md5


BASENUM = 1000000
global encoded
global stop
global result
stop = False


def md5x(str):
    m1 = md5.new()
    m1.update(str)
    return m1.hexdigest()


class Multicpu():

    def __init__(self, cpu_num, thread_num):
        self.cpu_num = cpu_num
        self.thread_num = thread_num

    def _multi_cpu(self, func, job_queue, timeout):
        if getLen(job_queue) == 0:
            return []
        index = get_index(job_queue, self.cpu_num)

        cpu_pool = multiprocessing.Pool(processes=self.cpu_num)
        mgr = multiprocessing.Manager()
        process_bar = mgr.list()
        for i in range(self.cpu_num):
            process_bar.append(0)

        result_queue = cpu_pool.map(_multi_thread, [[func, self.cpu_num, self.thread_num, job_queue[
                                    index[i][0]: index[i][1] + 1], timeout, process_bar, i] for i in range(len(index))])

        result = []
        for rl in result_queue:
            for r in rl:
                result.append(r)
        return result


def _func(argv):
    argv[2][argv[3]] = round((argv[4] * 100.0 / argv[5]), 2)
    sys.stdout.write(str(argv[2]) + ' ||' + '->' + "\r")
    sys.stdout.flush()
    return argv[0](argv[1])


def _multi_thread(argv):
    thread_num = argv[2]
    if getLen(argv[3]) < thread_num:
        thread_num = argv[3]

    func_argvs = [[argv[0], argv[3][i], argv[5], argv[6],
                   i, len(argv[3])] for i in range(len(argv[3]))]

    result = []
    if thread_num == 1:
        for func_argv in func_argvs:
            result.append(_func(func_argv))
        return result

    # else
    thread_pool = futures.ThreadPoolExecutor(max_workers=thread_num)

    result = thread_pool.map(_func, func_argvs, timeout=argv[4])

    return [r for r in result]


def get_index(job_queue, split_num):
    job_num = getLen(job_queue)

    if job_num < split_num:
        split_num = job_num
    each_num = job_num / split_num

    index = [[i * each_num, i * each_num + each_num - 1]
             for i in range(split_num)]

    residual_num = job_num % split_num
    for i in range(residual_num):
        index[split_num - residual_num + i][0] += i
        index[split_num - residual_num + i][1] += i + 1

    return index


def getLen(_list):
    if _list == None:
        return 0
    return len(_list)


def multi_cpu(func, job_queue, cpu_num=1, thread_num=1, timeout=None):
    multicpu_instance = Multicpu(cpu_num, thread_num)
    return multicpu_instance._multi_cpu(func, job_queue, timeout)


def runmd5(num):
    global encoded
    global stop
    start = BASENUM * (int(num))
    i = start
    while i <= start * 10:
        if os.getenv('runmd5') or stop:
            break
        if md5x(str(i))[0:6] == encoded:
            print('DeCode : %d\n' % i)
            os.setenv('runmd5', '1')
            stop = True
            return i
        i += 1
    return False

if __name__ == '__main__':
    global encoded
    encoded = raw_input('code : ')
    while encoded:
        os.setenv('runmd5', '0')
        print('Runing... %s' % encoded)
        m = multi_cpu(runmd5, [i for i in range(1, 100)], 5, 10)
        print(m)
        encoded = raw_input('code : ')
