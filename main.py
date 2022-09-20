#filling a number list with a line of actions
#insert index(int) number example- insert 0 1
#append number
#remove number
#sort
#reverse
#pop
if __name__ == '__main__':
    #n is the number of action lines to be performed
    N = int(input())
    #filling in the list of commands
    queries = [[j for j in input().split()] for i in range(N)]
    #numList is the integer list after the commands are performed
    numList = []
    while len(queries) != 0:
        action = queries[0][0]
        if action == 'print':
            print(numList)
            queries.pop(0)
        if action == 'insert':
            numList.insert(int(queries[0][1]), int(queries[0][2]))
            queries.pop(0)
        if action == 'append':
            numList.append(int(queries[0][1]))
            queries.pop(0)
        if action == 'remove':
            numList.remove(int(queries[0][1]))
            queries.pop(0)
        if action == 'sort':
            numList.sort()
            queries.pop(0)
        if action == 'pop':
            numList.pop()
            queries.pop(0)
        if action == 'reverse':
            numList.reverse()
            queries.pop(0)
