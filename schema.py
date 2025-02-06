from pydantic import BaseModel
from typing import List

class ClassifierResponse(BaseModel):
    number: int = 1
    is_prime: bool = True
    is_perfect: bool = True
    properties: List[str] = ["1", "1"]
    digit_sum: int = 1
    fun_fact: str = "1"