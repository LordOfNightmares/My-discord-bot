import concurrent.futures
from functools import wraps, partial

from methods.wrappers import timeit


def threading(func=None, *, workers=4):
    if func is None:
        return partial(threading, workers=workers)

    @wraps(func)
    def wrapper(*args, **kwargs):
        # print(f"{args=}")
        # print(f"{kwargs=}")
        largs = len(args) > 0
        lkwargs = len(kwargs) > 0
        with concurrent.futures.ThreadPoolExecutor(max_workers=workers, thread_name_prefix='T') as executor:
            if largs and lkwargs:
                futures = [executor.submit(func, *arg, *args[1:], **kwargs) for arg in zip(args[0])]
            elif largs:
                futures = [executor.submit(func, *arg, *args[1:]) for arg in zip(args[0])]
            elif lkwargs:
                futures = [executor.submit(func, *kw, **kwargs) for kw in zip(kwargs)]
            return [future.result() for future in concurrent.futures.as_completed(futures) if future.done()]
    return wrapper

def processing(func=None, *, workers=4):
    if func is None:
        return partial(processing, workers=workers)

    @wraps(func)
    def wrapper(*args, **kwargs):
        # print(f"{args=}")
        # print(f"{kwargs=}")
        largs = len(args) > 0
        lkwargs = len(kwargs) > 0
        with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as executor:
            if largs and lkwargs:
                futures = [executor.submit(func, *arg, *args, **kwargs) for arg in zip(args)]
            elif largs:
                futures = [executor.submit(func, *arg, *args) for arg in zip(args)]
            elif lkwargs:
                futures = [executor.submit(func, *kw, **kwargs) for kw in zip(kwargs)]
            return [future.result() for future in concurrent.futures.as_completed(futures) if future.done()]

    return wrapper

# with concurrent.futures.ThreadPoolExecutor(max_workers=10, thread_name_prefix='T') as executor:
#     futures = [executor.submit(func, *arg) for arg in zip(args[0])]

# -----------------------------------TEST-----------------------------------
import logging

logging.basicConfig(format='%(asctime)s| %(threadName)s | %(levelname)-5s| %(message)s',
                    level=logging.WARN,
                    datefmt="%H:%M:%S")


# workers = 10
# from memory_profiler import profile
# @profile(precision=4)
# def test():
#     pass

# @threading(workers=2)
# def test(*args, **kwargs):
#     # print(kwargs)
#     response = args[0]
#     try:
#         logging.info(f'{args=}\t{kwargs=}\t{response=}')
#         # yield response, kwargs
#         return response
#     except Exception:
#         logging.exception(f'Exception:\n\nItem:{args}\n\n')
@timeit
@threading
def test(*args, **kwargs):
    # print(kwargs)
    response = args[0]
    try:
        logging.info(f'{args=}\t{kwargs=}\t{response=}')
        # yield response, kwargs
        return response
    except Exception:
        logging.exception(f'Exception:\n\nItem:{args}\n\n')



def testt(*args, **kwargs):
    # print(kwargs)
    response = args[0]
    try:
        logging.info(f'{args=}\t{kwargs=}\t{response=}')
        # yield response, kwargs
        return response
    except Exception:
        logging.exception(f'Exception:\n\nItem:{args}\n\n')

@timeit
@processing(testt)
def testing(*args, **kwargs):
    return testt(*args, **kwargs)

if __name__ == '__main__':
    vals = range(10000)
    kw = {'a': 1, "b": 2, "c": 3}
    wk = {'a1': True, "b2": False, "c3": None}
    print(testing(vals))
    # print(processing(test, vals))
    # test(vals)
    # print("ANS: ", test(vals), '\n')
    # print("ANS: ", test(*kw), '\n')
    # print("ANS: ", test(*wk), '\n')
    # print("ANS: ", test(**wk), '\n')
    # print("ANS: ", test(*kw, **wk), '\n')

# print(f'{test(vals,ok=1,zok=2)=}')
