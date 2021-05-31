class Node():
    id = int(0)

    def __init__(self, id, begin, length):
        self.id = id
        self.begin = begin
        self.length = length
        self.end = self.begin + self.length - 1  # 末址
        Node.id += 1


class File():
    def __init__(self, id, size):
        self.id = id
        self.size = size
        self.index = []


class Disk():
    def __init__(self):
        self.length = 500
        self.size = 2
        self.empty = []
        self.empty.append(Node(Node.id, 0, self.length))
        self.left = self.length
        self.FCB = []

    def allocate(self, name, size):
        if size <= 0 or size > self.length * self.size:
            return False
        if size % self.size == 0:
            k = size // self.size
        else:
            k = size // self.size + 1
        if k > self.left:
            return False
        k = int(k)
        self.left -= k
        for i in self.FCB:
            if i.id == name:
                return False
        f = File(name, size)
        self.empty.sort(key=self.getBegin)
        # while k > 0:
        #     for i in range(len(self.empty)):
        #         if self.empty[i].length >= k:
        #             for j in range(self.empty[i].begin, self.empty[i].begin + k):
        #                 f.index.append(j)
        #             newbegin = self.empty[i].begin + k
        #             newlength = self.empty[i].length - k
        #             self.empty.pop(i)
        #             if newlength != 0:
        #                 t = Node(Node.id, newbegin, newlength)
        #                 self.empty.insert(i, t)
        #             k = 0
        #             break
        #         else:
        #             for j in range(self.empty[i].begin, self.empty[i].begin + self.empty[i].length):
        #                 f.index.append(j)
        #             k -= self.empty[i].length
        #             self.empty.pop(i)
        fail=0
        while k > 0:
            for i in range(len(self.empty)):
                i=i-fail
                if self.empty[i].length >= k:
                    for j in range(self.empty[i].begin, self.empty[i].begin + k):
                        f.index.append(j)
                    newbegin = self.empty[i].begin + k
                    newlength = self.empty[i].length - k
                    self.empty.pop(i)
                    if newlength != 0:
                        t = Node(Node.id, newbegin, newlength)
                        self.empty.insert(i, t)
                    k = 0
                    break
                else:
                    for j in range(self.empty[i].begin, self.empty[i].begin + self.empty[i].length):
                        f.index.append(j)
                    k -= self.empty[i].length
                    self.empty.pop(i)
                    fail+=1

        self.FCB.append(f)
        return True

    def recycle(self, id):
        t = []
        for i in range(len(self.FCB)):
            if self.FCB[i].id == id:
                t = self.FCB.pop(i).index
                break
        self.left += len(t)
        i = 0
        while i < len(t):
            start = i
            while i < len(t) - 1 and t[i + 1] - t[i] == 1:
                i += 1
            i += 1
            bck = Node(Node.id, t[start], i - start)
            x = Node.id
            idx = 0
            self.empty.append(bck)
            self.empty.sort(key=self.getBegin, reverse=False)
            for j in range(len(self.empty)):
                if self.empty[j].id == x:
                    idx = j
                    break
            if idx == 0 and self.empty[idx].begin + self.empty[idx].length == self.empty[idx + 1].begin:
                tnode = Node(Node.id, self.empty[idx].begin, self.empty[idx].length + self.empty[idx + 1].length)
                del self.empty[idx:idx + 2]
                self.empty.insert(idx, tnode)
            elif idx == len(t) - 1 and self.empty[idx - 1].begin + self.empty[idx - 1].length == self.empty[idx].begin:
                tnode = Node(Node.id, self.empty[idx - 1].begin, self.empty[idx - 1].length + self.empty[idx].length)
                del self.empty[idx - 1:idx + 1]
                self.empty.insert(idx - 1, tnode)
            else:
                b1, b2, b3 = self.empty[idx - 1].begin, self.empty[idx].begin, self.empty[idx + 1].begin
                l1, l2, l3 = self.empty[idx - 1].length, self.empty[idx].length, self.empty[idx + 1].length
                a = self.empty[idx - 1].begin + self.empty[idx - 1].length
                b = self.empty[idx].begin + self.empty[idx].length
                d1 = self.empty[idx].begin
                d2 = self.empty[idx + 1].begin
                if a != d1 and b != d2:
                    continue
                elif a != d1:
                    del self.empty[idx:idx + 2]
                    self.empty.insert(idx, Node(Node.id, b2, l2 + l3))
                elif b != d2:
                    del self.empty[idx - 1:idx + 1]
                    self.empty.insert(idx - 1, Node(Node.id, b1, l1 + l2))
                else:
                    del self.empty[idx - 1:idx + 2]
                    self.empty.insert(idx - 1, Node(Node.id, b1, l1 + l2 + l3))
        return True

    def getBegin(self, a: Node) -> int:
        return a.begin
