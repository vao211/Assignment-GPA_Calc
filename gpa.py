#Tên
name = str(input('Tên của bạn là: '))
#Nhập y/n để bắt đầu/kết thúc chương trình
while True:
    
    bat_dau = str(input('Bắt đầu chương trình? (y/n): '))
    if bat_dau != 'y' and bat_dau != 'n':
        print('Vui lòng nhập y hoặc n ')
        break
    elif bat_dau == 'n':
        print('Đã kết thúc chương trình! ')
        break
    else:
        print('')
    #Vòng lặp khi nhập sai giá trị
    while True:
        try:
            #list điểm và tín
            list_diem=[]
            list_tin=[]
            so_luong_mon = int(input('Nhập số lượng môn: '))
            for i in range (so_luong_mon):
                diem_mon = float(input(f'Nhập điểm của môn thứ {i+1}: '))
                so_tin = int(input(f'Nhập số tín của môn {i+1}: '))
                if so_tin == 0:
                    break
                list_diem.append(diem_mon)
                list_tin.append(so_tin)
            if so_luong_mon > 0 and so_tin > 0 :
                break
            elif so_luong_mon <= 0 :
                print('Số lượng môn phải lớn hơn 0!')
            elif so_tin <= 0 :
                print('Số tín phải lớn hơn 0!')
        #ValueError sẽ phải nhập lại giá trị.
        except ValueError:
            print('Số lượng môn và số tín phải là số tự nhiên!')
            print()
            break#không thực hiện nhập lại giá trị mà sẽ hỏi lại có muốn bắt đầu ctrinh
    #try except tránh lỗi khi break ở trên
    try:
        #tính tổng điểm các môn
        tong_diem_cac_mon = 0
        for i in range(so_luong_mon):
            tong_diem_cac_mon += list_diem[i]*list_tin[i]
        #hàm tính toán
        def tinh_gpa():
            gpa=tong_diem_cac_mon/sum(list_tin)
            return gpa
        print(f'Điểm gpa của bạn là {tinh_gpa()}')
        break#có kq rồi sẽ không chạy lại chương trình
    except:
        pass#không làm gì
