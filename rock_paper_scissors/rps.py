#!/usr/bin/python
import sys


def rock_paper_scissors(n):
    rounds_left = n
    # Create a list of choices
    choices = ['rock', 'paper', 'scissors']
    # create a place to store the answers
    answer = []
    plays = []
    # if n <= 0:
    #     return answer

    def recurse(rounds_left, plays):
        # Start base case
        if rounds_left < 1:
            answer.append(plays)
            plays = []
            return answer
        else:
            for i in range(len(choices)):
                current = choices[i]
                # print('current', current, ' Plays: ', plays, type(plays))
                # plays.append(current)
                recurse(rounds_left - 1, plays + [current])
    recurse(rounds_left, plays)
    # print(answer)
    return answer


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
