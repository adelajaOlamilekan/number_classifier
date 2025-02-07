import utils
import schema
from fastapi import HTTPException, status

def classify_number(number):
    
    number = int(number)
    is_prime = utils.check_prime(number)
    is_perfect = utils.check_perfect(number)
    is_armstrong = utils.check_armstrong(number)
    is_odd = utils.check_odd(number)
    digit_sum = utils.digit_sum(number)
    fun_fact = utils.fun_fact(number)

    return serialize_response(number, is_prime, is_perfect, is_armstrong,is_odd, digit_sum, fun_fact)

def serialize_response(number, is_prime:bool, is_perfect:bool, is_armstrong:bool, 
                       is_odd:bool, digit_sum:int, fun_fact:str):
    return schema.ClassifierResponse(
        number = number,
        is_prime=is_prime,
        is_perfect=is_perfect,
        properties=number_properties(is_armstrong, is_odd),
        digit_sum=digit_sum,
        fun_fact=fun_fact
    )

def number_properties(is_armstrong:bool, is_odd:bool):
    properties = []

    if is_armstrong:
        properties.append("armstrong")

    if is_odd:
        properties.append("odd")
    else:
        properties.append("even")

    return properties
        