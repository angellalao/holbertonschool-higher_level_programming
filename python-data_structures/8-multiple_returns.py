#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    else:
        first_let = sentence[0]
        return (len(sentence), first_let)
