


class Test_Python():

    def test_fibo(self, limit):
        var1 = 0
        var2 = 1
        print(var1)
        print(var2)

        while var1 < limit:
            var = var1+var2
            print(var)
            var1 = var2
            var2 = var




    def test_01(self):
        self.test_fibo(100000)



   #
   #
   # def test_f(limit):  # генератор (а не функция, т.к. оператор return заменён на yield)
   #     var_1, var_2 = 0, 1
   #     while var_1 < limit:
   #          yield var_1  # return a, + запоминаем место рестарта для следующего вызова
   #          var_1= var_2
   #          var_2 = var_1 + var_2
   #
   #     for n in test_f(1000):  # используем генератор fibonacci() как итератор
   #          print(n)  # печатаем все числа Фибоначчи меньшие 1000 через пробел







