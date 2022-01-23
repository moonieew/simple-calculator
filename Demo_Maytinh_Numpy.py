import numpy as np

print("Input first matrix")  
R1 = int(input("Enter the number of rows:"))
C1 = int(input("Enter the number of columns:"))

print("Enter the entries in a single line (separated by space): ")

# User input of entries in a 
# single line separated by space
entries1 = list(map(int, input().split()))  
A = np.array(entries1).reshape(R1, C1)

print("Input second matrix")  
R2 = int(input("Enter the number of rows:"))
C2 = int(input("Enter the number of columns:"))

entries2 = list(map(int, input().split()))  
B = np.array(entries2).reshape(R2, C2)
'''print("lua chon cac phuong thuc tinh toan:")
print("Cong 2 ma tran               - Press 1")
print("Tru 2 ma tran                - Press 2")
print("Nhan 2 ma tran               - Press 3")
print("Khoi tao ma tran chuyen vi   - Press 4")
print("Tinh dinh thuc ma tran vuong - Press 5")
print("Ma tran nghich dao           - Press 6")
print("Ma tran nhan voi mot so      - Press 7")
print("Thoat                        - Press 0")'''
choice= 100
while(choice!=0):
    print("lua chon cac phuong thuc tinh toan:")
    print("Cong 2 ma tran               - Press 1")
    print("Tru 2 ma tran                - Press 2")
    print("Nhan 2 ma tran               - Press 3")
    print("Khoi tao ma tran chuyen vi   - Press 4")
    print("Tinh dinh thuc ma tran vuong - Press 5")
    print("Ma tran nghich dao           - Press 6")
    print("Ma tran nhan voi mot so      - Press 7")
    print("Ma tran chia voi mot so      - Press 8")
    print("Hang cua ma tran             - Press 9")
    print("Luy thua ma tran             - Press 10")
    print("Thoat                        - Press 0")
    choice=int(input())
    if(choice == 1):
        print("Ket qua ma tran:\n",A+B)
    elif(choice ==2):
        print("Ket qua ma tran:\n",A-B)
    elif(choice ==3):
        print("Ket qua ma tran:\n",A@B)
    elif(choice ==4):
        print("Ket qua ma tran chuyen vi:\n",A.T)
    elif(choice == 5):
        print("Dinh thuc cua ma tran vuong la:\n",np.linalg.det(A))
    elif(choice == 6):
        print("Ma tran nghich dao:\n",np.linalg.inv(A))
    elif(choice == 7):
        num=int(input("Ma tran nhan voi mot so, nhap so vao:\n "))
        print(A*num)    
    elif(choice == 8):
        num=int(input("Ma tran chia voi mot so, nhap so vao:\n "))
        print(A/num)   
    elif(choice == 9):
        print("Hang cua ma tran la: ",np.linalg.matrix_rank(A))
    elif(choice == 10):
        num=int(input("Luy thua cua ma tran, nhap so vao: "))
        print(np.linalg.matrix_power(A, num))
    else:
        print("Tat may tinh")
