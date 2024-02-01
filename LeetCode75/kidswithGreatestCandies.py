class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Create a list of tuples with coupled index and candies
        coupled_candies = list(enumerate(candies))

        # # Sort the coupled_candies based on candies in descending order
        # coupled_candies.sort(key=lambda x: x[1], reverse=True)

        # Get the index of the kids with the greatest number of candies after extraCandies
        greatest_indices = [index for index, kid_candies in coupled_candies if kid_candies + extraCandies >= max(candies)]

        # Initialize the result list with False for all kids
        result = [False] * len(candies)

        # Set True for the kids with the greatest number of candies
        for index in greatest_indices:
            result[index] = True

        return result


