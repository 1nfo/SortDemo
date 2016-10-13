import time, sys

def merge(li):
    if len(li)<2: return
    m = len(li)/2
    l1=li[:m]
    merge(l1)
    l2=li[m:]
    merge(l2)
    p1,p2=0,0
    ret = []
    while p1<len(l1) and p2<len(l2):
        if(l1[p1]>l2[p2]):
            ret.append(l2[p2])
            p2+=1
        else:
            ret.append(l1[p1])
            p1+=1
    if(p1<len(l1)):ret+=l1[p1:]
    if(p2<len(l2)):ret+=l2[p2:]
    li[:]=ret

def heap(li):
    for i in xrange(len(li)/2-1,-1,-1):
        c = i*2+1
        while c<len(li):
            if c+1<len(li) and li[c]<li[c+1]: c+=1
            if li[i]>=li[c]:break
            else:
                tmp = li[i]
                li[i] = li[c]
                li[c] = tmp
                i=c
                c=i*2+1
    for i in xrange(len(li)-1,-1,-1):
        tmp = li[0]
        li[0] = li[i]
        li[i] = tmp
        p,c = 0,1
        while c<i:
            if c+1<i and li[c]<li[c+1]: c+=1
            if li[p]>=li[c] : break
            else:
                tmp = li[p]
                li[p] = li[c]
                li[c] = tmp
                p=c
                c=p*2+1
    li[:]=li


def bubble(li):
    for i in xrange(len(li)):
        for j in xrange(len(li)-i-1):
            if(li[j]>li[j+1]):
                tmp = li[j]
                li[j] = li[j+1]
                li[j+1] = tmp

def insert(li):
    for i in xrange(len(li)):
        for j in xrange(i):
            if li[i]<li[j]:
                tmp = li[i]
                li[i] = li[j]
                li[j] = tmp

def select(li):
    for i in xrange(len(li)):
        for j in xrange(i+1,len(li)):
            min = i
            if(li[min]>li[j]): min=j
            tmp = li[i]
            li[i] = li[min]
            li[min] = tmp

class Timer:
    def __init__(self, msg=""):
        self.msg = msg

    def __enter__(self):
        self.s = time.time()

    def __exit__(self,*arg):
        print "%s : %.2f" %(self.msg,time.time()-self.s),
        sys.stdout.flush()

if __name__ == "__main__":
    times = 100 if(len(sys.argv)<2) else int(sys.argv[1])
    # li = [3,2,4,1,5,3,4,2,3,5,3,4,7,56,4,2,4,6,4,3,5,3,5,7,4,5,2,1,4]*times
    li = range(times*20-1,-1,-1)
    with Timer("insert sort"):
        insert(li)
    with Timer(" bubble sort"):
        bubble(li[:])
    with Timer(" select sort"):
        select(li[:])
    with Timer(" merge sort"):
        merge(li[:])
    with Timer(" heap sort"):
        heap(li)
    print ''

