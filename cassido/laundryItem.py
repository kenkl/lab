#!/usr/bin/env python3
"""This week's (2025-08-18) question:
Write a generator function createLaundryItem() that returns an object representing a laundry item. This object should have a method nextCycle() which,
 when called, advances the item through a series of laundry cycles in order: 'soak', 'wash', 'rinse', 'spin', and 'dry'. After the final cycle, 
 subsequent calls to nextCycle() should return 'done'.
"""
def createLaundryItem(item = "item"):
    cycles = ['soak', 'wash', 'rinse', 'spin', 'dry']
    index = 0

    class LaundryItem:
        name = item
        def nextCycle(self):
            nonlocal index
            if index < len(cycles):
                cycle = cycles[index]
                index += 1
                return cycle
            else:
                return 'done'

    return LaundryItem()

def wash(item):
    while True:
        cycle = item.nextCycle()
        print(f"{item.name} is now in the '{cycle}' cycle.")
        if cycle == 'done':
            break

if __name__ == "__main__":
    towel = createLaundryItem("towel")
    socks = createLaundryItem("socks")
    knickers = createLaundryItem("knickers")
    
    wash(socks)
    wash(knickers)
    wash(towel)
