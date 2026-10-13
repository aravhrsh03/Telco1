# 9. Valid Parentheses

parans = input()

stack = []

back = ['}', ')', ']']

for cur in parans:
    if not stack and (cur in back):
        print (False)
    if cur == '}' and stack[-1] == '{':
        stack.pop()
    elif cur == ')' and stack[-1] == '(':
        stack.pop()
    elif cur == ']' and stack[-1] == '[':
        stack.pop()
    else:
        stack.append(cur)

print(stack)
print(not stack)