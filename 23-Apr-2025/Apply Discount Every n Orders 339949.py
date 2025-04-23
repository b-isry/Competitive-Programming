# Problem: Apply Discount Every n Orders - https://leetcode.com/problems/apply-discount-every-n-orders/description/

class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.mp = defaultdict(int)
        for i in range(len(products)):
            self.mp[products[i]] = prices[i]
        self.cnt = 0
        
    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.cnt += 1
        bill = 0
        for i in range(len(product)):
            bill += self.mp[product[i]] * amount[i]
        if (self.cnt % self.n == 0):
            discnt = (self.discount/100) * bill
            bill -= discnt
        return bill



# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)