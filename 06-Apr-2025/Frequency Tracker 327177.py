# Problem: Frequency Tracker - https://leetcode.com/problems/frequency-tracker/description/

class FrequencyTracker:

    def __init__(self):
        self.freq = defaultdict(int)  
        self.occ = defaultdict(int)  

    def add(self, number: int) -> None:
        self.freq[number] += 1
        self.occ[self.freq[number]] += 1
        self.occ[self.freq[number]-1] -= 1 

    def deleteOne(self, number: int) -> None:
        if self.freq[number]:
            self.freq[number] -= 1
            if self.freq[number] == 0: 
                del self.freq[number]
            self.occ[self.freq[number]] += 1
            self.occ[self.freq[number]+1] -= 1 
    def hasFrequency(self, frequency: int) -> bool:
        return self.occ[frequency] > 0

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)