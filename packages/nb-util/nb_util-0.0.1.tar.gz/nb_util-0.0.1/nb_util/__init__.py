import joblib
from tqdm import tqdm
import caffeine

import platform

def can_caffeinate():
    return platform.system() == "Darwin"

def do_parallel(fn, loop, n_jobs=-1, progress=True, keep_alive=True):
    if progress:
        loop = tqdm(loop)
    with joblib.Parallel(n_jobs=-1) as par:
        if keep_alive and can_caffeinate():
            caffeine.on(display=True)
            res = par(joblib.delayed(fn)(l) for l in loop)
            caffeine.off()
        else:
            res = par(joblib.delayed(fn)(l) for l in loop)
    return res