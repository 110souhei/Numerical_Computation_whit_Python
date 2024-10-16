import math
def newton_sqrt(x,rtol,atol):
    old_sqrt = x
    for times in range(0,10):
        new_sqrt = (old_sqrt + x / old_sqrt) / 2.0
        if math.fabs(new_sqrt - old_sqrt) <= math.fabs(old_sqrt) * rtol + atol:
            return new_sqrt, times
        old_sqrt = new_sqrt
    return new_sqrt, times


rel_tol = 1.0e-10
abs_tol = 1.0e-50


x = 3.0

true_val = math.sqrt(x)
newton_val, iter_times = newton_sqrt(x,rel_tol,abs_tol)
print('math.sqrt(',x, ') = ', true_val)
print('newton   (',x, ') = ', newton_val, ', Iter.Times = ', iter_times)

