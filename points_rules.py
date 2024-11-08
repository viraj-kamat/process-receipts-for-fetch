import math

def points_for_alphanumeric(retailer):
    """
    Returns points for alphanumeric characters in the retailer name.
    
    :param retailer: The name of the retailer
    :type retailer: str
    :return: The points awarded for alphanumeric characters in the retailer name
    :rtype: int
    """
    points = 0
    for char in retailer:
        if char.isalnum():
            points += 1
    return points

def points_if_whole_number(total):
    """
    Returns points if the receipt total is a whole number.
    
    :param total: The total of the receipt
    :type total: float
    :return: The points awarded if the total is a whole number
    :rtype: int
    """

    points = 0
    total = round(total,2)
    if total%1 == 0:
        points += 50  
    return points

def points_if_multiple_of_pointtwofive(total):
    """
    Returns points if the receipt total is a multiple of 0.25.
    
    :param total: The total of the receipt
    :type total: float
    :return: The points awarded if the total is a multiple of 0.25
    :rtype: int
    """

    points = 0
    total = round(total,2)
    if total%0.25 == 0:
        points += 25
    return points
def points_for_every_two_items(items):
    points = 0
    total_items = len(items)
    points += 5 * (total_items // 2) 
    return points

def points_based_on_name_of_items(item_name, item_price):
    """
    Returns points based on the length of the item name and the price of the item.
    
    :param item_name: The name of the item
    :type item_name: str
    :param item_price: The price of the item
    :type item_price: float
    :return: The points awarded based on the length of the item name and the price of the item
    :rtype: int
    """
    points = 0
    item_name = item_name.strip()
    if len(item_name)%3 == 0:
        points += math.ceil(item_price*0.2)
    return points

def points_based_on_date(purchase_date):
    """
    Returns points based on the date of the purchase.
    
    :param purchase_date: The date of the purchase
    :type purchase_date: str
    :return: The points awarded based on the date of the purchase
    :rtype: int
    """
    points = 0
    purchase_day = int(purchase_date.split("-")[2])
    if purchase_day%2 == 1:
        points += 6
    return points

def points_based_on_time(purchase_time):
    """
    Returns points based on the time of the purchase.
    
    :param purchase_time: The time of the purchase
    :type purchase_time: str
    :return: The points awarded based on the time of the purchase
    :rtype: int
    """
    points = 0
    purchase_hour = int(purchase_time.split(":")[0])
    if 14 <= purchase_hour <= 16:
        points += 10
    return points
