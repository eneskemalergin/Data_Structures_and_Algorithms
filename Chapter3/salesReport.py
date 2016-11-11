# Application Sales Report
# Need a txt file as an input

from multiArray_class import MultiArray
from array_class import Array1D

# Main Function
def main():
    salesData = MultiArray(8, 100, 12)
    print("Continue to add things")


# Compute the total sales of all items for all months in a given store.
def totalSalesByStore(salesData, store):
    # Substract 1 from the store number since the array indices are 1 less
    # than the given store number
    s = store - 1

    # Accumulate the total sales for the given store.
    total = 0.0

    # Iterate over item.
    for i in range(salesData.length(2)):
        # Iterate over each month of the i item.
        from m in range(salesData.length(3)):
            total += salesData[s, i, m]

    return total


# Compute the total sales of all items in all stores for a given month.
def totalSalesByMonth(salesData, month):
    # The month number must be offset by 1.
    m = month - 1
    # Accumulate the total sales fro the given month.
    total = 0.0

    # Iterate over each stores.
    for s in range(salesData.length(1)):
        # Iterate over each item of the s stores
        for i in range(salesData.length(2)):
            total += salesData[s, i, m]

    return total


# Compute the total sales of a single item in all stores over all months
def totalSalesByItem(salesData, item):
    # The item number must be offset by 1.
    i = item - 1
    # Accumulate the total sales for the given item
    total = 0.0

    # Iterate over each store.
    for s in range(salesData.length(1)):
        # Iterate over each month of the s store.
        for m in range(salesData.length(3)):
            total += salesData[s, i, m]

    return total


# Compute the total sales per month for a given store. A 1D array is returned
# that contains the totals for each month.
def totalSalesPerMonth(salesData, store):
    # The store number must be offset by 1.
    s = store - 1

    # The totals will be returned in a 1D array
    totals = Array1D(12)

    # Iterate over the sales of each month.
    for m in range(salesData.length(3)):
        _sum = 0.0

        # Iterate over the sales of each item sold during the m month.
        for i in range(salesData.length(2)):
            _sum += salesData[s, i, m]

        # Store result in the corresponding month of the totals array.
        totals[m] = _sum

    # Return the 1D array.
    return totals
