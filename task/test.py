#coding:utf-8


def _tasks_test():
    from tasks_test import add, div, mult

    r1 = add.delay(10, 330)
    print "r1 =>  %s" % r1
    print "r1  =>  %s" % r1.backend
    print "r1   =>  %s" % add.AsyncResult(str(r1)).get()

    r2 = div.delay(10, 3)
    print "r2 =>  %s" % r2
    print "r2  =>  %s" % r2.backend
    print "r2   =>  %s" % div.AsyncResult(str(r2)).get()

    r3 = mult.delay(10, 40)
    print "r3 =>  %s" % r3
    print "r3  =>  %s" % r3.get()


if __name__ == "__main__":
    _tasks_test()
