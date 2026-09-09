class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #output array stores temp diffs
        output = [0] * len(temperatures)
        #stack stores temps waiting for a higher temp
        stack = []
        for index, temp in enumerate(temperatures):
            #pops till temp not higher
            while stack and temperatures[stack[-1]] <temp:
                prev = stack.pop()
                output[prev] = index - prev
            stack.append(index)
        return output


        