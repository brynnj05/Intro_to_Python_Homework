"""
Based on information about the user's lifestyle, this program will recommend what type of cat 
they should adopt.
"""

def cat_recommendation(hours_away, wants_kitten, has_other_pets):
    """
    Desired behavior:

    If hours_away is outside the range (0, 24), print a statement that tells the user that the number of 
    hours is not valid.
    If the user wants a kitten and is away from home for 8 or less hours a day, recommend a kitten.
    Otherwise, recommend an adult.
    If the user is away from home for 8 or more hours a day and does not have other pets, 
    recommend an independent cat.
    If the user has other pets, recommend a social cat.
    Otherwise, recommend a calm cat.

    Inputs:
        hours_away: Numeric value (integer/float) indicating how many hours per day the user is away from home
        wants_kitten: Boolean indicating whether the user wants a kitten
        has_other_pets: Boolean indicating whether the user has other pets

    Outputs:
        Statement recommending an age (kitten or adult) and personality (independent, social, or calm) for the cat.
    """

    # Answer Key 

    if hours_away < 0 or hours_away > 24:
        print("That number of hours is not valid!")
        return

    if wants_kitten and hours_away <= 8:
        print("You should adopt a kitten!")
    else:
        print("You should adopt an adult cat!")

    if hours_away >= 8 and not has_other_pets:
        print("You should adopt an independent cat!")
    elif has_other_pets:
        print("You should adopt a social cat!")
    else:
        print("You should adopt a calm cat!")

testing_function_1 = cat_recommendation(4, False, True)