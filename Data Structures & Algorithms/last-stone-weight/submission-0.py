class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        sortedStones = sorted(stones)
        while len(sortedStones) > 1:
            if sortedStones[-1] > sortedStones[-2]:
                val = sortedStones.pop() - sortedStones.pop()
                sortedStones.append(val)
                sortedStones.sort()
            elif sortedStones[-1] == sortedStones[-2]:
                sortedStones.pop()
                sortedStones.pop()
        return sortedStones[0] if sortedStones else 0