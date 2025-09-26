class Solution(object):
    def findDisappearedNumbers(self, nums):
        N = len(nums)  # получаем длину массива
        seen = [0] * (N + 1)  # создаем список из нулей длиной N+1
        for num in nums:  # проходим по всем числам в исходном массиве
            seen[num] = 1  # отмечаем присутствие числа в списке seen
        ans = []  # создаем пустой список для результата
        for i in range(1, N + 1):  # проверяем все числа от 1 до N
            if seen[i] == 0:  # если число не было отмечено
                ans.append(i)  # добавляем его в результат
        return ans  # возвращаем список пропущенных чисел
