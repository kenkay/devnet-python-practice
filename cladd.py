while True:
    class calc():
        def initCalc():
            mathfx = input ('Please use "d" for divide or "a" for addition: ')
            return mathfx

    pick = calc.initCalc()

    if pick == 'a':
        def sum():
                try:
                    x = int(input("First number "))
                    y = int(input("Second number "))
                except ValueError:
                    print ("Please use numbers only")
                else:
                    z = x + y
                    print (z)
                    print ("==========================")
        sum()


    if pick == 'd':
        def div():
            try:
                x = int(input("First number "))
                y = int(input("Second number "))
            except ValueError:
                print ("Please use numbers only")
            else:
                z = x / y
                print (z)
                print ("==========================")
        div()