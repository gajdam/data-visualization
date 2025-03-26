import matplotlib.pyplot as plt
import numpy as np

data = [
    ("Don Budge", 1915, 1932, 1955, 1938),
    ("Maureen Connolly", 1934, 1951, 1955, 1953),
    ("Rod Laver", 1938, 1962, 1976, 1962, 1969),
    ("Margaret Court", 1942, 1960, 1977, 1970),
    ("Steffi Graf", 1969, 1982, 1999, 1988)
]

plt.figure(figsize=(10, 6))

y_pos = np.arange(len(data))

for i, (name, birth, start, end, *gs) in enumerate(data):
    start_age = start - birth
    end_age = end - birth
    gs_ages = [g - birth for g in gs]

    plt.plot([start_age, end_age], [i, i], marker='o', label=name)
    for ga in gs_ages:
        plt.scatter(ga, i, color='red', zorder=3)

plt.yticks(y_pos, [name for name, *_ in data])
plt.xlabel("Wiek")
plt.ylabel("Zawodnik")
plt.title("Wiek tenisistów w momencie rozpoczęcia, zakończenia kariery i zdobycia Wielkiego Szlema")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
