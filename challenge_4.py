
# Knapsack Problem - Using dynamic programming

class Item:
    def __init__(self, name, weight, val):
        self.name = name
        self.weight = weight
        self.val = val

def knapsack(C, items):
    ''' A  method to determine the maximum value of the items included in the knapsack
    without exceeding the capacity  C

        Parameters:
        C= 50
        items = (("boot", 10, 60),
             ("tent", 20, 100),
             ("water", 30, 120),
             ("first aid", 15, 70))
        Returns: max value
    '''
    # Base case where there are no items or if the maximum weight in the bag is 0
    if len(items) == 0 or C == 0:
        return (0, [])

    # Get access to the first item in list
    item = items[0]

    # Don't do anything with the item becasue it exceeds the capacity
    if item.weight > C:
        return knapsack(C, items[1:])
    else:
        # calculate the 2 sub probelems: kanpsack with the item in it, or either knapsack without the item
        val_with_item, knap_items = knapsack(C - item.weight, items[1:])
        val_with_item += item.val       # add the value of the item!
        val_without_item, knap__without_items = knapsack(C, items[1:])

        # if we want the knapsack with the item in it:
        if val_with_item > val_without_item:
            # append the specific item to our array and we can return the new value along with the list of items
            knap_items.append(item.name)
            return (val_with_item, knap_items)
        else:
            # return the tuple with the same value (because we didn't add an additional item to our list) and the list of items 
            return (val_without_item, knap__without_items)

items = [Item("boot", 10, 60),
        Item("tent", 20, 100),
        Item("water", 30, 120),
        Item("first aid", 15, 70)]
print(knapsack(50, items))
