
def findPath():
   source = input('source: ')
   path = [source]
   dict = {'a': [('b', 8), ('d', 2), ('e', 1)], 'b': [('a', 2), ('c', 4)], 'c': [('b', 4), ('d', 6)]}
   pathList = dict[source]
   print('path list: ' + str(pathList))

   pathList.pop(0)
   pathList.sort(key=lambda x:x[1])
   mx = max(pathList[1:])
   print(mx)

   print('path: ' + str(path))

findPath()