def latest(scores):
    return scores[-1]


def personal_best(scores):
    best = float('-inf')
    for score in scores:
        if score > best:
            best = score
    return best


def personal_top_three(scores):
    best_three = []
    best_index = 0
    count = 0
    while (len(scores) > 0 and count < 3):    
        best = float('-inf')
        for i in range(len(scores)):
            if scores[i] > scores[best_index]:
                best_index = i
        best = scores[best_index]        
        best_three.append(best)
    
    return best_three 