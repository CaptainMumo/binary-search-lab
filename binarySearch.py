class searchObject:
    def __init__(self, count, index):
        self.count = count
        self.index = index

    def __getitem__(self, key):
        if key == 'count':
            return self.count
        else:
            return self.index

class binarySearch:

    def __init__(self, length, step):
        self.binarySearch = [x for x in range(step,(length*step)+1,step)]
        self.length = len(self.binarySearch)

    def __str__(self):
        return str(self.binarySearch)

    def __getitem__(self, key):
        return self.binarySearch[key]
    
    def search(self, number):
        
        first = 0
        index = -1
        last = len(self.binarySearch)-1
        found = False
        
        while( first<=last and not found):
            count = 0
            midpoint = (first + last)//2
            if self[midpoint] == number:
                found = True
                index = list(self).index(number)
                #break
            else:
                if number < self[midpoint]:
                    last = midpoint - 1
                else:
                    first = midpoint + 1
            count = count + 1
        return searchObject(count, index)
        

if __name__=="__main__":
    one_to_twenty = binarySearch(20, 1)
    two_to_forty = binarySearch(20, 2)
    print(two_to_forty.search(4).__dict__)
