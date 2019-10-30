#创建新字符串替换空格为%20
class Solution:
	#遍历字符串，
	def replaceSpace(self, s):
		if s == None:
			return None
		result = ''
		for i in range(len(s)):
			if i != ' ':
				result += s[i]
			else:
				result += %20
		s = result
		return s

#replace方法 s.replace(' ','%20')