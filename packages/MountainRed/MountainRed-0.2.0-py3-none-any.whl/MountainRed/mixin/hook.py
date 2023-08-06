def before_save(obj):
    print("before saving %s " % str(obj))
    pass


def after_save(obj):
    print("after saving %s " % str(obj))
    pass


def before_delete(obj):
    print("before delete %s " % str(obj))
    pass


def after_delete(obj):
    print("after delete %s " % str(obj))
    pass
