def duration(start, stop):
    """
    spec:
        domain dt.datetime(211, 2, 5), dt.datetime(211, 2, 8):
            import datetime as dt
            results dt.timedelta(days=3)
    """
    return stop - start
