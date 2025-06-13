from kmp import kmp_search
from boyer_moore import boyer_moore_search
from rabin_karp import rabin_karp_search
import timeit

_TIMES_ = 100

def read_article(file_name: str) -> str:
    with open(f"task_3/{file_name}", "r", encoding="utf-8") as file:
        return file.read()


searchrs = ("kmp_search", "boyer_moore_search", "rabin_karp_search")
articles = (read_article("стаття_1.txt"), read_article("стаття_2.txt"))
patterns = (
    "Пошук стрибками, цей алгоритм від двійкового пошуку відрізняється рухом виключно вперед. Такий пошук вимагає відсортованої колекції. Стрибаючи вперед на інтервал sqrt (arraylength), досягаючи елемента більшого, ніж поточний елемент або кінця масиву. При кожному стрибку записується попередній крок. Стрибки припиняються, коли знайдений елемент більше шуканого. Потім запускаємо лінійний пошук між попереднім і поточним кроками. Це зменшує поле пошуку та робить лінійний пошук життєздатним варіантом [5].",
    "У таблиці 1 наведено результати серії експериментів, проведених для порівняння часу формування рекомендацій системою при використанні різних структур даних для реалізації бази даних.",
)

print("Час роботи алгоритмів коли фрагмент існує в тексті:")
print(f"{'Алгоритм':<22}{'Стаття 1':<11}{'Стаття 2':<11}")
for search in searchrs:
    print(f"{search:<20}|", end=" ")
    for i in range(2):
        time =timeit.timeit(f"{search}(articles[{i}],patterns[{i}])", number=_TIMES_, globals=globals())/_TIMES_
        print(f"{time:.6f}", end=" | ")
    print()

print("Час роботи алгоритмів коли фрагмент не існує в тексті:")
print(f"{'Алгоритм':<22}{'Стаття 1':<11}{'Стаття 2':<11}")
for search in searchrs:
    print(f"{search:<20}|", end=" ")
    for i in range(2):
        time =timeit.timeit(f"{search}(articles[{i}],patterns[{1-i}])", number=_TIMES_, globals=globals())/_TIMES_
        print(f"{time:.6f}", end=" | ")
    print()
