# Last updated: 8/11/2026, 6:35:22 PM
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_cuisines = {}
        self.food_ratings = {}
        self.cuisines_food = {}
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_cuisines[food] = cuisine
            self.food_ratings[food] = rating
            if cuisine not in self.cuisines_food:
                self.cuisines_food[cuisine] = []
            heapq.heappush(self.cuisines_food[cuisine], (-rating, food))


    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.food_cuisines[food]
        self.food_ratings[food] = newRating
        heapq.heappush(self.cuisines_food[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisines_food[cuisine]
        while heap:
            rating, food = heap[0]
            if -rating == self.food_ratings[food]:
                return food
            heapq.heappop(heap)


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)