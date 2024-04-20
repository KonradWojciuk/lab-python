# a) Iteracyjnie:

def draw_triangle_itereatively(n):
    for i in range(1, n + 1):
        print(i * "*")

# b) Rekurencyjnie:
def draw_triangle_recursive(levels, current_level=1):
    if current_level <= levels:
        print('*' * current_level)
        draw_triangle_recursive(levels, current_level + 1)

def main():
    levels = int(input("Podaj liczbę poziomów trójkąta dla iteracji: "))
    draw_triangle_itereatively(levels)
    levels = int(input("Podaj liczbę poziomów trójkąta dla rekurencji: "))
    draw_triangle_recursive(levels)

if __name__ == "__main__":
    main()