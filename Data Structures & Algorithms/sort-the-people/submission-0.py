class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        tuple_list = []
        for i in range(len(heights)):
            tuple_list.append((names[i], heights[i]))
        # print(tuple_list)
        tuple_list.sort(key= lambda x: x[1], reverse= True)
        res = [item[0] for item in tuple_list]
        return res