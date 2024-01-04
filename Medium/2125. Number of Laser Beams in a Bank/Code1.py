class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        return sum(a.count("1") * b.count("1") for a, b in pairwise(filter(lambda x: "1" in x, bank)))        
