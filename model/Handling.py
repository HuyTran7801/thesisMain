import time

class Handling:
    def __init__(self):
        pass
    
    def countdown(self, t): 
	
        while t: 
            mins, secs = divmod(t, 60) 
            timer = '{:02d}:{:02d}'.format(mins, secs) 
            print(timer, end="\r") 
            time.sleep(1) 
            t -= 1
        
        return "Times up"
    
    
    def split_2_mcqs(self, mcqs):
        lst_mcq = []
        nums= ['I.', 'II.']
        mp = dict()
        for i in nums:
            mp[i] = -1
        ids = []
        index = 0
        for i in range(len(nums)):
            ok1, ok2 = 0, 0
            add = 0
            for j in range(index, len(mcqs)):
                val, val2 = mcqs[j:j+2], mcqs[j:j+3]
                
                if val == nums[i]:
                    if mp[val] == -1:
                        mp[val] = j
                        ids.append(j)
                        ok1 = 1
                elif val2 == nums[i]:
                    if mp[val2] == -1:
                        mp[val2] = j
                        ids.append(j)
                        ok2 = 1
                        
                if ok1 == 1 or ok2 == 1:
                    if ok1 == 1:
                        add =2
                    elif ok2 == 1:
                        add = 3
                    break
                
            index = ids[len(ids)-1] + add
        ids.sort()
        print('ids final ', ids)
        for i in range(len(ids) - 1):
            lst_mcq.append(mcqs[ids[i]:ids[i + 1]])
        lst_mcq.append(mcqs[ids[len(ids) - 1]:])
        return lst_mcq
    
    
    def split_3_mcqs(self, mcqs):
        lst_mcq = []
        nums= ['I.', 'II.', 'III.']
        mp = dict()
        for i in nums:
            mp[i] = -1
        ids = []
        index = 0
        for i in range(len(nums)):
            ok1, ok2, ok3 = 0, 0, 0
            add = 0
            for j in range(index, len(mcqs)):
                val, val2, val3 = mcqs[j:j+2], mcqs[j:j+3], mcqs[j:j+4]
                
                if val == nums[i]:
                    if mp[val] == -1:
                        mp[val] = j
                        ids.append(j)
                        ok1 = 1
                elif val2 == nums[i]:
                    if mp[val2] == -1:
                        mp[val2] = j
                        ids.append(j)
                        ok2 = 1
                elif val3 == nums[i]:
                    if mp[val3] == -1:
                        mp[val3] = j
                        ids.append(j)
                        ok3 = 1
                        
                if ok1 == 1 or ok2 == 1 or ok3 == 1:
                    if ok1 == 1:
                        add =2
                    elif ok2 == 1:
                        add = 3
                    elif ok3 == 1:
                        add = 4
                    break
                
            index = ids[len(ids)-1] + add
        ids.sort()
        print('ids final ', ids)
        for i in range(len(ids) - 1):
            lst_mcq.append(mcqs[ids[i]:ids[i + 1]])
        lst_mcq.append(mcqs[ids[len(ids) - 1]:])
        return lst_mcq
    
    
    def split_4_mcqs(self, mcqs):
        lst_mcq = []
        nums= ['I.', 'II.', 'III.','IV.']
        mp = dict()
        for i in nums:
            mp[i] = -1
        ids = []
        index = 0
        for i in range(len(nums)):
            ok1, ok2, ok3 = 0, 0, 0
            add = 0
            for j in range(index, len(mcqs)):
                val, val2, val3 = mcqs[j:j+2], mcqs[j:j+3], mcqs[j:j+4]
                
                if val == nums[i]:
                    if mp[val] == -1:
                        mp[val] = j
                        ids.append(j)
                        ok1 = 1
                elif val2 == nums[i]:
                    if mp[val2] == -1:
                        mp[val2] = j
                        ids.append(j)
                        ok2 = 1
                elif val3 == nums[i]:
                    if mp[val3] == -1:
                        mp[val3] = j
                        ids.append(j)
                        ok3 = 1
                        
                if ok1 == 1 or ok2 == 1 or ok3 == 1:
                    if ok1 == 1:
                        add =2
                    elif ok2 == 1:
                        add = 3
                    elif ok3 == 1:
                        add = 4
                    break
                
            index = ids[len(ids)-1] + add
        ids.sort()
        print('ids final ', ids)
        for i in range(len(ids) - 1):
            lst_mcq.append(mcqs[ids[i]:ids[i + 1]])
        lst_mcq.append(mcqs[ids[len(ids) - 1]:])
        return lst_mcq
    
    def split_5_mcqs(self, mcqs):
        lst_mcq = []
        nums= ['I.', 'II.', 'III.','IV.', 'V.']
        mp = dict()
        for i in nums:
            mp[i] = -1
        ids = []
        index = 0
        for i in range(len(nums)):
            ok1, ok2, ok3 = 0, 0, 0
            add = 0
            for j in range(index, len(mcqs)):
                val, val2, val3 = mcqs[j:j+2], mcqs[j:j+3], mcqs[j:j+4]
                
                if val == nums[i]:
                    if mp[val] == -1:
                        mp[val] = j
                        ids.append(j)
                        ok1 = 1
                elif val2 == nums[i]:
                    if mp[val2] == -1:
                        mp[val2] = j
                        ids.append(j)
                        ok2 = 1
                elif val3 == nums[i]:
                    if mp[val3] == -1:
                        mp[val3] = j
                        ids.append(j)
                        ok3 = 1
                        
                if ok1 == 1 or ok2 == 1 or ok3 == 1:
                    if ok1 == 1:
                        add =2
                    elif ok2 == 1:
                        add = 3
                    elif ok3 == 1:
                        add = 4
                    break
                
            index = ids[len(ids)-1] + add
        ids.sort()
        print('ids final ', ids)
        for i in range(len(ids) - 1):
            lst_mcq.append(mcqs[ids[i]:ids[i + 1]])
        lst_mcq.append(mcqs[ids[len(ids) - 1]:])
        return lst_mcq
    
    
    def split_6_mcqs(self, mcqs):
        lst_mcq = []
        nums= ['I.', 'II.', 'III.','IV.', 'V.', 'VI.']
        mp = dict()
        for i in nums:
            mp[i] = -1
        ids = []
        index = 0
        for i in range(len(nums)):
            ok1, ok2, ok3 = 0, 0, 0
            add = 0
            for j in range(index, len(mcqs)):
                val, val2, val3 = mcqs[j:j+2], mcqs[j:j+3], mcqs[j:j+4]
                
                if val == nums[i]:
                    if mp[val] == -1:
                        mp[val] = j
                        ids.append(j)
                        ok1 = 1
                elif val2 == nums[i]:
                    if mp[val2] == -1:
                        mp[val2] = j
                        ids.append(j)
                        ok2 = 1
                elif val3 == nums[i]:
                    if mp[val3] == -1:
                        mp[val3] = j
                        ids.append(j)
                        ok3 = 1
                        
                if ok1 == 1 or ok2 == 1 or ok3 == 1:
                    if ok1 == 1:
                        add =2
                    elif ok2 == 1:
                        add = 3
                    elif ok3 == 1:
                        add = 4
                    break
                
            index = ids[len(ids)-1] + add
        ids.sort()
        print('ids final ', ids)
        for i in range(len(ids) - 1):
            lst_mcq.append(mcqs[ids[i]:ids[i + 1]])
        lst_mcq.append(mcqs[ids[len(ids) - 1]:])
        return lst_mcq
    
    def split_7_mcqs(self, mcqs):
        lst_mcq = []
        nums= ['I.', 'II.', 'III.','IV.', 'V.', 'VI.', 'VII.']
        mp = dict()
        for i in nums:
            mp[i] = -1
        ids = []
        index = 0
        for i in range(len(nums)):
            ok1, ok2, ok3 = 0, 0, 0
            add = 0
            for j in range(index, len(mcqs)):
                val, val2, val3 = mcqs[j:j+2], mcqs[j:j+3], mcqs[j:j+4]
                
                if val == nums[i]:
                    if mp[val] == -1:
                        mp[val] = j
                        ids.append(j)
                        ok1 = 1
                elif val2 == nums[i]:
                    if mp[val2] == -1:
                        mp[val2] = j
                        ids.append(j)
                        ok2 = 1
                elif val3 == nums[i]:
                    if mp[val3] == -1:
                        mp[val3] = j
                        ids.append(j)
                        ok3 = 1
                        
                if ok1 == 1 or ok2 == 1 or ok3 == 1:
                    if ok1 == 1:
                        add =2
                    elif ok2 == 1:
                        add = 3
                    elif ok3 == 1:
                        add = 4
                    break
                
            index = ids[len(ids)-1] + add
        ids.sort()
        print('ids final ', ids)
        for i in range(len(ids) - 1):
            lst_mcq.append(mcqs[ids[i]:ids[i + 1]])
        lst_mcq.append(mcqs[ids[len(ids) - 1]:])
        return lst_mcq
    
    def split_8_mcqs(self, mcqs):
        lst_mcq = []
        nums = ['I.', 'II.', 'III.', 'IV.', 'V.', 'VI.', 'VII.', 'VIII.']
        # arr = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]
        mp = dict()
        for i in nums:
            mp[i] = -1
        ids = []
        index = 0
        for i in range(len(nums)):
            ok1, ok2, ok3, ok4 = 0, 0, 0, 0
            add = 0
            for j in range(index, len(mcqs)):
                val, val2, val3, val4 = mcqs[j:j+2], mcqs[j:j+3], mcqs[j:j+4], mcqs[j:j+5]
                
                if val == nums[i]:
                    if mp[val] == -1:
                        mp[val] = j
                        ids.append(j)
                        ok1 = 1
                elif val2 == nums[i]:
                    if mp[val2] == -1:
                        mp[val2] = j
                        ids.append(j)
                        ok2 = 1
                elif val3 == nums[i]:
                    if mp[val3] == -1:
                        mp[val3] = j
                        ids.append(j)
                        ok3 = 1
                elif val4 == nums[i]:
                    if mp[val4] == -1:
                        mp[val4] = j
                        ids.append(j)
                        ok4 = 1
                if ok1 == 1 or ok2 == 1 or ok3 == 1 or ok4 == 1:
                    if ok1 == 1:
                        add =2
                    elif ok2 == 1:
                        add = 3
                    elif ok3 == 1:
                        add = 4
                    elif ok4 == 1:
                        add = 5
                    break
                
            index = ids[len(ids)-1] + add
        ids.sort()
        print('ids final ', ids)
        for i in range(len(ids) - 1):
            lst_mcq.append(mcqs[ids[i]:ids[i + 1]])
        lst_mcq.append(mcqs[ids[len(ids) - 1]:])
        return lst_mcq
    
    def split_9_mcqs(self, mcqs):
        lst_mcq = []
        nums = ['I.', 'II.', 'III.', 'IV.', 'V.', 'VI.', 'VII.', 'VIII.', 'IX.',]
        # arr = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]
        mp = dict()
        for i in nums:
            mp[i] = -1
        ids = []
        index = 0
        for i in range(len(nums)):
            ok1, ok2, ok3, ok4 = 0, 0, 0, 0
            add = 0
            for j in range(index, len(mcqs)):
                val, val2, val3, val4 = mcqs[j:j+2], mcqs[j:j+3], mcqs[j:j+4], mcqs[j:j+5]
                
                if val == nums[i]:
                    if mp[val] == -1:
                        mp[val] = j
                        ids.append(j)
                        ok1 = 1
                elif val2 == nums[i]:
                    if mp[val2] == -1:
                        mp[val2] = j
                        ids.append(j)
                        ok2 = 1
                elif val3 == nums[i]:
                    if mp[val3] == -1:
                        mp[val3] = j
                        ids.append(j)
                        ok3 = 1
                elif val4 == nums[i]:
                    if mp[val4] == -1:
                        mp[val4] = j
                        ids.append(j)
                        ok4 = 1
                if ok1 == 1 or ok2 == 1 or ok3 == 1 or ok4 == 1:
                    if ok1 == 1:
                        add =2
                    elif ok2 == 1:
                        add = 3
                    elif ok3 == 1:
                        add = 4
                    elif ok4 == 1:
                        add = 5
                    break
                
            index = ids[len(ids)-1] + add
        ids.sort()
        print('ids final ', ids)
        for i in range(len(ids) - 1):
            lst_mcq.append(mcqs[ids[i]:ids[i + 1]])
        lst_mcq.append(mcqs[ids[len(ids) - 1]:])
        return lst_mcq
    
    def split_10_mcqs(self, mcqs):
        lst_mcq = []
        nums = ['I.', 'II.', 'III.', 'IV.', 'V.', 'VI.', 'VII.', 'VIII.', 'IX.', 'X.']
        # arr = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]
        mp = dict()
        for i in nums:
            mp[i] = -1
        ids = []
        index = 0
        for i in range(len(nums)):
            ok1, ok2, ok3, ok4 = 0, 0, 0, 0
            add = 0
            for j in range(index, len(mcqs)):
                val, val2, val3, val4 = mcqs[j:j+2], mcqs[j:j+3], mcqs[j:j+4], mcqs[j:j+5]
                
                if val == nums[i]:
                    if mp[val] == -1:
                        mp[val] = j
                        ids.append(j)
                        ok1 = 1
                elif val2 == nums[i]:
                    if mp[val2] == -1:
                        mp[val2] = j
                        ids.append(j)
                        ok2 = 1
                elif val3 == nums[i]:
                    if mp[val3] == -1:
                        mp[val3] = j
                        ids.append(j)
                        ok3 = 1
                elif val4 == nums[i]:
                    if mp[val4] == -1:
                        mp[val4] = j
                        ids.append(j)
                        ok4 = 1
                if ok1 == 1 or ok2 == 1 or ok3 == 1 or ok4 == 1:
                    if ok1 == 1:
                        add =2
                    elif ok2 == 1:
                        add = 3
                    elif ok3 == 1:
                        add = 4
                    elif ok4 == 1:
                        add = 5
                    break
                
            index = ids[len(ids)-1] + add
        ids.sort()
        print('ids final ', ids)
        for i in range(len(ids) - 1):
            lst_mcq.append(mcqs[ids[i]:ids[i + 1]])
        lst_mcq.append(mcqs[ids[len(ids) - 1]:])
        return lst_mcq
        
    def split_11_mcqs(self, mcqs):
        lst_mcq = []
        nums = ['I.', 'II.', 'III.','IV.', 'V.', 'VI.', 'VII.', 'VIII.', 'IX.', 'X.', 'XI.']
        mp = dict()
        for i in nums:
            mp[i] = -1
        ids = []
        index = 0
        for i in range(len(nums)):
            ok1, ok2, ok3, ok4 = 0, 0, 0, 0
            add = 0
            for j in range(index, len(mcqs)):
                val, val2, val3, val4 = mcqs[j:j+2], mcqs[j:j+3], mcqs[j:j+4], mcqs[j:j+5]
                
                if val == nums[i]:
                    if mp[val] == -1:
                        mp[val] = j
                        ids.append(j)
                        ok1 = 1
                elif val2 == nums[i]:
                    if mp[val2] == -1:
                        mp[val2] = j
                        ids.append(j)
                        ok2 = 1
                elif val3 == nums[i]:
                    if mp[val3] == -1:
                        mp[val3] = j
                        ids.append(j)
                        ok3 = 1
                elif val4 == nums[i]:
                    if mp[val4] == -1:
                        mp[val4] = j
                        ids.append(j)
                        ok4 = 1
                if ok1 == 1 or ok2 == 1 or ok3 == 1 or ok4 == 1:
                    if ok1 == 1:
                        add =2
                    elif ok2 == 1:
                        add = 3
                    elif ok3 == 1:
                        add = 4
                    elif ok4 == 1:
                        add = 5
                    break
                
            index = ids[len(ids)-1] + add
        ids.sort()
        print('ids final ', ids)
        for i in range(len(ids) - 1):
            lst_mcq.append(mcqs[ids[i]:ids[i + 1]])
        lst_mcq.append(mcqs[ids[len(ids) - 1]:])
        return lst_mcq
    
    def split_12_mcqs(self, mcqs):
        lst_mcq = []
        nums = ['I.', 'II.', 'III.','IV.', 'V.', 'VI.', 'VII.', 'VIII.', 'IX.', 'X.', 'XI.', 'XII.']
        mp = dict()
        for i in nums:
            mp[i] = -1
        ids = []
        index = 0
        for i in range(len(nums)):
            ok1, ok2, ok3, ok4 = 0, 0, 0, 0
            add = 0
            for j in range(index, len(mcqs)):
                val, val2, val3, val4 = mcqs[j:j+2], mcqs[j:j+3], mcqs[j:j+4], mcqs[j:j+5]
                
                if val == nums[i]:
                    if mp[val] == -1:
                        mp[val] = j
                        ids.append(j)
                        ok1 = 1
                elif val2 == nums[i]:
                    if mp[val2] == -1:
                        mp[val2] = j
                        ids.append(j)
                        ok2 = 1
                elif val3 == nums[i]:
                    if mp[val3] == -1:
                        mp[val3] = j
                        ids.append(j)
                        ok3 = 1
                elif val4 == nums[i]:
                    if mp[val4] == -1:
                        mp[val4] = j
                        ids.append(j)
                        ok4 = 1
                if ok1 == 1 or ok2 == 1 or ok3 == 1 or ok4 == 1:
                    if ok1 == 1:
                        add =2
                    elif ok2 == 1:
                        add = 3
                    elif ok3 == 1:
                        add = 4
                    elif ok4 == 1:
                        add = 5
                    break
                
            index = ids[len(ids)-1] + add
        ids.sort()
        print('ids final ', ids)
        for i in range(len(ids) - 1):
            lst_mcq.append(mcqs[ids[i]:ids[i + 1]])
        lst_mcq.append(mcqs[ids[len(ids) - 1]:])
        return lst_mcq
    
    def split_13_mcqs(self, mcqs):
        lst_mcq = []
        nums = ['I.', 'II.', 'III.','IV.', 'V.', 'VI.', 'VII.', 'VIII.', 'IX.', 'X.', 'XI.', 'XII.', 'XIII.']
        mp = dict()
        for i in nums:
            mp[i] = -1
        ids = []
        index = 0
        for i in range(len(nums)):
            ok1, ok2, ok3, ok4 = 0, 0, 0, 0
            add = 0
            for j in range(index, len(mcqs)):
                val, val2, val3, val4 = mcqs[j:j+2], mcqs[j:j+3], mcqs[j:j+4], mcqs[j:j+5]
                
                if val == nums[i]:
                    if mp[val] == -1:
                        mp[val] = j
                        ids.append(j)
                        ok1 = 1
                elif val2 == nums[i]:
                    if mp[val2] == -1:
                        mp[val2] = j
                        ids.append(j)
                        ok2 = 1
                elif val3 == nums[i]:
                    if mp[val3] == -1:
                        mp[val3] = j
                        ids.append(j)
                        ok3 = 1
                elif val4 == nums[i]:
                    if mp[val4] == -1:
                        mp[val4] = j
                        ids.append(j)
                        ok4 = 1
                if ok1 == 1 or ok2 == 1 or ok3 == 1 or ok4 == 1:
                    if ok1 == 1:
                        add =2
                    elif ok2 == 1:
                        add = 3
                    elif ok3 == 1:
                        add = 4
                    elif ok4 == 1:
                        add = 5
                    break
                
            index = ids[len(ids)-1] + add
        ids.sort()
        print('ids final ', ids)
        for i in range(len(ids) - 1):
            lst_mcq.append(mcqs[ids[i]:ids[i + 1]])
        lst_mcq.append(mcqs[ids[len(ids) - 1]:])
        return lst_mcq
    
    def split_14_mcqs(self, mcqs):
        lst_mcq = []
        nums = ['I.', 'II.', 'III.','IV.', 'V.', 'VI.', 'VII.', 'VIII.', 'IX.', 'X.', 'XI.', 'XII.', 'XIII.', 'XIV.']
        mp = dict()
        for i in nums:
            mp[i] = -1
        ids = []
        index = 0
        for i in range(len(nums)):
            ok1, ok2, ok3, ok4 = 0, 0, 0, 0
            add = 0
            for j in range(index, len(mcqs)):
                val, val2, val3, val4 = mcqs[j:j+2], mcqs[j:j+3], mcqs[j:j+4], mcqs[j:j+5]
                
                if val == nums[i]:
                    if mp[val] == -1:
                        mp[val] = j
                        ids.append(j)
                        ok1 = 1
                elif val2 == nums[i]:
                    if mp[val2] == -1:
                        mp[val2] = j
                        ids.append(j)
                        ok2 = 1
                elif val3 == nums[i]:
                    if mp[val3] == -1:
                        mp[val3] = j
                        ids.append(j)
                        ok3 = 1
                elif val4 == nums[i]:
                    if mp[val4] == -1:
                        mp[val4] = j
                        ids.append(j)
                        ok4 = 1
                if ok1 == 1 or ok2 == 1 or ok3 == 1 or ok4 == 1:
                    if ok1 == 1:
                        add =2
                    elif ok2 == 1:
                        add = 3
                    elif ok3 == 1:
                        add = 4
                    elif ok4 == 1:
                        add = 5
                    break
                
            index = ids[len(ids)-1] + add
        ids.sort()
        print('ids final ', ids)
        for i in range(len(ids) - 1):
            lst_mcq.append(mcqs[ids[i]:ids[i + 1]])
        lst_mcq.append(mcqs[ids[len(ids) - 1]:])
        return lst_mcq
    
    def split_15_mcqs(self, mcqs):
        lst_mcq = []
        nums = ['I.', 'II.', 'III.','IV.', 'V.', 'VI.', 'VII.', 'VIII.', 'IX.', 'X.', 'XI.', 'XII.', 'XIII.', 'XIV.', 'XV.']
        mp = dict()
        for i in nums:
            mp[i] = -1
        ids = []
        index = 0
        for i in range(len(nums)):
            ok1, ok2, ok3, ok4 = 0, 0, 0, 0
            add = 0
            for j in range(index, len(mcqs)):
                val, val2, val3, val4 = mcqs[j:j+2], mcqs[j:j+3], mcqs[j:j+4], mcqs[j:j+5]
                
                if val == nums[i]:
                    if mp[val] == -1:
                        mp[val] = j
                        ids.append(j)
                        ok1 = 1
                elif val2 == nums[i]:
                    if mp[val2] == -1:
                        mp[val2] = j
                        ids.append(j)
                        ok2 = 1
                elif val3 == nums[i]:
                    if mp[val3] == -1:
                        mp[val3] = j
                        ids.append(j)
                        ok3 = 1
                elif val4 == nums[i]:
                    if mp[val4] == -1:
                        mp[val4] = j
                        ids.append(j)
                        ok4 = 1
                if ok1 == 1 or ok2 == 1 or ok3 == 1 or ok4 == 1:
                    if ok1 == 1:
                        add =2
                    elif ok2 == 1:
                        add = 3
                    elif ok3 == 1:
                        add = 4
                    elif ok4 == 1:
                        add = 5
                    break
                
            index = ids[len(ids)-1] + add
        ids.sort()
        print('ids final ', ids)
        for i in range(len(ids) - 1):
            lst_mcq.append(mcqs[ids[i]:ids[i + 1]])
        lst_mcq.append(mcqs[ids[len(ids) - 1]:])
        return lst_mcq
    
    def split_QA(self, mcqs):
        question = None
        answers = []
        
        labels= ['A)', 'B)', 'C)', 'D)']
        pos = dict()
        for i in labels:
            pos[i] = -1
        ids = []
        tail = -1
        for i in range(len(mcqs)):
            val = mcqs[i:i+2]
            if val in labels and pos[val] == -1:
                if val == 'A)':
                    tail = i
                pos[val] = i
        
        for k, v in pos.items():
            ids.append(v)
        # for i in ids:
            # print('id= ', i)
        
        question = mcqs[0:tail]    
        for i in range(len(ids) - 1):
            answer = mcqs[ids[i] + 3: ids[i + 1]]
            answers.append(answer)
            
        ids_ans = ids
            
        # print('question ', question)
        # print('answers ', answers)
        feedback_lst = []
        patterns = ['The correct answer is:', 'Explanation:']
        mp = dict()
        for i in patterns:
            mp[i] = -1
        ids = []
                    
        for i in range(len(mcqs)):
            string = mcqs[i:i + 22]
            # print('string 1: ', string)
            if string in patterns:
                if mp[string] == -1:
                    # print('go 1')
                    mp[string] = i
                    tail = i
                    ids.append(i)
        
        # print('IDS ', ids)
        answers.append(mcqs[ids_ans[len(ids_ans) - 1] + 3:tail])
                    
        for i in range(len(mcqs)):
            string = mcqs[i:i + 12]
            # print('string 2: ', string)
            if string in patterns:
                if mp[string] == -1:
                    # print('go 2')
                    mp[string] = i
                    ids.append(i)
        for i in range(len(ids) - 1):
            # print('subs ', mcqs[ids[i]: ids[i + 1]])
            feedback_lst.append(mcqs[ids[i]: ids[i + 1]])
        lst = ids[len(ids) - 1]
        # print('lst ', lst)
        # print(len(lst))
        # print('IDS ', ids)
        # print('subs ', mcqs[lst:])
        feedback_lst.append(mcqs[lst:])
        
        corrected_answer = None
        for i in range(tail, len(mcqs)):
            val = mcqs[i:i + 2]
            if val in labels and pos[val] != -1:
                corrected_answer = val
                break
        return question, answers, feedback_lst, corrected_answer
    
    
    def split_QA_fill_in_the_blank(self, fibqs):
        patterns = ['The correct answer is:', 'Explanation:']
        vis = dict()
        for i in patterns:
            vis[i] = -1
        tail = -1
        tail2 = -1
        ids = []
        for i in range(len(fibqs)):
            val=fibqs[i:i + 22]
            if val in patterns and vis[val] == -1:
                vis[val] = i
                tail = i
                ids.append(i)
                break
        for i in range(len(fibqs)):
            val = fibqs[i:i + 12]
            if val in patterns and vis[val] == -1:
                vis[val] = i
                tail2 = i
                ids.append(i)
                break
        question = fibqs[:tail]
        feedback_lst = []
        for i in range(len(ids)-1):
            feedback_lst.append(fibqs[ids[i]: ids[i + 1]])
        feedback_lst.append(fibqs[ids[len(ids)-1]:])
        corrected_answer = fibqs[tail+22:tail2]
        return question, feedback_lst, corrected_answer
    
    def split_explanation(self, explanation):
        feedback_lst = []
        patterns = ['The correct answer is:', 'Explanation:']
        mp = dict()
        for i in patterns:
            mp[i] = -1
        ids = []
                    
        for i in range(len(explanation)):
            string = explanation[i:i + 22]
            if string in patterns:
                if mp[string] == -1:
                    mp[string] = i
                    ids.append(i)
                    
        for i in range(len(explanation)):
            string = explanation[i:i + 12]
            if string in patterns:
                if mp[string] == -1:
                    mp[string] = i
                    ids.append(i)
                    
        for i in range(len(ids) - 1):
            feedback_lst.append(explanation[ids[i]: ids[i + 1]])
        lst = ids[len(ids) - 1]
        # print('lst ', lst)
        # print(len(lst))
        # print('IDS ', ids)
        # print('subs ', mcqs[lst:])
        feedback_lst.append(explanation[lst:])
        return feedback_lst
    
    def split_question_label(self, mcqs):
        patterns = ['A)', 'B)', 'C)', 'D)']
        ids = []
        mp = dict()
        for i in patterns:
            mp[i] = -1
        tail = -1
        for i in range(len(mcqs)):
            val = mcqs[i:i + 2]
            if val in patterns:
                if mp[val] == -1:
                    tail = i
                    mp[val] = i
                    ids.append(i)
                    
        question = mcqs[:tail]
        print(ids)
        
        answers= []
        for i in range(len(ids)):
            answers.append(mcqs[ids[i] + 3:ids[i + 1]])
        answers.append(mcqs[ids[len(ids)-1] + 3:])
        
        return question,answers