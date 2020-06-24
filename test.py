

def main():
	items = list(map(int, input().split()))
	size = len(items)
	
	overall, partition = {}, {}
	overall[size-1] = partition[size-1] = items[size-1]
	
	for i in range(size-2, -1, -1):
		partition[i] = max(items[i], partition[i+1] + itmes[i])
		overall[i] = max(partition[i], overall[i+1])
	print(overall[0])
	
	
def maxlcp(strs):
	if strs == None or len(strs)==0:
		return 0
		
	lens = len(strs)
	dp = [0 for _ in range(lens)]
	dp[0] = 1 if strs[0] == strs[lens-1] else 0
	
	for i in range(lens):
		pre = dp[0]
		dp[0] = max(dp[0], 1 if strs[i] == strs[lens-1] else 0)
		
		for j in range(1, lens):
			cur = dp[j]
			dp[j] = max(dp[j], dp[j-1])
			if strs[i] == strs[len-1-j]:
				dp[j] = max(dp[j], pre+1)
			pre = cur
	return dp[lens-1]

def maxlcp(strs):
	if strs==None or len(strs)==0:
		return 0
	lens = len(strs)
	dp =[0 for _ in range(lens)]
	dp[0] = 1 if strs[0] == strs[lens-1] else 0
	for i in range(lens):
		pre = dp[0]
		dp[0] = max(dp[0],1 if strs[i] == strs[lens-1] else 0)
		for j in range(1,lens):
			cur = dp[j]
			dp[j] = max(dp[j],dp[j-1])
			if strs[i] == strs[lens-1-j]:
				dp[j] = max(dp[j],pre+1)
			pre = cur
	return dp[lens-1]
	
def maxlcp(strs):
	
	rstrs = strs[::-1]
	
	lens = len(strs)
	maxlen = [[0 for _ in range(lens)] for _ in range(lens)]
	
	for i in range(1, lens):
		for j in range(1, lens):
			if strs[i-1] == rstrs[j-1]:
				maxlen[i][j] = maxlen[i-1][j-1] + 1
			else:
				maxlen[i][j] = max(maxlen[i-1][j], max_len[i][j-1])
	return maxlen[lens-1][lens-1]
	
	
class Solution(object):

	def LeftRotateString(self, s, n):
		# write code here
		n = n % len(s)
		
		return s[n:] + s[:n]

			
if __name__ == "__main__":
	ss = Solution()
	print(ss.LeftRotateString(s='abcXYZdef', n=20))