from django import template

register = template.Library()

def check_num(number, delit):
    if number % delit == 0:
        return number
    else:
        return

register.filter('check_num', check_num)