import datetime
import time
from functools import wraps
from typing import Any

from discord.ext import commands

from settings import Settings


def is_me(func=None, *args, **kwargs):
    def predicate(ctx):
        if ctx.message.author.id == Settings.myID or ctx.message.author.id in args:
            return True
        else:
            return False

    return commands.check(predicate)


def timeit(func):
    """Times a function, usually used as decorator"""

    @wraps(func)
    def timed_func(*args: Any, **kwargs: Any) -> Any:
        """Returns the timed function"""
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed_time = datetime.timedelta(seconds=(time.time() - start_time))
        print(f"{func.__name__}: {elapsed_time}")
        return result

    return timed_func
