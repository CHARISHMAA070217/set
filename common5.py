'''
def common_member(a, b):
    a_set = set(a)
    b_set = set(b)
 
    if (a_set & b_set):
        print(a_set & b_set)
    else:
        print("No common elements") 
a = [1,2,3,4]
b = [2,4,6,8]
common_member(a, b)
  
a = [1,2,3,4]
b = [2,4,6,8]
common_member(a, b)
Output: 
{2,4}
No common elements
'''
