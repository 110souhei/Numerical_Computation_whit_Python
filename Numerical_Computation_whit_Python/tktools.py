import numpy as np
def relerr(approx,true_val):
    relerr = np.abs(approx - true_val)

    if isinstance(approx,(list,np.ndarray)):
        if true_val.any() == 0.0:
            nonzero_abs_true_val = []
            for val in true_val:
                if val == 0.0:
                    nonzero_abs_true_val.append(1.0)
                else:
                    nonzero_abs_true_val.append(np.abs(val))
        else:
            nonzero_abs_true_val = np.abs(true_val)
        relerr /= nonzero_abs_true_val
    else:
        if true_val != 0.0:
            relerr /= np.abs(true_val)
    return relerr