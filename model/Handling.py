class Handling:
    def __init__(self):
        pass
    
    def split_mcqs(self, mcqs):
        lst_mcq = []
        nums=['1.', '2.', '3.', '4.', '5.']
        mp = dict()
        for i in range(len(mcqs)):
            val = mcqs[i:i+2]
            if val in nums:
                mp[val] = i
        # for k,v in mp.items():
        #     print(k, ' - ', v)
        for i in range(len(nums)-1):
            start = mp[nums[i]]
            end = mp[nums[i + 1]]
            lst_mcq.append(mcqs[start:end])
        lst = mp[nums[len(nums) - 1]]
        lst_mcq.append(mcqs[lst:])
        return lst_mcq