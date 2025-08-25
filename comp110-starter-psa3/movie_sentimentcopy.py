"""
Module: movie_sentiment

Program to analyze movie reviews and predict the sentiment of new reviews.

Authors:
1) Cavin Nguyen - cavinnguyen@sandiego.edu
2) Jessica Cervantes - jessicacervantes@sandiego.edu
"""

def average_review(word, review_filename):
    """
    This function calculates the average score of reviews inside a file based on a word.

    Parameters:
    word (type: string): The word to look for in the reviews.
    review_filename (type: string): The string that contains the name of a file containing movie reviews.

    Returns:
    (type: float) Returns the average score of the reviews.
    """
    lowercase_word = word.lower()
    review_file = open(review_filename, 'r')
    sum_points = 0
    total_reviews = 0
    for line in review_file:
        # make lower case to avoid case sensitivity
        lower_line = line.lower()  
        split_line = lower_line.split()
        if lowercase_word in split_line:
            sum_points += float(split_line[0])
            total_reviews += 1
    
    # done reading file, so close it
    review_file.close()

    # calculate the average review score
    if total_reviews == 0:
        average = 2.0
    else:    
        average = sum_points / total_reviews
    return float(average)    # replace this with returning the calculated average


def estimate_review_score(movie_review, review_filename):
    """
    This function first removes the puncuation from a file then calculates the total average score of a review based on the scores of 
    the individual words in a review from a file.

    Parameters:
    movie_review (type: string): The review that will be scored
    review_filename (type: string): The string that contains the name of a file containing movie reviews.

    Returns:
    total_est_review_score (type: float) Returns the total estimated score of all the reviews.
    """


    punc_list = ["!", ",", ".", "-",]
    new_list = []
    review_score = 0.0
    review_num = 0
    
    lower_movie_review = movie_review.lower()
    split_movie_review = lower_movie_review.split()

    for element in split_movie_review:
        if "!" not in element:
            new_list.append(element)
        if "," not in element:
            new_list.append(element)
        if "." not in element:
            new_list.append(element)
        if "-" not in element:
            new_list.append(element)
    # no_exclam = lower_movie_review.replace("!", "")
    # no_comma = no_exclam.replace(",", "")
    # no_period = no_comma.replace(".", "")
    # no_dash = no_period.replace("-", "")

    # non_punc_review = no_dash.split()
    

    for element in new_list:
        review_score += average_review(element, review_filename)
        review_num += 1
    total_est_review_score = (review_score / review_num)

    return total_est_review_score     # replace this with returning the estimated review


def estimate_user_review():
    """
    Asks user to enter a movie review, then the name of a file with existing
    movie reviews.
    It then calculates the estimated rating of the review they entered, along
    with a description of that rating (e.g. "neutral" or "slightly positive").
    """
    movie_review = input("Enter a movie review: ")
    review_filename = input("Enter a review file name: ")  
    
    score = estimate_review_score(movie_review, review_filename)
    round_score = round(score)
    if round_score <= 0:
        review = "negative"
    elif round_score == 1:
        review = "somewhat negative"
    elif round_score == 2:
        review = "neutral"
    elif round_score == 3:
        review = "somewhat positive"
    else:
        review = "positive"
    print("Estimated score: " + str(score) + " (" + review + ")")


# Do not modify anything after this point.
if __name__ == "__main__":
    estimate_user_review()
