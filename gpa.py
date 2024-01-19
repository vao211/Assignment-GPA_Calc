#Tên
name = str(input('Enter your name: '))
#Nhập y/n để bắt đầu/kết thúc chương trình
while True:
    start = str(input('Start the program? (y/n): '))
    if start != 'y' and start != 'n':
        print('Please enter y or n!')
        break
    elif start == 'n':
        print('The program has ended! ')
        break
    else:
        print('')
    #Vòng lặp khi nhập sai giá trị
    while True:
        try:
            #list điểm và tín
            list_point=[]
            list_credit=[]
            num_subject = int(input('Enter the number of subjects: '))
            for i in range (num_subject):
                point = float(input(f'Enter the score of the {i+1} subject: '))
                num_credit = int(input(f'Enter the number of credits of the {i+1} subject: '))
                if num_credit == 0:
                    break
                list_point.append(point)
                list_credit.append(num_credit)
            if num_subject > 0 and num_credit > 0 :
                break
            elif num_subject <= 0 :
                print('The number of subjects must be greater than 0!')
            elif num_credit <= 0 :
                print('The number of credits must be greater than 0!')
        #ValueError sẽ phải nhập lại giá trị.
        except ValueError:
            print('The number of subjects and credits must be natural numbers!')
            print()
            break#không thực hiện nhập lại giá trị mà sẽ hỏi lại có muốn bắt đầu ctrinh
    #try except tránh lỗi khi break ở trên
    try:
        #tính tổng điểm các môn
        total_point_subject = 0
        for i in range(num_subject):
            total_point_subject += list_point[i]*list_credit[i]
        #hàm tính toán
        def calc_gpa():
            gpa=total_point_subject/sum(list_credit)
            print(f'Your GPA is: {gpa}')
            return gpa
        GPA=float((calc_gpa()))
        #lưu kq vào list result
        result=[f'name: {name}',f'Point {tuple(list_point)}',f'Credits {tuple(list_credit)}',f'Gpa:{format(GPA,".3f")}']
        #truyền vào text
        import os
        #tạo thư mục
        os.makedirs("C:/Result_GPA", exist_ok=True)
        #tạo và ghi file
        with open(os.path.join("C:/Result_GPA", "result.txt"), mode='w') as f:
            f.write(f'{result}')
        break#có kq rồi sẽ không chạy lại chương trình
    except:
        pass#không làm gì
