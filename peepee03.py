#Function 3 : No Parameter/Have return ***
def funcA( ) :
    print('peepo')
    print('Ojo')
    return 'Pepsi Pepsi Pepsi'

def funcB( ) :
    return 999, True, 10 + 20
funcA( )
funcB( )
# funcA( ) เขียนได้ แต่เขาไม่ทำกัน
print( funcA( ))
x = funcA( )

a, b, c = funcB( ) #***ควรสร้างตัวแปรเพื่อมาเก็บค่า return
print(f'{a} {b} {c}')