from scipy.stats import pearsonr
import numpy as np
from utils.book_list import book_list

def get_user_ratings(user):
    print(f"\n{user}, rate the following books on a scale of 1-5 (1: Did not like, 5: Loved it).")
    print("If you haven't read a book, simply press Enter to skip it.")
    ratings = []
    for book in book_list:
        while True:
            rating_input = input(f"{book}: ")
            if not rating_input:
                ratings.append(np.nan)
                break
            try:
                rating = int(rating_input)
                if 1 <= rating <= 5:
                    ratings.append(rating)
                    break
                else:
                    print("Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a number or press Enter to skip.")
    return ratings

user1_ratings = get_user_ratings("Person 1")
user2_ratings = get_user_ratings("Person 2")

paired_ratings = [(u1, u2) for u1, u2 in zip(user1_ratings, user2_ratings) if not (np.isnan(u1) or np.isnan(u2))]

print("\n** Results **")

if len(paired_ratings) < 2:
    print("\nNot enough data to calculate a meaningful correlation.")
else:
    user1_paired, user2_paired = zip(*paired_ratings)
    if np.var(user1_paired) == 0 or np.var(user2_paired) == 0:
        print("\nNot enough variance in the ratings to calculate a meaningful correlation.")
    else:
        correlation, _ = pearsonr(user1_paired, user2_paired)
        print(f"\nThe Pearson correlation coefficient (r) between your book preferences is: {correlation:.2f}")
        if correlation > 0.5:
            print("You have very similar book preferences!\n")
        elif correlation > 0:
            print("Your book preferences are kinda similar!\n")
        elif correlation == 0:
            print("Sorry, there's no correlation between these book preferences.\n")
        else:
            print("You like different books.\n")
