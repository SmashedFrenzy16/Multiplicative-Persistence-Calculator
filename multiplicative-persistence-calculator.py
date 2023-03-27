n = int(input("Enter a number: "))


def m_p(x):

    persistence = 0

    product = 1

    while x > 9:

        x_string = str(x)

        for digit in range(0, len(x_string)):

            product = product * int(x_string[digit])

        print(product)

        persistence += 1

        x = product

        product = 1

    print(f"Persistence Of Number: {persistence}")
            


m_p(n)