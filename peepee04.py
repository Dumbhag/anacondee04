#Function 4 : Have Parameter/Have Return ****
def funcA( n1, n2) :
    print(f'N1 is {n1}')
    print(f'N2 is {n2}')
    return n1 + n2

def funcB( name, yeet ) :
    return f'hi {name}' ,2053 - yeet

print(f"Sum is {funcA(10,20)}")

x ,y = funcB("Nigga", 2000)
print(f'{x} อายุ {y} ปี')