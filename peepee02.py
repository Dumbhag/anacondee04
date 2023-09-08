#Function 2 : Have Parameter/No return 
#parameter คือ ตัวแปรประเภทหนึ่ง

def funcA( x , y ) :
    print('Mi...')
    z = x + y 
    print(f'{x} + {y} = {z}')
    #ไม่มีคำสั่ง return
def funcB( x ) :
    print(f"X is {x} 555...")
funcA(10,20) #Argument อากิเมนต์ (ข้อมูลที่ส่งให้parameter)
funcA(5,5)
funcB("UwU")