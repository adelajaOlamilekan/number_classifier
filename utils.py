import math
import requests
import constants
from fastapi import status, HTTPException

def check_prime(number:int):
    sqrt_number = math.floor(math.sqrt(number))
    for i in range(2, sqrt_number):
        if not number%i:
            return False
    return True

def check_perfect(number:int):
    num_sum = 0

    for i in range(1, number):
        if not number%i:
            num_sum+=i
    
    return num_sum == number

def check_odd(number:int):
    return bool(number % 2)


def split_number(number):
    digits = []

    while number:
        digit = number % 10
        number //= 10
        digits.append(digit)

    return digits

def check_armstrong(number:int):
    digits = split_number(number)
    digits_len = len(digits) 
    num_sum = 0

    for digit in digits:
        num_sum += digit**digits_len
    return num_sum == number

def digit_sum(number:int):
    digits = split_number(number)
    num_sum = 0

    for digit in digits:
        num_sum += digit 
    
    return num_sum

def fun_fact(number:int):
    endpoint = f"{constants.FUN_FACT_URL}/{number}"

    fact = requests.get(endpoint)

    if fact.status_code != status.HTTP_200_OK:
        return HTTPException(status_code=fact.status_code, detail=fact.text)
    
    return fact.text
