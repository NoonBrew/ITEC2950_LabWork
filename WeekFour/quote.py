"""
Generate quotes for lawn mowing service.
Small lawn = $10 
Medium lawn = $15
Large lawn = $20

Add on $5 for same-day service

"""

def lawn_quote(size, same_day):
    if size == 'small':
        price = 10
    elif size == 'medium':
        price = 15
    elif size == 'large':
        price = 20
    else:
        return # can't calculate, return None
    
    if same_day:
        price += 5
    
    return price