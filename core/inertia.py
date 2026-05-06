def calculate_ldiw(w1, w2, itr, max_itr):
    return (w1 - w2) * ((max_itr - itr) / max_itr) + w2


def calculate_aiw(w1, w2, ps):
    return (w1 - w2) * ps + w2


def calculate_ldaiw(w1, w2, ps, itr, max_itr):
    if ps <= 0:
        ps = 1.0
    # linear decrease base (from LDIW)
    linear   = (w1 - w2) * ((max_itr - itr) / max_itr) + w2
    # adaptive boost when particles are not improving (from AIW)
    # boost is larger when Ps is low (stuck) and early in search
    boost    = (w1 - w2) * (1.0 - ps) * ((max_itr - itr) / max_itr)
    w        = linear + boost
    # allow slight exploration above w1 but cap at 1.2 for stability
    return max(w2, min(1.2, w))
