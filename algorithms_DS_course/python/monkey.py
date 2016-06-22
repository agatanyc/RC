from random import randrange

goal = 'methinks it is like a weasel' # target string, length=28

def generate_one(str_len):
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    r = ''
    for i in range(str_len):
        r += alphabet[randrange(len(alphabet))]
    return r

def score(goal, test_string):
    score_num = 0
    for i in range(len(goal)):
        if goal[i] == test_string[i]:
            score_num += 1
    return float(score_num) / len(goal)

def main():
    best_score = 0
    best_string = ''
    total_tries = 0
    while best_score < 1:
        new_string = generate_one(len(goal))
        new_score = score(goal, new_string)
        if new_score > best_score:
            best_score = new_score
            best_string = new_string
        total_tries += 1
        if total_tries % 10000 == 0:
            print total_tries, best_score, best_string
    print total_tries, best_score, best_string

if __name__ == '__main__':
    main()
