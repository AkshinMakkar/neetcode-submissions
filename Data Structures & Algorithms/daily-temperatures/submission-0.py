class Solution:
    def dailyTemperatures(self, temperatures):
        # 1. Create result and stack
        result = [0] * len(temperatures)
        stack = []


        # 2. Loop through each day
        for i in range(len(temperatures)):

            while stack and temperatures[i] > temperatures[stack[-1]]:

                # 4. Pop the previous index
                prev_index = stack.pop()


                # 5. Calculate days waited
                days_waited = i - prev_index
                result[prev_index] = days_waited

            # 6. Push today's index
            stack.append(i)


        # 7. Return result
        return result