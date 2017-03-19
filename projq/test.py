# coding:utf-8


def _tasks_test():
    from projq.projq_tasks import add, div, mult

    r1 = add.delay(10, 330)
    print "r1 =>  %s" % r1
    print "r1  =>  %s" % r1.backend
    print "r1   =>  %s" % add.AsyncResult(str(r1)).get()

    r2 = div.delay(10, 4)
    print "r2 =>  %s" % r2
    print "r2  =>  %s" % r2.backend
    print "r2   =>  %s" % add.AsyncResult(str(r2)).get()

    r3 = mult.apply_async((17, 334), queue="web_tasks")
    print "r3 =>  %s" % r3
    print "r3  =>  %s" % r3.backend
    print "r3   =>  %s" % add.AsyncResult(str(r3)).get()


if __name__ == "__main__":
    _tasks_test()
