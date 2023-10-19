def solution(text, ending):
    len_of_the_end = len(ending)

    if len_of_the_end == 0 or len_of_the_end > len(text):
        return False
    
    return True if text[-len_of_the_end:] == ending else False


print(solution('abc', 'bc'))
