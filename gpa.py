#lấy số lượng môn
num_subject=int(input('Nhập số lượng môn học: '))
try:
#tạo list điểm và tín
    try:
        all_point=[]
        all_num_credit=[]
        # Nhập dữ liệu
        for i in range(num_subject):
            try:
                point=float(input(f'Nhập điểm môn số {i+1}: '))
            except:
                print('Vui lòng nhập số thực khác 0')
            num_credit=int(input(f'Nhập số tín của môn thứ {i+1}: '))
            # Thêm dữ liệu từ bàn phím vào list
            all_point.append(point)
            all_num_credit.append(num_credit)
        #Tính tổng điểm của các môn: sum(điểm mỗi môn*số tín mỗi môn)
        #tạo list chứa tổng điểm total_point
        total_points=[]
        for i in range (num_subject):
                #tạo biến tt_points để gán giá trị (=Điểm của môn * số tín của môn)
            tt_points=all_point[i]*all_num_credit[i]
                #nhập giá trị từ tt_point vào list
            total_points.append(tt_points)
        #tính GPA:
        def gpa_calc():
            gpa=sum(total_points)/sum(all_num_credit)
            return gpa
        print('Điểm GPA của bạn là: ',gpa_calc())
    except:
        print('Vui lòng nhập số nguyên lớn hơn 0')
except:
    print('Vui lòng nhập số nguyên lớn hơn 0')



