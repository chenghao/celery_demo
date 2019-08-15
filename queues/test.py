# coding:utf-8


def _tasks_test():
    from queues_tasks import add, div, mult

    r1 = add.apply_async((4455, 3583), queue="web_tasks")
    print "r1 =>  %s" % r1
    print "r1  =>  %s" % r1.backend
    print "r1   =>  %s" % add.AsyncResult(str(r1)).get()

    r2 = div.delay(532, 4.0)
    print "r2 =>  %s" % r2
    print "r2  =>  %s" % r2.backend
    print "r2   =>  %s" % add.AsyncResult(str(r2)).get()

    r3 = mult.apply_async((2568, 534), queue="web_tasks")
    print "r3 =>  %s" % r3
    print "r3  =>  %s" % r3.backend
    print "r3   =>  %s" % add.AsyncResult(str(r3)).get()


if __name__ == "__main__":
    _tasks_test()
