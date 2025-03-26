for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        # faccio prima il fizzbuzz perche' se metto prima il fizz o il buzz non entra mai nella condizione dove i e' multiplo di 3 e 5
        print(f"{i} -> FizzBuzz")
    elif i % 3 == 0:
        print(f"{i} -> Fizz")
    elif i % 5 == 0:
        print(f"{i} -> Buzz")
    else:
        print(i)