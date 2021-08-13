"""Task1"""

class EnumerateWithIndex:

    def __init__(self, _iterable, _from=0):
        self._iterable = _iterable
        self._from = _from
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter > len(self._iterable):
            raise StopIteration
        else:
            try:
                self.counter += 1
                return f'{self._from+self.counter} {self._iterable[self.counter]}'
            except:
                Exception("\nIter is ended")


if __name__ == '__main__':
    a = "qwerty"
    for i in EnumerateWithIndex(a, 10):
        print(i)

"""Task2"""


class RangeFunction:

    def __init__(self, _start, _stop, _step):
        self._start = _start
        self._stop = _stop
        self._step = _step

    def __iter__(self):
        self._start -= self._step
        return self

    def __next__(self):
        self._start += self._step
        if self._start < self._stop:
            return self._start
        raise StopIteration


if __name__ == '__main__':
    a = RangeFunction(1, 100, 1)
    for i in a:
        print(i)


class CountDays:

    def __init__(self, iterable: str, ind=0):
        self.iterable = iterable
        self.ind = ind

    def __iter__(self):
        print(f"We have {len(self.iterable[self.ind:])} days for protection")
        return self

    def __next__(self):
        if self.ind < len(self.iterable):
            old_ind = self.ind
            self.ind += 1
            return f"We have  {len(self.iterable[old_ind:])} days for protection!"
        else:
            print(f"we will all die!")
            raise StopIteration

if __name__ == '__main__':
    dante = CountDays("i need more times", 3)
    for i in dante:
        print(i)
