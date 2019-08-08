
# 1. Knapsack Problem - Using dynamic programming

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

    # Don't do anything with the item becasue it exceeds the capacity. Meaning that it can't be included.
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
# print(knapsack(50, items))



# 2. Minimum value path - Using dynamic programming
# Using recursion
def min_path_sum(grid, i, j):
    '''
    starts at 0,0
    ex. [[1,3,1],
        [1,5,1],
        [4,2,1]]
    should return a value of 7 from the shortest path: 1->3->1->1->1
    '''
    # means that we've hit the end!
    if i == len(grid) - 1 and j == len(grid) - 1:
        return grid[i][j]
    # means that we've hit the last row, and now we can only go to the right
    elif i == len(grid) - 1:
        return min_path_sum(grid, i, j + 1) + grid[i][j]
    # means that we've hit the last possible column, and now we can only go down
    elif j == len(grid) - 1:
        return min_path_sum(grid, i + 1, j) + grid[i][j]
    else:
        down = min_path_sum(grid,i + 1, j)
        right = min_path_sum(grid, i, j + 1)
        return min(down, right) + grid[i][j]

# print(min_path_sum([[1,3,1], [1,5,1], [4,2,1]], 0, 0))

# Using iteration
def min_path_sum(grid):
    '''
    variable:
        row - Int of the grid's count (this value never changes)
        column - Int of the grid at [0]'s count (this value never changes)
        memo - a grid of ints that keep track of the calculated values. Initially is the exact same grid with all values of 0
               ex. If input is [[1, 2],
                                [4, 8]]
                then the memo will initially look like [[0, 0],
                                                        [0, 0]]
    psuedocode:
        - since we're using an iterative approach, this means we're building a bottom up table
        - for loop through the rows, and also columns
        - these are some cases we would need to check:
            - if the row and column is a 0(starting off the first iteration); put the current value into our memoize grid of calculated values
            - if only the row is 0; calculate the new value by adding the current value in the grid with the memoized value in to the curr's left!
            - if only the column is 0; calculate the new value by adding the current value in the grid with the memoized value in to the curr's top!
            - else; meaning that it can be passed from the left side or either the top side. In this case, we're going to calculate the memoized value
                from the left and top, and choose the least ammount to add to the curr's value in the grid. And that will be the new memoized value!!
        - Once the for loops have been finished executing(we've hit the last rows and columns in the grid) we return the last item in the grid
          We can be sure that this will return the expected solution because we keep the memoized value moving from top left, all the way to bottom right of
          grid. So we return the value in the memo at index [last row][last column]. example if this was a 3x3 grid, we will return memo[2][2].
    '''
    # Initialize our row and column variables so we can iterate over (assuming that the grid is a square)
    row = len(grid)
    column = len(grid[0])
    memo = [[0] * len(grid) for _ in range(len(grid))]

    for i in range(row):
        for j in range(column):
            if i == 0 and j == 0:
                memo[i][j] = grid[i][j]
                continue # we wouldn't want to go through the other steps in the smallest for loop any more
            elif i == 0:
                # we can only go to the right since we're at the top row in the grid. And since we have already
                # calculated the values on the left side of current [i][j] grid, we can grab that and add it to the current [i][j]
                # in the grid. Now we will also need to update the memo grid with the number to the left
                memo[i][j] = grid[i][j] + memo[i][j-1]
            elif j == 0:
                # we can only go down the grid(rows can change) becasue we're in the last column.
                # upgrade the memo grid with our newly calculated value!!
                # the value we put into the memo = input grid at [i][j] add with the cached value right to the top of curr[i][j] in memo
                memo[i][j] = grid[i][j] + memo[i-1][j]
            else:
                # This means that we can either go down or right. We should calculate from both(saved from memo) and get the value which
                # is the least, so we can add that to the current [i][j] in the grid
                up = memo[i-1][j]
                left = memo[i][j-1]
                memo[i][j] = grid[i][j] + min(up, left)
    return memo[row-1][column-1]

print(min_path_sum([[1,3,1], [1,5,1], [4,2,1]]))
