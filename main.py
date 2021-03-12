from myDeque import Deque

d = Deque()
d.pushRigth(1)
d.pushRigth(2)
d.pushRigth(3)
d.pushRigth(4)
d.pushRigth(5)
d.pushLeft(0)
d.pushLeft(-1)
d.pushLeft("ola")
print(d.size())
print(d.peekRight())
print(d.peekLeft())
print(d.isEmpty())
print(d.show())
