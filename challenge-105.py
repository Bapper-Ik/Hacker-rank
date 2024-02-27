'''
Task

Debug the given function print_from_stream using the default value of one of its arguments.
This function should print the first  values returned by get_next() method of stream object provided as an argument. Each of these values should be printed in a separate line.

Whenever the function is called without the stream argument, it should use an instance of EvenStream class defined in the code stubs above as the value of stream.

Your function will be tested on several cases.

'''

# to solve it, i've add a, if-statement to test if stream = None, then it'll set it to EvenStream() class by default

class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

def print_from_stream(n, stream=None):

    # challeng inplementation
    if stream is None:
        stream = EvenStream()

    for _ in range(n):
        print(stream.get_next())


queries = int(input())
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())
