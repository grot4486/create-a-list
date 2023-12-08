import random
import time
import matplotlib.pyplot as plt

sizes = [] #сами списки
times = []


for size in range(1000, 101000, 1000): #1000-100000

start = time.time() #начало

r = [random.randint(1, 100) for _ in range(size)] #создание

end = time.time() #время окончания
c = end - start

sizes.append(size) # размер и время
times.append(c)


plt.figure(figsize=(10, 6)) # график
plt.plot(sizes, times, marker='o', linestyle='-')
plt.title('Зависимость времени создания списка от его размера')
plt.xlabel('Размер списка')
plt.ylabel('Время создания (сек)')
plt.grid(True)

plt.show() # показ
