#Task
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hand = set()
        for i in nums:
            if i in hand:
                return True
            hand.add(i)
        return False

# Разбор решения
Заходит массив в nums 
создаем переменнут hand с элементом set
запускаем цикл с массива nums 
в цикле прописываем условия если в i есть повторяющий элемент из hand тогда возврашаем True инаце в hand элементом add добовляем значение i 
если нет вопторяющего элемента в цикле тогда сразу возвращяем False
