class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        n = len(speed)

        if n == 1:
            return 1

        position_sorted_array = [
            (position[i], speed[i]) for i in range(n)
        ]


        position_sorted_array.sort(reverse=True)

        fleet = 1


        prev_time = (target - position_sorted_array[0][0]) / position_sorted_array[0][1]

        for i in range(1, n):

            current_time = (
                target - position_sorted_array[i][0]
            ) / position_sorted_array[i][1]

            if current_time > prev_time:
                fleet += 1
                prev_time = current_time

        return fleet