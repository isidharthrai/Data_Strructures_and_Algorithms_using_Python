#LL - has a head node, tail node, and pointers.

#Appending at the end of list/tail is O(1), but popping elememt from tail is O(n).
#whereas adding a new head or poping it is O(1). 

#Adding or Removing element from middle of LL is O(n).

#Traversing/Lookup by value through list is O(n), but by index is O(1).

#example
head = {
        'val':11,
        next:{
            'val':22,
            next:{
                'val':33,
                next:{
                    'val':22,
                    next: None #tail
                    }
                }
            }
        }



