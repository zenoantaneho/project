start_distance = int(input('Введите значение а: '))
goal_distance = int(input('Введите значение b: '))
print("Спортсмен занимается ежедневными пробежками. В первый день его результат составил", start_distance, "километров. Каждый день спортсмен увеличивал результат на 10% относительно предыдущего")
day = 1
while goal_distance > start_distance:
    start_distance *= 1.1
    day += 1

print("На", day, "день спортсмен достиг результата — не менее", goal_distance, "км")