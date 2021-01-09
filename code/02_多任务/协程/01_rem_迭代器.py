from collections.abc import Iterable, Iterator


class student(object):
    def __init__(self):
        self.names = list()

    def add(self, other):
        self.names.append(other)

    def __iter__(self):
        return StudentIteror(self)


class StudentIteror:
    def __init__(self,obj):
        self.obj = obj
        self.count = 0

    def __iter__(self):
        pass
    def __next__(self):
        if self.count < len(self.obj.names):
            data = self.obj.names[self.count]
            self.count = self.count + 1
        else:
            # 抛出迭代异常，避免数组越界
            raise StopIteration
        return data



def main():
    studentA = student()
    # 判断 studentA是否是可迭代的对象
    print(isinstance(studentA,Iterable))
    # 判断studentIteror是否是迭代器
    print(isinstance(iter(studentA),Iterator))
    studentA.add("三玖")
    studentA.add("雷姆")
    studentA.add("硝子")
    for i in studentA:
        print(i)



if __name__ == "__main__":
    main()