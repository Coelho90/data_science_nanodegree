def quiz_correction(my_answers,answers):
    results= [None, None, None, None, None]
    for index, choice in enumerate(my_answers):
        if choice == answers[index]:
            results[index] = True
        else:
             results[index] = False
    return results



def check_answers(my_answers,answers):
    """
    Checks the five answers provided to a multiple choice quiz and returns the results.
    """
    results = quiz_correction(my_answers,answers)
    count_correct = 0
    count_incorrect = 0
    for result in results:
        if result == True:
            count_correct += 1
        if result != True:
            count_incorrect += 1
    if count_correct/5 > 0.7:
        return "Congratulations, you passed the test! You scored " + str(count_correct) + " out of 5."
    elif count_incorrect/5 >= 0.3:
        return "Unfortunately, you did not pass. You scored " + str(count_correct) + " out of 5."


my_answers = [1,2,3,4,5]
answers = [1,2,3,4,6]
print(check_answers(my_answers,answers))