
import md5
from concurrent import futures
from multicpu import multi_cpu

code = "0"
_t = False


def md5x(str):
    m1 = md5.new()
    m1.update(str)
    return m1.hexdigest()


def run_md5(arg):
    code = arg
    start = 10000000
    end = 100000000
    if not code:
        return False
    print('[+] Runing...')
    while start <= end:
        res = md5x(str(start))[:len(code)]
        if res == code:
            print('[+] Runing md5 successfully \'%s\'...' % start)
            return start
        start += 1
    return 0


def process_job(job):
	global code
	global _t
	if _t:
		return 1
    res = md5x(str(job))[:len(code)]
    if res == code:
        print('[+] Runing md5 successfully \'%s\'...' % job)
        return job


def fuck_md5(_code):
	global
	code = _code
    result = multi_cpu(process_job, range(start, end), 1, 10)
