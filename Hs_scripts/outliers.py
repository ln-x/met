

def is_outlier(points, threshold=0.5):
    if len(points.shape) == 1:
        points = points[:,None]

    median = np.median(points, axis=0)

    diff = np.sum((points-median)**2, axis=-1)
    diff = np.sqrt(diff)

    med_abs_deviation = np.median(diff)

    modified_z_score = 0.6745 * diff / med_abs_deviation
    return modified_z_score > threshold

x = np.random.random(100)
buckets = 50
x = np.r_[x, -49, 95, 100, -100]

filtered = x[~is_outlier(x)]
print x
print filtered