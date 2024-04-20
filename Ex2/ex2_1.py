def main():
    products = input("Wprowadź produkty oddzielone przecinkiem: ")

    product_list = products.split(",")
    
    cash_register = {}

    for product in product_list:
        product = product.strip().lower()

        price = float(input(f"Podaj cenę produktu {product}: "))

        cash_register[product] = price

    for product, price in cash_register.items():
        print(f"{product}: {price:.2f} zł")

if __name__ == "__main__":
    main()