def multiple_choice(right_answer, given_answer):
    if given_answer is None:
        return 0
    elif right_answer == given_answer:
        return 1
    elif given_answer != right_answer:
        return -0.2