def slices(series, length):
    if len(series) < length or length < 1:
        raise ValueError('invalid length')
    subseries = []
    for i in range(0, len(series) - length + 1):
        subseries.append(series[i:i+length])
    return subseries