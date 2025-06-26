class Solution(object):
    def distributeCandies(self, candies, num_people):
        # Create a list of zeros, one for each person
        result = [0] * num_people

        # Start giving from 1 candy
        give = 1
        i = 0  # step counter

        while candies > 0:
            # Current person index using modulo
            person_index = i % num_people

            # How many candies we can actually give
            current_give = min(give, candies)

            # Add candies to the person's total
            result[person_index] = result[person_index] + current_give

            # Subtract from total candies
            candies = candies - current_give

            # Prepare for next round
            give = give + 1
            i = i + 1

        return result
