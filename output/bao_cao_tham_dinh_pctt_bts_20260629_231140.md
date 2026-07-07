# Báo cáo thẩm định PCTT/UCTT trạm BTS

## 1. Kết luận tổng hợp

- Điểm tổng: **0**
- Kết luận: **KHONG_DAT**

## 2. Chi tiết phát hiện

### 1. Đủ trường dữ liệu tối thiểu
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/Tong hop_PA PTDS
- Loại bất thường: Thiếu trường dữ liệu
- Bằng chứng: Nhận diện được: {'staff': 'Unnamed: 20', 'cutoff': 'Unnamed: 24', 'flood': 'Unnamed: 25', 'ats': 'Unnamed: 44', 'battery_hours': 'Unnamed: 41'}
- Khoảng thiếu/rủi ro: Thiếu/không nhận diện: site_code, priority, generator_plan
- Khuyến nghị: Bổ sung mapping cột hoặc đổi header theo mẫu rule

### 2. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/Tong hop_PA PTDS/2
- Vị trí ô: **U2** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 2: ngập=TÀI NGUYÊN HIỆN CÓ, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 3. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/Tong hop_PA PTDS/10
- Vị trí ô: **AP10** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 10: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 4. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/Tong hop_PA PTDS/11
- Vị trí ô: **AP11** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 11: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 5. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/Tong hop_PA PTDS/13
- Vị trí ô: **AP13** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 13: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 6. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/Tong hop_PA PTDS/14
- Vị trí ô: **AP14** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 14: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 7. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/Tong hop_PA PTDS/15
- Vị trí ô: **AP15** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 15: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 8. Đủ trường dữ liệu tối thiểu
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/PL9.1.1_Tram UT1_2_3321
- Loại bất thường: Thiếu trường dữ liệu
- Bằng chứng: Nhận diện được: {'staff': 'Unnamed: 20', 'cutoff': 'Unnamed: 24', 'flood': '37', 'ats': 'Unnamed: 44', 'battery_hours': 'Unnamed: 41'}
- Khoảng thiếu/rủi ro: Thiếu/không nhận diện: site_code, priority, generator_plan
- Khuyến nghị: Bổ sung mapping cột hoặc đổi header theo mẫu rule

### 9. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/PL9.1.1_Tram UT1_2_3321/7
- Vị trí ô: **AP7** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 7: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 10. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/PL9.1.1_Tram UT1_2_3321/10
- Vị trí ô: **AP10** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 10: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 11. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/PL9.1.1_Tram UT1_2_3321/11
- Vị trí ô: **AP11** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 11: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 12. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/PL9.1.1_Tram UT1_2_3321/13
- Vị trí ô: **AP13** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 13: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 13. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/PL9.1.1_Tram UT1_2_3321/14
- Vị trí ô: **AP14** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 14: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 14. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/PL9.1.1_Tram UT1_2_3321/15
- Vị trí ô: **AP15** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 15: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 15. Đủ trường dữ liệu tối thiểu
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/PL9.1.2_Tram Thu phu
- Loại bất thường: Thiếu trường dữ liệu
- Bằng chứng: Nhận diện được: {'staff': 'Unnamed: 20', 'cutoff': 'Unnamed: 24', 'flood': 'Unnamed: 25', 'ats': 'Unnamed: 44', 'battery_hours': 'Unnamed: 41'}
- Khoảng thiếu/rủi ro: Thiếu/không nhận diện: site_code, priority, generator_plan
- Khuyến nghị: Bổ sung mapping cột hoặc đổi header theo mẫu rule

### 16. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/PL9.1.2_Tram Thu phu/2
- Vị trí ô: **U2** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 2: ngập=TÀI NGUYÊN HIỆN CÓ, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 17. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/PL9.1.2_Tram Thu phu/8
- Vị trí ô: **AP8** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 8: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 18. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/PL9.1.2_Tram Thu phu/9
- Vị trí ô: **AP9** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 9: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 19. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/PL9.1.2_Tram Thu phu/10
- Vị trí ô: **AP10** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 10: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 20. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/PL9.1.2_Tram Thu phu/11
- Vị trí ô: **AP11** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 11: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 21. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/PL9.1.2_Tram Thu phu/13
- Vị trí ô: **AP13** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 13: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 22. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/PL9.1.2_Tram Thu phu/14
- Vị trí ô: **AP14** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 14: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 23. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/PL9.1.2_Tram Thu phu/15
- Vị trí ô: **AP15** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 15: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 24. Đủ trường dữ liệu tối thiểu
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/PL9.1.3_Tram NL
- Loại bất thường: Thiếu trường dữ liệu
- Bằng chứng: Nhận diện được: {'staff': 'Unnamed: 20', 'cutoff': 'Unnamed: 24', 'flood': 'Unnamed: 25', 'ats': 'Unnamed: 44', 'battery_hours': 'Unnamed: 41'}
- Khoảng thiếu/rủi ro: Thiếu/không nhận diện: site_code, priority, generator_plan
- Khuyến nghị: Bổ sung mapping cột hoặc đổi header theo mẫu rule

### 25. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/PL9.1.3_Tram NL/2
- Vị trí ô: **U2** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 2: ngập=TÀI NGUYÊN HIỆN CÓ, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 26. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/PL9.1.3_Tram NL/6
- Vị trí ô: **AP6** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 6: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 27. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/PL9.1.3_Tram NL/7
- Vị trí ô: **AP7** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 7: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 28. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/PL9.1.3_Tram NL/8
- Vị trí ô: **U8** | Cột: U | Giá trị: 0
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 8: ngập=2, chia cắt=0, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 29. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/PL9.1.3_Tram NL/10
- Vị trí ô: **AP10** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 10: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 30. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/PL9.1.3_Tram NL/11
- Vị trí ô: **AP11** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 11: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 31. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/PL9.1.3_Tram NL/12
- Vị trí ô: **AP12** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 12: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 32. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/PL9.1.3_Tram NL/13
- Vị trí ô: **AP13** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 13: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 33. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/PL9.1.3_Tram NL/14
- Vị trí ô: **AP14** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 14: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 34. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/PL9.1.3_Tram NL/15
- Vị trí ô: **AP15** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 15: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 35. Đủ trường dữ liệu tối thiểu
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/PL9.1.4_Tram CC
- Loại bất thường: Thiếu trường dữ liệu
- Bằng chứng: Nhận diện được: {'staff': 'Unnamed: 20', 'cutoff': 'Unnamed: 24', 'flood': 'Unnamed: 25', 'ats': 'Unnamed: 44', 'battery_hours': 'Unnamed: 41'}
- Khoảng thiếu/rủi ro: Thiếu/không nhận diện: site_code, priority, generator_plan
- Khuyến nghị: Bổ sung mapping cột hoặc đổi header theo mẫu rule

### 36. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/PL9.1.4_Tram CC/2
- Vị trí ô: **U2** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 2: ngập=TÀI NGUYÊN HIỆN CÓ, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 37. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/PL9.1.4_Tram CC/6
- Vị trí ô: **AP6** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 6: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 38. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/PL9.1.4_Tram CC/10
- Vị trí ô: **AP10** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 10: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 39. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/PL9.1.4_Tram CC/11
- Vị trí ô: **AP11** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 11: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 40. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/PL9.1.4_Tram CC/12
- Vị trí ô: **AP12** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 12: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 41. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/PL9.1.4_Tram CC/13
- Vị trí ô: **AP13** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 13: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 42. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/PL9.1.4_Tram CC/14
- Vị trí ô: **AP14** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 14: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 43. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/PL9.1.4_Tram CC/15
- Vị trí ô: **AP15** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 15: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 44. Đủ trường dữ liệu tối thiểu
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/PL9.1.5_Tram con lai
- Loại bất thường: Thiếu trường dữ liệu
- Bằng chứng: Nhận diện được: {'staff': 'Unnamed: 20', 'cutoff': 'Unnamed: 24', 'flood': 'Unnamed: 25', 'ats': 'Unnamed: 44', 'battery_hours': 'Unnamed: 41'}
- Khoảng thiếu/rủi ro: Thiếu/không nhận diện: site_code, priority, generator_plan
- Khuyến nghị: Bổ sung mapping cột hoặc đổi header theo mẫu rule

### 45. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/PL9.1.5_Tram con lai/2
- Vị trí ô: **U2** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 2: ngập=TÀI NGUYÊN HIỆN CÓ, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 46. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/PL9.1.5_Tram con lai/7
- Vị trí ô: **U7** | Cột: U | Giá trị: 0
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 7: ngập=0, chia cắt=1, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 47. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/PL9.1.5_Tram con lai/10
- Vị trí ô: **AP10** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 10: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 48. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/PL9.1.5_Tram con lai/11
- Vị trí ô: **AP11** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 11: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 49. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/PL9.1.5_Tram con lai/13
- Vị trí ô: **AP13** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 13: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 50. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/PL9.1.5_Tram con lai/14
- Vị trí ô: **AP14** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 14: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 51. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/PL9.1.5_Tram con lai/15
- Vị trí ô: **AP15** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 15: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 52. Đủ trường dữ liệu tối thiểu
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/Tram SCH
- Loại bất thường: Thiếu trường dữ liệu
- Bằng chứng: Nhận diện được: {'staff': 'Unnamed: 20', 'cutoff': 'Unnamed: 24', 'flood': 'Unnamed: 25', 'ats': 'Unnamed: 44', 'battery_hours': 'Unnamed: 41'}
- Khoảng thiếu/rủi ro: Thiếu/không nhận diện: site_code, priority, generator_plan
- Khuyến nghị: Bổ sung mapping cột hoặc đổi header theo mẫu rule

### 53. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/Tram SCH/2
- Vị trí ô: **U2** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 2: ngập=TÀI NGUYÊN HIỆN CÓ, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 54. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/Tram SCH/6
- Vị trí ô: **AP6** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 6: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 55. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/Tram SCH/7
- Vị trí ô: **AP7** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 7: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 56. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/Tram SCH/10
- Vị trí ô: **AP10** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 10: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 57. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/Tram SCH/11
- Vị trí ô: **AP11** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 11: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 58. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/Tram SCH/12
- Vị trí ô: **AP12** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 12: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 59. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/Tram SCH/13
- Vị trí ô: **AP13** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 13: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 60. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/Tram SCH/14
- Vị trí ô: **AP14** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 14: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 61. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/Tram SCH/15
- Vị trí ô: **AP15** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 15: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 62. Đủ trường dữ liệu tối thiểu
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/Tram UT1
- Loại bất thường: Thiếu trường dữ liệu
- Bằng chứng: Nhận diện được: {'staff': 'Unnamed: 20', 'cutoff': 'Unnamed: 24', 'flood': 'Unnamed: 25', 'ats': 'Unnamed: 44', 'battery_hours': 'Unnamed: 41'}
- Khoảng thiếu/rủi ro: Thiếu/không nhận diện: site_code, priority, generator_plan
- Khuyến nghị: Bổ sung mapping cột hoặc đổi header theo mẫu rule

### 63. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/Tram UT1/2
- Vị trí ô: **U2** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 2: ngập=TÀI NGUYÊN HIỆN CÓ, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 64. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/Tram UT1/7
- Vị trí ô: **AP7** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 7: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 65. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/Tram UT1/9
- Vị trí ô: **U9** | Cột: U | Giá trị: 0
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 9: ngập=2, chia cắt=0, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 66. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/Tram UT1/10
- Vị trí ô: **AP10** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 10: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 67. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/Tram UT1/11
- Vị trí ô: **AP11** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 11: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 68. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/Tram UT1/13
- Vị trí ô: **AP13** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 13: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 69. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/Tram UT1/14
- Vị trí ô: **AP14** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 14: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 70. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/Tram UT1/15
- Vị trí ô: **AP15** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 15: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 71. Đủ trường dữ liệu tối thiểu
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/Tram UT2
- Loại bất thường: Thiếu trường dữ liệu
- Bằng chứng: Nhận diện được: {'staff': 'Unnamed: 20', 'cutoff': 'Unnamed: 24', 'flood': 'Unnamed: 25', 'ats': 'Unnamed: 44', 'battery_hours': 'Unnamed: 41'}
- Khoảng thiếu/rủi ro: Thiếu/không nhận diện: site_code, priority, generator_plan
- Khuyến nghị: Bổ sung mapping cột hoặc đổi header theo mẫu rule

### 72. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/Tram UT2/2
- Vị trí ô: **U2** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 2: ngập=TÀI NGUYÊN HIỆN CÓ, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 73. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/Tram UT2/6
- Vị trí ô: **AP6** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 6: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 74. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/Tram UT2/7
- Vị trí ô: **AP7** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 7: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 75. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/Tram UT2/10
- Vị trí ô: **AP10** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 10: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 76. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/Tram UT2/11
- Vị trí ô: **AP11** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 11: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 77. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/Tram UT2/12
- Vị trí ô: **AP12** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 12: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 78. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/Tram UT2/13
- Vị trí ô: **AP13** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 13: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 79. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/Tram UT2/14
- Vị trí ô: **AP14** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 14: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 80. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/Tram UT2/15
- Vị trí ô: **AP15** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 15: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 81. Đủ trường dữ liệu tối thiểu
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT
- Loại bất thường: Thiếu trường dữ liệu
- Bằng chứng: Nhận diện được: {'staff': 'BỔ SUNG CỘT ==> Tính toán theo quan điểm PCTT', 'cutoff': 'Unnamed: 24', 'flood': 'BỔ SUNG CỘT.7', 'ats': 'Unnamed: 44', 'battery_hours': 'Unnamed: 41'}
- Khoảng thiếu/rủi ro: Thiếu/không nhận diện: site_code, priority, generator_plan
- Khuyến nghị: Bổ sung mapping cột hoặc đổi header theo mẫu rule

### 82. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/input_PA PCTT/5
- Vị trí ô: **DH5** | Cột: DH | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 5: ngập=, chia cắt=161, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 83. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/9
- Vị trí ô: **AP9** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 9: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 84. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/12
- Vị trí ô: **AP12** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 12: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 85. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/16
- Vị trí ô: **AP16** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 16: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 86. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/18
- Vị trí ô: **AP18** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 18: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 87. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/20
- Vị trí ô: **AP20** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 20: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 88. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/21
- Vị trí ô: **AP21** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 21: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 89. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/22
- Vị trí ô: **AP22** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 22: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 90. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/27
- Vị trí ô: **AP27** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 27: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 91. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/29
- Vị trí ô: **AP29** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 29: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 92. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/31
- Vị trí ô: **AP31** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 31: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 93. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/38
- Vị trí ô: **AP38** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 38: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 94. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/44
- Vị trí ô: **AP44** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 44: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 95. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/49
- Vị trí ô: **AP49** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 49: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 96. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/50
- Vị trí ô: **AP50** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 50: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 97. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/51
- Vị trí ô: **AP51** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 51: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 98. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/53
- Vị trí ô: **AP53** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 53: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 99. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/54
- Vị trí ô: **AP54** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 54: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 100. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/58
- Vị trí ô: **AP58** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 58: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 101. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/63
- Vị trí ô: **AP63** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 63: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 102. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/67
- Vị trí ô: **AP67** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 67: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 103. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/69
- Vị trí ô: **AP69** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 69: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 104. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/72
- Vị trí ô: **AP72** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 72: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 105. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/74
- Vị trí ô: **AP74** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 74: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 106. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/75
- Vị trí ô: **AP75** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 75: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 107. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/78
- Vị trí ô: **AP78** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 78: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 108. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/80
- Vị trí ô: **AP80** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 80: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 109. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/82
- Vị trí ô: **AP82** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 82: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 110. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/84
- Vị trí ô: **AP84** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 84: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 111. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/85
- Vị trí ô: **AP85** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 85: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 112. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/88
- Vị trí ô: **AP88** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 88: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 113. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/94
- Vị trí ô: **AP94** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 94: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 114. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/96
- Vị trí ô: **AP96** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 96: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 115. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/107
- Vị trí ô: **AP107** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 107: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 116. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/123
- Vị trí ô: **AP123** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 123: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 117. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/135
- Vị trí ô: **AP135** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 135: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 118. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/139
- Vị trí ô: **AP139** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 139: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 119. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/144
- Vị trí ô: **AP144** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 144: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 120. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/145
- Vị trí ô: **AP145** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 145: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 121. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/146
- Vị trí ô: **AP146** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 146: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 122. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/148
- Vị trí ô: **AP148** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 148: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 123. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/149
- Vị trí ô: **AP149** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 149: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 124. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/155
- Vị trí ô: **AP155** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 155: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 125. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/159
- Vị trí ô: **AP159** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 159: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 126. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/178
- Vị trí ô: **AP178** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 178: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 127. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/186
- Vị trí ô: **AP186** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 186: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 128. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/191
- Vị trí ô: **AP191** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 191: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 129. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/198
- Vị trí ô: **AP198** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 198: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 130. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/203
- Vị trí ô: **AP203** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 203: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 131. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/213
- Vị trí ô: **AP213** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 213: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 132. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/214
- Vị trí ô: **AP214** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 214: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 133. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/218
- Vị trí ô: **AP218** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 218: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 134. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/227
- Vị trí ô: **AP227** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 227: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 135. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/233
- Vị trí ô: **AP233** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 233: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 136. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/250
- Vị trí ô: **AP250** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 250: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 137. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/256
- Vị trí ô: **AP256** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 256: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 138. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/267
- Vị trí ô: **AP267** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 267: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 139. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/269
- Vị trí ô: **AP269** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 269: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 140. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/283
- Vị trí ô: **AP283** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 283: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 141. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/292
- Vị trí ô: **AP292** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 292: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 142. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/304
- Vị trí ô: **AP304** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 304: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 143. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/320
- Vị trí ô: **AP320** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 320: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 144. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/321
- Vị trí ô: **AP321** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 321: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 145. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/322
- Vị trí ô: **AP322** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 322: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 146. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/327
- Vị trí ô: **AP327** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 327: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 147. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/328
- Vị trí ô: **AP328** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 328: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 148. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/330
- Vị trí ô: **AP330** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 330: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 149. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/331
- Vị trí ô: **AP331** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 331: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 150. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/333
- Vị trí ô: **AP333** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 333: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 151. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/334
- Vị trí ô: **AP334** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 334: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 152. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/349
- Vị trí ô: **AP349** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 349: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 153. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/355
- Vị trí ô: **AP355** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 355: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 154. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/374
- Vị trí ô: **AP374** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 374: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 155. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/375
- Vị trí ô: **AP375** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 375: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 156. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/379
- Vị trí ô: **AP379** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 379: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 157. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/386
- Vị trí ô: **AP386** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 386: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 158. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/389
- Vị trí ô: **AP389** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 389: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 159. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/392
- Vị trí ô: **AP392** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 392: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 160. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/401
- Vị trí ô: **AP401** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 401: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 161. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/412
- Vị trí ô: **AP412** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 412: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 162. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/419
- Vị trí ô: **AP419** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 419: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 163. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/421
- Vị trí ô: **AP421** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 421: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 164. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/432
- Vị trí ô: **AP432** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 432: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 165. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/434
- Vị trí ô: **AP434** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 434: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 166. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/440
- Vị trí ô: **AP440** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 440: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 167. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/441
- Vị trí ô: **AP441** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 441: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 168. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/446
- Vị trí ô: **AP446** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 446: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 169. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/451
- Vị trí ô: **AP451** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 451: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 170. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/459
- Vị trí ô: **AP459** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 459: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 171. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/464
- Vị trí ô: **AP464** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 464: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 172. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/465
- Vị trí ô: **AP465** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 465: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 173. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/471
- Vị trí ô: **AP471** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 471: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 174. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/477
- Vị trí ô: **AP477** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 477: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 175. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/478
- Vị trí ô: **AP478** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 478: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 176. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/481
- Vị trí ô: **AP481** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 481: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 177. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/490
- Vị trí ô: **AP490** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 490: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 178. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/491
- Vị trí ô: **AP491** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 491: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 179. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/503
- Vị trí ô: **AP503** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 503: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 180. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/524
- Vị trí ô: **AP524** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 524: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 181. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/526
- Vị trí ô: **AP526** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 526: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 182. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/527
- Vị trí ô: **AP527** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 527: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 183. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/536
- Vị trí ô: **AP536** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 536: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 184. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/547
- Vị trí ô: **AP547** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 547: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 185. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/560
- Vị trí ô: **AP560** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 560: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 186. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/566
- Vị trí ô: **AP566** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 566: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 187. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/567
- Vị trí ô: **AP567** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 567: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 188. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/568
- Vị trí ô: **AP568** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 568: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 189. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/581
- Vị trí ô: **AP581** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 581: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 190. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/584
- Vị trí ô: **AP584** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 584: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 191. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/593
- Vị trí ô: **AP593** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 593: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 192. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/595
- Vị trí ô: **AP595** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 595: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 193. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/609
- Vị trí ô: **AP609** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 609: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 194. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/611
- Vị trí ô: **AP611** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 611: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 195. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/614
- Vị trí ô: **AP614** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 614: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 196. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/617
- Vị trí ô: **AP617** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 617: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 197. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/625
- Vị trí ô: **AP625** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 625: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 198. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/631
- Vị trí ô: **AP631** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 631: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 199. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/632
- Vị trí ô: **AP632** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 632: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 200. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/636
- Vị trí ô: **AP636** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 636: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 201. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/644
- Vị trí ô: **AP644** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 644: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 202. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/645
- Vị trí ô: **AP645** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 645: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 203. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/650
- Vị trí ô: **AP650** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 650: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 204. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/656
- Vị trí ô: **AP656** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 656: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 205. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/660
- Vị trí ô: **AP660** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 660: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 206. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/661
- Vị trí ô: **AP661** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 661: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 207. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/663
- Vị trí ô: **AP663** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 663: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 208. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/664
- Vị trí ô: **AP664** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 664: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 209. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/668
- Vị trí ô: **AP668** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 668: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 210. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/669
- Vị trí ô: **AP669** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 669: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 211. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/670
- Vị trí ô: **AP670** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 670: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 212. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/671
- Vị trí ô: **AP671** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 671: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 213. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/672
- Vị trí ô: **AP672** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 672: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 214. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/677
- Vị trí ô: **AP677** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 677: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 215. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/688
- Vị trí ô: **AP688** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 688: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 216. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/692
- Vị trí ô: **AP692** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 692: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 217. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/700
- Vị trí ô: **AP700** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 700: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 218. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/707
- Vị trí ô: **AP707** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 707: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 219. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/712
- Vị trí ô: **AP712** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 712: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 220. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/714
- Vị trí ô: **AP714** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 714: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 221. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/715
- Vị trí ô: **AP715** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 715: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 222. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/716
- Vị trí ô: **AP716** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 716: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 223. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/718
- Vị trí ô: **AP718** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 718: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 224. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/730
- Vị trí ô: **AP730** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 730: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 225. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/736
- Vị trí ô: **AP736** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 736: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 226. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/751
- Vị trí ô: **AP751** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 751: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 227. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/753
- Vị trí ô: **AP753** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 753: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 228. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/761
- Vị trí ô: **AP761** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 761: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 229. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/762
- Vị trí ô: **AP762** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 762: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 230. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/766
- Vị trí ô: **AP766** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 766: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 231. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/767
- Vị trí ô: **AP767** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 767: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 232. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/768
- Vị trí ô: **AP768** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 768: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 233. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/783
- Vị trí ô: **AP783** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 783: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 234. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/789
- Vị trí ô: **AP789** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 789: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 235. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/796
- Vị trí ô: **AP796** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 796: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 236. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/807
- Vị trí ô: **AP807** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 807: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 237. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/809
- Vị trí ô: **AP809** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 809: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 238. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/811
- Vị trí ô: **AP811** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 811: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 239. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/816
- Vị trí ô: **AP816** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 816: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 240. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/817
- Vị trí ô: **AP817** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 817: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 241. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/819
- Vị trí ô: **AP819** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 819: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 242. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/832
- Vị trí ô: **AP832** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 832: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 243. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/840
- Vị trí ô: **AP840** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 840: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 244. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/843
- Vị trí ô: **AP843** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 843: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 245. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/845
- Vị trí ô: **AP845** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 845: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 246. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/862
- Vị trí ô: **AP862** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 862: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 247. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/863
- Vị trí ô: **AP863** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 863: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 248. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/864
- Vị trí ô: **AP864** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 864: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 249. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/865
- Vị trí ô: **AP865** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 865: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 250. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/866
- Vị trí ô: **AP866** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 866: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 251. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/867
- Vị trí ô: **AP867** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 867: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 252. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/868
- Vị trí ô: **AP868** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 868: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 253. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/869
- Vị trí ô: **AP869** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 869: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 254. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/873
- Vị trí ô: **AP873** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 873: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 255. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/874
- Vị trí ô: **AP874** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 874: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 256. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/875
- Vị trí ô: **AP875** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 875: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 257. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/885
- Vị trí ô: **AP885** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 885: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 258. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/891
- Vị trí ô: **AP891** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 891: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 259. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/892
- Vị trí ô: **AP892** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 892: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 260. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/899
- Vị trí ô: **AP899** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 899: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 261. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/903
- Vị trí ô: **AP903** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 903: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 262. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/914
- Vị trí ô: **AP914** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 914: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 263. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/915
- Vị trí ô: **AP915** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 915: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 264. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/916
- Vị trí ô: **AP916** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 916: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 265. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/922
- Vị trí ô: **AP922** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 922: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 266. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/937
- Vị trí ô: **AP937** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 937: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 267. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/942
- Vị trí ô: **AP942** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 942: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 268. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/943
- Vị trí ô: **AP943** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 943: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 269. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/945
- Vị trí ô: **AP945** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 945: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 270. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/946
- Vị trí ô: **AP946** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 946: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 271. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/947
- Vị trí ô: **AP947** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 947: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 272. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/949
- Vị trí ô: **AP949** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 949: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 273. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/950
- Vị trí ô: **AP950** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 950: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 274. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/952
- Vị trí ô: **AP952** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 952: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 275. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/953
- Vị trí ô: **AP953** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 953: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 276. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/954
- Vị trí ô: **AP954** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 954: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 277. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/955
- Vị trí ô: **AP955** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 955: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 278. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/956
- Vị trí ô: **AP956** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 956: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 279. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/958
- Vị trí ô: **AP958** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 958: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 280. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/980
- Vị trí ô: **AP980** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 980: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 281. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/982
- Vị trí ô: **AP982** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 982: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 282. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/986
- Vị trí ô: **AP986** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 986: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 283. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/993
- Vị trí ô: **AP993** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 993: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 284. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/999
- Vị trí ô: **AP999** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 999: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 285. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/1000
- Vị trí ô: **AP1000** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 1000: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 286. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/1010
- Vị trí ô: **AP1010** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 1010: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 287. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/1012
- Vị trí ô: **AP1012** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 1012: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 288. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/1027
- Vị trí ô: **AP1027** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 1027: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 289. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/1028
- Vị trí ô: **AP1028** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 1028: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 290. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/1039
- Vị trí ô: **AP1039** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 1039: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 291. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/1045
- Vị trí ô: **AP1045** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 1045: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 292. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/1046
- Vị trí ô: **AP1046** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 1046: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 293. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/1058
- Vị trí ô: **AP1058** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 1058: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 294. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/1061
- Vị trí ô: **AP1061** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 1061: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 295. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/1068
- Vị trí ô: **AP1068** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 1068: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 296. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/1081
- Vị trí ô: **AP1081** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 1081: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 297. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/1088
- Vị trí ô: **AP1088** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 1088: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 298. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/1095
- Vị trí ô: **AP1095** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 1095: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 299. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/1096
- Vị trí ô: **AP1096** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 1096: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 300. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/1104
- Vị trí ô: **AP1104** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 1104: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 301. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/1110
- Vị trí ô: **AP1110** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 1110: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 302. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/1114
- Vị trí ô: **AP1114** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 1114: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 303. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/1120
- Vị trí ô: **AP1120** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 1120: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 304. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/1124
- Vị trí ô: **AP1124** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 1124: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 305. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/1127
- Vị trí ô: **AP1127** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 1127: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 306. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/1129
- Vị trí ô: **AP1129** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 1129: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 307. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/1132
- Vị trí ô: **AP1132** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 1132: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 308. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/1138
- Vị trí ô: **AP1138** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 1138: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 309. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/1140
- Vị trí ô: **AP1140** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 1140: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 310. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/1145
- Vị trí ô: **AP1145** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 1145: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 311. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/1146
- Vị trí ô: **AP1146** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 1146: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 312. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/1150
- Vị trí ô: **AP1150** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 1150: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 313. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/1151
- Vị trí ô: **AP1151** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 1151: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 314. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/1162
- Vị trí ô: **AP1162** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 1162: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 315. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/1183
- Vị trí ô: **AP1183** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 1183: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 316. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/1199
- Vị trí ô: **AP1199** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 1199: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 317. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/1215
- Vị trí ô: **AP1215** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 1215: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 318. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/1219
- Vị trí ô: **AP1219** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 1219: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 319. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/1223
- Vị trí ô: **AP1223** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 1223: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 320. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/1240
- Vị trí ô: **AP1240** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 1240: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 321. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/input_PA PCTT/1252
- Vị trí ô: **AP1252** | Cột: AP | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 1252: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 322. Nhận diện cột dữ liệu
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DU_DU_LIEU** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/Sheet2
- Loại bất thường: Thiếu mapping/header
- Bằng chứng: Sample.xlsx/Sheet2: không nhận diện được cột chuẩn
- Khoảng thiếu/rủi ro: Thiếu header hoặc header không rõ
- Khuyến nghị: Chuẩn hóa header hoặc mapping cột trong file CSDL

### 323. Đủ trường dữ liệu tối thiểu
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/Bao cao a Namkv2
- Loại bất thường: Thiếu trường dữ liệu
- Bằng chứng: Nhận diện được: {'site_code': 'Tổng số trạm', 'generator_plan': 'Tổng số MPĐ ở tỉnh trước bão số 13', 'battery_hours': 'TT'}
- Khoảng thiếu/rủi ro: Thiếu/không nhận diện: priority, staff, flood, cutoff, ats
- Khuyến nghị: Bổ sung mapping cột hoặc đổi header theo mẫu rule

### 324. Đủ trường dữ liệu tối thiểu
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/Bao cao file doc
- Loại bất thường: Thiếu trường dữ liệu
- Bằng chứng: Nhận diện được: {'site_code': 'Tổng số trạm', 'staff': 'Số bình acquy cần để đảm bảo TGX cho nhóm trạm cần UCTT trong bão (bỏ các trạm có thể đặt MPĐ cố định tại trạm trong thiên tai => ém quân và đảm bảo xăng dầu vận hành)', 'generator_plan': 'Trạm vận hành được MPĐ trong thiên tai', 'battery_hours': 'Tổng số bình ắc quy portable hiện có tại tỉnh '}
- Khoảng thiếu/rủi ro: Thiếu/không nhận diện: priority, flood, cutoff, ats
- Khuyến nghị: Bổ sung mapping cột hoặc đổi header theo mẫu rule

### 325. Đủ trường dữ liệu tối thiểu
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/PA tung tram
- Loại bất thường: Thiếu trường dữ liệu
- Bằng chứng: Nhận diện được: {'site_code': 'Mã trạm', 'priority': 'Mã trạm'}
- Khoảng thiếu/rủi ro: Thiếu/không nhận diện: staff, flood, cutoff, ats, generator_plan, battery_hours
- Khuyến nghị: Bổ sung mapping cột hoặc đổi header theo mẫu rule

### 326. Đủ trường dữ liệu tối thiểu
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/output_profile
- Loại bất thường: Thiếu trường dữ liệu
- Bằng chứng: Nhận diện được: {'cutoff': 'KHA', 'distance_km': 'KHA', 'staff': 'Unnamed: 20', 'flood': 'Unnamed: 25', 'ats': 'Unnamed: 44', 'battery_hours': 'Unnamed: 41'}
- Khoảng thiếu/rủi ro: Thiếu/không nhận diện: site_code, priority, generator_plan
- Khuyến nghị: Bổ sung mapping cột hoặc đổi header theo mẫu rule

### 327. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/2
- Vị trí ô: **U2** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 2: ngập=, chia cắt=B1 - Hạ tầng mạng lưới, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 328. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/6
- Vị trí ô: **U6** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 6: ngập=NTN, chia cắt=1, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 329. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/7
- Vị trí ô: **U7** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 7: ngập=KHA, chia cắt=2, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 330. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/8
- Vị trí ô: **U8** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 8: ngập=NTN, chia cắt=1, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 331. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/9
- Vị trí ô: **U9** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 9: ngập=NTN, chia cắt=2, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 332. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/10
- Vị trí ô: **U10** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 10: ngập=NTN, chia cắt=3, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 333. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/11
- Vị trí ô: **U11** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 11: ngập=NTN, chia cắt=4, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 334. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/12
- Vị trí ô: **U12** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 12: ngập=KHA, chia cắt=5, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 335. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/13
- Vị trí ô: **U13** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 13: ngập=KHA, chia cắt=6, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 336. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/14
- Vị trí ô: **U14** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 14: ngập=KHA, chia cắt=7, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 337. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/15
- Vị trí ô: **U15** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 15: ngập=KHA, chia cắt=8, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 338. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/16
- Vị trí ô: **U16** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 16: ngập=KHA, chia cắt=9, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 339. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/17
- Vị trí ô: **U17** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 17: ngập=, chia cắt=10, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 340. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/18
- Vị trí ô: **U18** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 18: ngập=, chia cắt=11, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 341. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/19
- Vị trí ô: **U19** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 19: ngập=, chia cắt=12, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 342. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/20
- Vị trí ô: **U20** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 20: ngập=, chia cắt=13, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 343. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/21
- Vị trí ô: **U21** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 21: ngập=, chia cắt=14, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 344. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/22
- Vị trí ô: **U22** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 22: ngập=, chia cắt=15, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 345. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/23
- Vị trí ô: **U23** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 23: ngập=, chia cắt=16, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 346. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/29
- Vị trí ô: **U29** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 29: ngập=, chia cắt=B2 - Đảm bảo nhiên liệu, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 347. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/30
- Vị trí ô: **U30** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 30: ngập=, chia cắt=STT, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 348. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/31
- Vị trí ô: **U31** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 31: ngập=, chia cắt=STT, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 349. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/33
- Vị trí ô: **U33** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 33: ngập=, chia cắt=1, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 350. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/34
- Vị trí ô: **U34** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 34: ngập=, chia cắt=2, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 351. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/35
- Vị trí ô: **U35** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 35: ngập=, chia cắt=1, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 352. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/36
- Vị trí ô: **U36** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 36: ngập=, chia cắt=2, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 353. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/37
- Vị trí ô: **U37** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 37: ngập=, chia cắt=3, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 354. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/38
- Vị trí ô: **U38** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 38: ngập=, chia cắt=4, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 355. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/39
- Vị trí ô: **U39** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 39: ngập=, chia cắt=5, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 356. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/40
- Vị trí ô: **U40** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 40: ngập=, chia cắt=6, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 357. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/41
- Vị trí ô: **U41** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 41: ngập=, chia cắt=7, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 358. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/42
- Vị trí ô: **U42** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 42: ngập=, chia cắt=8, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 359. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/43
- Vị trí ô: **U43** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 43: ngập=, chia cắt=9, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 360. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/44
- Vị trí ô: **U44** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 44: ngập=, chia cắt=10, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 361. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/45
- Vị trí ô: **U45** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 45: ngập=, chia cắt=11, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 362. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/46
- Vị trí ô: **U46** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 46: ngập=, chia cắt=12, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 363. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/47
- Vị trí ô: **U47** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 47: ngập=, chia cắt=13, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 364. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/48
- Vị trí ô: **U48** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 48: ngập=, chia cắt=14, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 365. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/49
- Vị trí ô: **U49** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 49: ngập=, chia cắt=15, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 366. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/50
- Vị trí ô: **U50** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 50: ngập=, chia cắt=16, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 367. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/53
- Vị trí ô: **U53** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 53: ngập=, chia cắt=B3 - Nhân sự ém quân, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 368. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/54
- Vị trí ô: **U54** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 54: ngập=, chia cắt=STT, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 369. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/55
- Vị trí ô: **U55** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 55: ngập=, chia cắt=STT, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 370. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/57
- Vị trí ô: **U57** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 57: ngập=, chia cắt=1, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 371. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/58
- Vị trí ô: **U58** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 58: ngập=, chia cắt=2, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 372. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/59
- Vị trí ô: **U59** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 59: ngập=, chia cắt=1, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 373. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/60
- Vị trí ô: **U60** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 60: ngập=, chia cắt=2, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 374. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/61
- Vị trí ô: **U61** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 61: ngập=, chia cắt=3, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 375. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/62
- Vị trí ô: **U62** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 62: ngập=, chia cắt=4, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 376. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/63
- Vị trí ô: **U63** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 63: ngập=, chia cắt=5, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 377. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/64
- Vị trí ô: **U64** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 64: ngập=, chia cắt=6, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 378. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/65
- Vị trí ô: **U65** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 65: ngập=, chia cắt=7, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 379. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/66
- Vị trí ô: **U66** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 66: ngập=, chia cắt=8, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 380. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/67
- Vị trí ô: **U67** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 67: ngập=, chia cắt=9, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 381. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/output_profile/78
- Vị trí ô: **U78** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 78: ngập=PA2
Có thể đặt gửi tạm 3 tháng, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 382. Đủ trường dữ liệu tối thiểu
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/Sheet1
- Loại bất thường: Thiếu trường dữ liệu
- Bằng chứng: Nhận diện được: {'generator_plan': 'Số MPĐ sau sau điều chuyển lượt 1 (17/10)'}
- Khoảng thiếu/rủi ro: Thiếu/không nhận diện: site_code, priority, staff, flood, cutoff, ats, battery_hours
- Khuyến nghị: Bổ sung mapping cột hoặc đổi header theo mẫu rule

### 383. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/Nhom UT12/4
- Vị trí ô: **AR4** | Cột: AR | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 4: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 384. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/Nhom NL/2
- Vị trí ô: **AU2** | Cột: AU | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: Tổng số trạm: ngập=SCH, chia cắt=ATS, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 385. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/Nhom NL/3
- Vị trí ô: **AU3** | Cột: AU | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1256: ngập=, chia cắt=15, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 386. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/Nhom NL/4
- Vị trí ô: **AU4** | Cột: AU | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 385: ngập=, chia cắt=5, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 387. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/Nhom NL/4
- Vị trí ô: **AQ4** | Cột: AQ | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: 385: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 388. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/Nhom NL/5
- Vị trí ô: **AU5** | Cột: AU | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 871: ngập=, chia cắt=10, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 389. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/Nhom NL/7
- Vị trí ô: **AU7** | Cột: AU | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 83: ngập=, chia cắt=1, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 390. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/Nhom NL/8
- Vị trí ô: **AU8** | Cột: AU | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 106: ngập=, chia cắt=4, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 391. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/Nhom NL/10
- Vị trí ô: **AU10** | Cột: AU | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 341: ngập=, chia cắt=2, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 392. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/Nhom NL/12
- Vị trí ô: **AU12** | Cột: AU | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 112: ngập=, chia cắt=7, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 393. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/Nhom NL/13
- Vị trí ô: **AU13** | Cột: AU | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 138: ngập=, chia cắt=1, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 394. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/Nhom CC/2
- Vị trí ô: **AU2** | Cột: AU | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: Tổng số trạm: ngập=SCH, chia cắt=ATS, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 395. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/Nhom CC/3
- Vị trí ô: **AU3** | Cột: AU | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 3: ngập=, chia cắt=47, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 396. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/Nhom CC/4
- Vị trí ô: **AU4** | Cột: AU | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 4: ngập=, chia cắt=13, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 397. Thời gian xả ắc quy không được bất thường bằng 0
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/Nhom CC/4
- Vị trí ô: **AQ4** | Cột: AQ | Giá trị: 0
- Loại bất thường: Giá trị bằng 0
- Bằng chứng: row 4: TGX=0.0
- Khoảng thiếu/rủi ro: TGX = 0 có khả năng thiếu hoặc sai dữ liệu
- Khuyến nghị: Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy

### 398. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/Nhom CC/5
- Vị trí ô: **AU5** | Cột: AU | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 5: ngập=, chia cắt=34, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 399. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/Nhom CC/7
- Vị trí ô: **AU7** | Cột: AU | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 7: ngập=, chia cắt=2, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 400. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/Nhom CC/8
- Vị trí ô: **AU8** | Cột: AU | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 8: ngập=, chia cắt=8, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 401. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/Nhom CC/9
- Vị trí ô: **AU9** | Cột: AU | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 9: ngập=, chia cắt=3, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 402. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/Nhom CC/10
- Vị trí ô: **AU10** | Cột: AU | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 10: ngập=, chia cắt=4, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 403. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/Nhom CC/11
- Vị trí ô: **AU11** | Cột: AU | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 11: ngập=, chia cắt=8, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 404. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/Nhom CC/12
- Vị trí ô: **AU12** | Cột: AU | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 12: ngập=, chia cắt=8, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 405. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/Nhom CC/13
- Vị trí ô: **AU13** | Cột: AU | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 13: ngập=, chia cắt=6, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 406. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/Nhom CC/14
- Vị trí ô: **AU14** | Cột: AU | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 14: ngập=, chia cắt=8, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 407. Đủ trường dữ liệu tối thiểu
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/ĐM NL MPĐ
- Loại bất thường: Thiếu trường dữ liệu
- Bằng chứng: Nhận diện được: {'staff': 'Unnamed: 20', 'cutoff': 'Unnamed: 24', 'flood': 'Xăng'}
- Khoảng thiếu/rủi ro: Thiếu/không nhận diện: site_code, priority, ats, generator_plan, battery_hours
- Khuyến nghị: Bổ sung mapping cột hoặc đổi header theo mẫu rule

### 408. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/ĐM NL MPĐ/3
- Vị trí ô: **U3** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 3: ngập=, chia cắt=16.666666666666668, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 409. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/ĐM NL MPĐ/4
- Vị trí ô: **U4** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 4: ngập=3.3, chia cắt=12.5, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 410. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/ĐM NL MPĐ/5
- Vị trí ô: **U5** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 5: ngập=CS_8_Dầu_40l, chia cắt=12.5, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 411. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/ĐM NL MPĐ/6
- Vị trí ô: **U6** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 6: ngập=CS_10_Dầu_50l, chia cắt=13.513513513513512, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 412. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/ĐM NL MPĐ/7
- Vị trí ô: **U7** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 7: ngập=CS_15_Dầu_65l, chia cắt=12.264150943396228, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 413. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/ĐM NL MPĐ/15
- Vị trí ô: **U15** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 15: ngập=CS_6,5_Xăng_17l, chia cắt=5.151515151515151, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 414. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/ĐM NL MPĐ/16
- Vị trí ô: **U16** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 16: ngập=CS_8,8_Xăng_27l, chia cắt=6, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 415. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/ĐM NL MPĐ/17
- Vị trí ô: **U17** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: row 17: ngập=CS_10_Xăng_38l, chia cắt=7.037037037037036, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 416. Đủ trường dữ liệu tối thiểu
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/rules PCTT
- Loại bất thường: Thiếu trường dữ liệu
- Bằng chứng: Nhận diện được: {'site_code': '1. Định nghĩa Trạm ưu tiên', 'priority': '1. Định nghĩa Trạm ưu tiên', 'staff': 'Unnamed: 20'}
- Khoảng thiếu/rủi ro: Thiếu/không nhận diện: flood, cutoff, ats, generator_plan, battery_hours
- Khuyến nghị: Bổ sung mapping cột hoặc đổi header theo mẫu rule

### 417. 100% trạm UT1/UT1_3321 phải có nhân sự ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **HIGH**
- Nguồn: Sample.xlsx/rules PCTT/4
- Vị trí ô: **U4** | Cột: U | Giá trị: 
- Loại bất thường: Ô trống/bất thường
- Bằng chứng: Định nghĩa trạm SCH: Là trạm UT1 thuộc một trong các mục đích sau:: priority=ĐỊNH NGHĨA TRẠM SCH: LÀ TRẠM UT1 THUỘC MỘT TRONG CÁC MỤC ĐÍCH SAU:, nhân sự ém quân trống
- Khoảng thiếu/rủi ro: Thiếu nhân sự ém quân
- Khuyến nghị: Bổ sung họ tên, SĐT, vị trí ém quân và ca trực

### 418. 100% trạm UT1/UT1_3321 phải có nhân sự ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **HIGH**
- Nguồn: Sample.xlsx/rules PCTT/52
- Vị trí ô: **U52** | Cột: U | Giá trị: 
- Loại bất thường: Ô trống/bất thường
- Bằng chứng: Mức UT1:: priority=MỨC UT1:, nhân sự ém quân trống
- Khoảng thiếu/rủi ro: Thiếu nhân sự ém quân
- Khuyến nghị: Bổ sung họ tên, SĐT, vị trí ém quân và ca trực

### 419. 100% trạm UT1/UT1_3321 phải có nhân sự ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **HIGH**
- Nguồn: Sample.xlsx/rules PCTT/59
- Vị trí ô: **U59** | Cột: U | Giá trị: 
- Loại bất thường: Ô trống/bất thường
- Bằng chứng: Mức UT1:: priority=MỨC UT1:, nhân sự ém quân trống
- Khoảng thiếu/rủi ro: Thiếu nhân sự ém quân
- Khuyến nghị: Bổ sung họ tên, SĐT, vị trí ém quân và ca trực

### 420. Đủ trường dữ liệu tối thiểu
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/CSDL
- Loại bất thường: Thiếu trường dữ liệu
- Bằng chứng: Nhận diện được: {'site_code': 'Matram', 'priority': 'Matram', 'distance_km': 'Cum', 'staff': 'Unnamed: 20', 'cutoff': 'Unnamed: 24', 'flood': 'Unnamed: 25'}
- Khoảng thiếu/rủi ro: Thiếu/không nhận diện: ats, generator_plan, battery_hours
- Khuyến nghị: Bổ sung mapping cột hoặc đổi header theo mẫu rule

### 421. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/CSDL/2
- Vị trí ô: **U2** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: Mã vị trí: ngập=, chia cắt=SotramUCTT, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 422. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/CSDL/3
- Vị trí ô: **U3** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: QBH0051: ngập=, chia cắt=473, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 423. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/CSDL/4
- Vị trí ô: **U4** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: QTI3991: ngập=, chia cắt=373, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 424. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/CSDL/5
- Vị trí ô: **U5** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: QTI0138: ngập=, chia cắt=354, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 425. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/CSDL/6
- Vị trí ô: **U6** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: QTI0414: ngập=, chia cắt=669, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 426. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/CSDL/7
- Vị trí ô: **U7** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: QTI0060: ngập=, chia cắt=944, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 427. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/CSDL/8
- Vị trí ô: **U8** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: QTI0054: ngập=, chia cắt=596, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 428. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/CSDL/9
- Vị trí ô: **U9** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: QTI8002: ngập=, chia cắt=562, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 429. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/CSDL/10
- Vị trí ô: **U10** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: QTI8003: ngập=, chia cắt=567, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 430. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/CSDL/11
- Vị trí ô: **U11** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: QTI8101: ngập=, chia cắt=254, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 431. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/CSDL/12
- Vị trí ô: **U12** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: QTI8102: ngập=, chia cắt=545, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 432. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/CSDL/13
- Vị trí ô: **U13** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: QTI8702: ngập=, chia cắt=487, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 433. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/CSDL/14
- Vị trí ô: **U14** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: QTI0007: ngập=, chia cắt=302, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 434. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/CSDL/15
- Vị trí ô: **U15** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: QTI0008: ngập=, chia cắt=618, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 435. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/CSDL/16
- Vị trí ô: **U16** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: QTI0044: ngập=, chia cắt=484, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 436. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/CSDL/17
- Vị trí ô: **U17** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: QTI0040: ngập=, chia cắt=275, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 437. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/CSDL/18
- Vị trí ô: **U18** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: QTI0199: ngập=, chia cắt=525, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 438. Đủ trường dữ liệu tối thiểu
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/BM01_tramUT.VT
- Loại bất thường: Thiếu trường dữ liệu
- Bằng chứng: Nhận diện được: {'site_code': 'Biểu mẫu 01: Phân loại trạm ưu tiên kiên cố củng cố', 'priority': 'Biểu mẫu 01: Phân loại trạm ưu tiên kiên cố củng cố', 'staff': 'Unnamed: 20', 'cutoff': 'Unnamed: 24', 'flood': 'Unnamed: 25'}
- Khoảng thiếu/rủi ro: Thiếu/không nhận diện: ats, generator_plan, battery_hours
- Khuyến nghị: Bổ sung mapping cột hoặc đổi header theo mẫu rule

### 439. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/14
- Vị trí ô: **U14** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 7: ngập=, chia cắt=1, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 440. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/143
- Vị trí ô: **U143** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 136: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 441. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/144
- Vị trí ô: **U144** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 137: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 442. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/145
- Vị trí ô: **U145** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 138: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 443. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/146
- Vị trí ô: **U146** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 139: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 444. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/147
- Vị trí ô: **U147** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 140: ngập=1, chia cắt=1, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 445. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/148
- Vị trí ô: **U148** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 141: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 446. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/149
- Vị trí ô: **U149** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 142: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 447. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/150
- Vị trí ô: **U150** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 143: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 448. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/151
- Vị trí ô: **U151** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 144: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 449. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/152
- Vị trí ô: **U152** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 145: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 450. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/153
- Vị trí ô: **U153** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 146: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 451. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/154
- Vị trí ô: **U154** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 147: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 452. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/155
- Vị trí ô: **U155** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 148: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 453. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/156
- Vị trí ô: **U156** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 149: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 454. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/157
- Vị trí ô: **U157** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 150: ngập=1, chia cắt=1, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 455. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/158
- Vị trí ô: **U158** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 151: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 456. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/159
- Vị trí ô: **U159** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 152: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 457. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/160
- Vị trí ô: **U160** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 153: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 458. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/161
- Vị trí ô: **U161** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 154: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 459. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/162
- Vị trí ô: **U162** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 155: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 460. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/163
- Vị trí ô: **U163** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 156: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 461. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/164
- Vị trí ô: **U164** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 157: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 462. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/165
- Vị trí ô: **U165** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 158: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 463. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/166
- Vị trí ô: **U166** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 159: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 464. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/167
- Vị trí ô: **U167** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 160: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 465. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/168
- Vị trí ô: **U168** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 161: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 466. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/169
- Vị trí ô: **U169** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 162: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 467. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/170
- Vị trí ô: **U170** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 163: ngập=1, chia cắt=1, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 468. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/171
- Vị trí ô: **U171** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 164: ngập=1, chia cắt=1, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 469. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/172
- Vị trí ô: **U172** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 165: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 470. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/173
- Vị trí ô: **U173** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 166: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 471. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/174
- Vị trí ô: **U174** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 167: ngập=1, chia cắt=1, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 472. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/175
- Vị trí ô: **U175** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 168: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 473. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/176
- Vị trí ô: **U176** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 169: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 474. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/177
- Vị trí ô: **U177** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 170: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 475. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/178
- Vị trí ô: **U178** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 171: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 476. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/179
- Vị trí ô: **U179** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 172: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 477. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/180
- Vị trí ô: **U180** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 173: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 478. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/181
- Vị trí ô: **U181** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 174: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 479. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/182
- Vị trí ô: **U182** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 175: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 480. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/183
- Vị trí ô: **U183** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 176: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 481. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/184
- Vị trí ô: **U184** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 177: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 482. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/185
- Vị trí ô: **U185** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 178: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 483. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/186
- Vị trí ô: **U186** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 179: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 484. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/187
- Vị trí ô: **U187** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 180: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 485. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/188
- Vị trí ô: **U188** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 181: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 486. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/189
- Vị trí ô: **U189** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 182: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 487. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/190
- Vị trí ô: **U190** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 183: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 488. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/191
- Vị trí ô: **U191** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 184: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 489. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/192
- Vị trí ô: **U192** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 185: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 490. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/193
- Vị trí ô: **U193** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 186: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 491. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/194
- Vị trí ô: **U194** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 187: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 492. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/195
- Vị trí ô: **U195** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 188: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 493. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/196
- Vị trí ô: **U196** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 189: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 494. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/197
- Vị trí ô: **U197** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 190: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 495. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/198
- Vị trí ô: **U198** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 191: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 496. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/199
- Vị trí ô: **U199** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 192: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 497. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/200
- Vị trí ô: **U200** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 193: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 498. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/201
- Vị trí ô: **U201** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 194: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 499. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/202
- Vị trí ô: **U202** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 195: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 500. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/203
- Vị trí ô: **U203** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 196: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 501. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/204
- Vị trí ô: **U204** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 197: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 502. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/205
- Vị trí ô: **U205** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 198: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 503. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/206
- Vị trí ô: **U206** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 199: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 504. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/207
- Vị trí ô: **U207** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 200: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 505. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/208
- Vị trí ô: **U208** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 201: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 506. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/209
- Vị trí ô: **U209** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 202: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 507. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/210
- Vị trí ô: **U210** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 203: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 508. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/211
- Vị trí ô: **U211** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 204: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 509. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/212
- Vị trí ô: **U212** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 205: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 510. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/213
- Vị trí ô: **U213** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 206: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 511. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/214
- Vị trí ô: **U214** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 207: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 512. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/215
- Vị trí ô: **U215** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 208: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 513. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/216
- Vị trí ô: **U216** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 209: ngập=1, chia cắt=1, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 514. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/217
- Vị trí ô: **U217** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 210: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 515. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/218
- Vị trí ô: **U218** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 211: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 516. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/219
- Vị trí ô: **U219** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 212: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 517. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/220
- Vị trí ô: **U220** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 213: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 518. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/221
- Vị trí ô: **U221** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 214: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 519. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/222
- Vị trí ô: **U222** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 215: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 520. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/223
- Vị trí ô: **U223** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 216: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 521. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/224
- Vị trí ô: **U224** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 217: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 522. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/225
- Vị trí ô: **U225** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 218: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 523. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/226
- Vị trí ô: **U226** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 219: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 524. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/227
- Vị trí ô: **U227** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 220: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 525. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/228
- Vị trí ô: **U228** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 221: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 526. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/229
- Vị trí ô: **U229** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 222: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 527. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/230
- Vị trí ô: **U230** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 223: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 528. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/231
- Vị trí ô: **U231** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 224: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 529. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/232
- Vị trí ô: **U232** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 225: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 530. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/233
- Vị trí ô: **U233** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 226: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 531. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/234
- Vị trí ô: **U234** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 227: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 532. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/235
- Vị trí ô: **U235** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 228: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 533. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/236
- Vị trí ô: **U236** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 229: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 534. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/237
- Vị trí ô: **U237** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 230: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 535. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/238
- Vị trí ô: **U238** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 231: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 536. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/239
- Vị trí ô: **U239** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 232: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 537. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/240
- Vị trí ô: **U240** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 233: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 538. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/241
- Vị trí ô: **U241** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 234: ngập=1, chia cắt=1, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 539. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/242
- Vị trí ô: **U242** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 235: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 540. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/243
- Vị trí ô: **U243** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 236: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 541. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/244
- Vị trí ô: **U244** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 237: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 542. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/245
- Vị trí ô: **U245** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 238: ngập=1, chia cắt=1, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 543. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/246
- Vị trí ô: **U246** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 239: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 544. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/247
- Vị trí ô: **U247** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 240: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 545. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/249
- Vị trí ô: **U249** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 242: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 546. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/250
- Vị trí ô: **U250** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 243: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 547. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/251
- Vị trí ô: **U251** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 244: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 548. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/252
- Vị trí ô: **U252** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 245: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 549. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/253
- Vị trí ô: **U253** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 246: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 550. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/254
- Vị trí ô: **U254** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 247: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 551. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/255
- Vị trí ô: **U255** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 248: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 552. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/256
- Vị trí ô: **U256** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 249: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 553. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/257
- Vị trí ô: **U257** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 250: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 554. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/258
- Vị trí ô: **U258** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 251: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 555. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/259
- Vị trí ô: **U259** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 252: ngập=1, chia cắt=1, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 556. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/260
- Vị trí ô: **U260** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 253: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 557. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/261
- Vị trí ô: **U261** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 254: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 558. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/262
- Vị trí ô: **U262** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 255: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 559. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/263
- Vị trí ô: **U263** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 256: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 560. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/264
- Vị trí ô: **U264** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 257: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 561. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/265
- Vị trí ô: **U265** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 258: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 562. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/266
- Vị trí ô: **U266** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 259: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 563. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/267
- Vị trí ô: **U267** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 260: ngập=1, chia cắt=1, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 564. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/268
- Vị trí ô: **U268** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 261: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 565. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/269
- Vị trí ô: **U269** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 262: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 566. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/270
- Vị trí ô: **U270** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 263: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 567. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/271
- Vị trí ô: **U271** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 264: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 568. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/272
- Vị trí ô: **U272** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 265: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 569. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/273
- Vị trí ô: **U273** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 266: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 570. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/274
- Vị trí ô: **U274** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 267: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 571. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/275
- Vị trí ô: **U275** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 268: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 572. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/276
- Vị trí ô: **U276** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 269: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 573. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/277
- Vị trí ô: **U277** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 270: ngập=1, chia cắt=1, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 574. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/278
- Vị trí ô: **U278** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 271: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 575. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/279
- Vị trí ô: **U279** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 272: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 576. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/280
- Vị trí ô: **U280** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 273: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 577. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/281
- Vị trí ô: **U281** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 274: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 578. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/282
- Vị trí ô: **U282** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 275: ngập=1, chia cắt=1, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 579. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/283
- Vị trí ô: **U283** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 276: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 580. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/284
- Vị trí ô: **U284** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 277: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 581. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/285
- Vị trí ô: **U285** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 278: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 582. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/286
- Vị trí ô: **U286** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 279: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 583. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/287
- Vị trí ô: **U287** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 280: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 584. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/288
- Vị trí ô: **U288** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 281: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 585. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/289
- Vị trí ô: **U289** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 282: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 586. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/290
- Vị trí ô: **U290** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 283: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 587. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/291
- Vị trí ô: **U291** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 284: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 588. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/292
- Vị trí ô: **U292** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 285: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 589. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/293
- Vị trí ô: **U293** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 286: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 590. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/294
- Vị trí ô: **U294** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 287: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 591. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/295
- Vị trí ô: **U295** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 288: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 592. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/296
- Vị trí ô: **U296** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 289: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 593. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/297
- Vị trí ô: **U297** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 290: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 594. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/298
- Vị trí ô: **U298** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 291: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 595. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/299
- Vị trí ô: **U299** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 292: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 596. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/300
- Vị trí ô: **U300** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 293: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 597. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/301
- Vị trí ô: **U301** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 294: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 598. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/302
- Vị trí ô: **U302** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 295: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 599. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/303
- Vị trí ô: **U303** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 296: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 600. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/304
- Vị trí ô: **U304** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 297: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 601. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/305
- Vị trí ô: **U305** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 298: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 602. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/306
- Vị trí ô: **U306** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 299: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 603. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/307
- Vị trí ô: **U307** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 300: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 604. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/308
- Vị trí ô: **U308** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 301: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 605. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/309
- Vị trí ô: **U309** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 302: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 606. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/310
- Vị trí ô: **U310** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 303: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 607. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/311
- Vị trí ô: **U311** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 304: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 608. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/312
- Vị trí ô: **U312** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 305: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 609. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/313
- Vị trí ô: **U313** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 306: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 610. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/314
- Vị trí ô: **U314** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 307: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 611. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/315
- Vị trí ô: **U315** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 308: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 612. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/316
- Vị trí ô: **U316** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 309: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 613. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/317
- Vị trí ô: **U317** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 310: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 614. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/318
- Vị trí ô: **U318** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 311: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 615. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/319
- Vị trí ô: **U319** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 312: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 616. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/320
- Vị trí ô: **U320** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 313: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 617. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/321
- Vị trí ô: **U321** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 314: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 618. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/322
- Vị trí ô: **U322** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 315: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 619. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/323
- Vị trí ô: **U323** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 316: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 620. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/324
- Vị trí ô: **U324** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 317: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 621. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/325
- Vị trí ô: **U325** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 318: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 622. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/326
- Vị trí ô: **U326** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 319: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 623. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/327
- Vị trí ô: **U327** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 320: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 624. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/328
- Vị trí ô: **U328** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 321: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 625. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/329
- Vị trí ô: **U329** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 322: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 626. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/330
- Vị trí ô: **U330** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 323: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 627. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/331
- Vị trí ô: **U331** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 324: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 628. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/332
- Vị trí ô: **U332** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 325: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 629. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/333
- Vị trí ô: **U333** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 326: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 630. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/334
- Vị trí ô: **U334** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 327: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 631. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/335
- Vị trí ô: **U335** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 328: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 632. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/336
- Vị trí ô: **U336** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 329: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 633. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/337
- Vị trí ô: **U337** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 330: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 634. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/338
- Vị trí ô: **U338** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 331: ngập=1, chia cắt=1, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 635. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/339
- Vị trí ô: **U339** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 332: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 636. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/340
- Vị trí ô: **U340** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 333: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 637. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/341
- Vị trí ô: **U341** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 334: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 638. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/342
- Vị trí ô: **U342** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 335: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 639. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/343
- Vị trí ô: **U343** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 336: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 640. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/344
- Vị trí ô: **U344** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 337: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 641. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/345
- Vị trí ô: **U345** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 338: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 642. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/346
- Vị trí ô: **U346** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 339: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 643. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/347
- Vị trí ô: **U347** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 340: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 644. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/348
- Vị trí ô: **U348** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 341: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 645. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/349
- Vị trí ô: **U349** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 342: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 646. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/350
- Vị trí ô: **U350** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 343: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 647. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/351
- Vị trí ô: **U351** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 344: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 648. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/352
- Vị trí ô: **U352** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 345: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 649. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/353
- Vị trí ô: **U353** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 346: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 650. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/354
- Vị trí ô: **U354** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 347: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 651. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/355
- Vị trí ô: **U355** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 348: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 652. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/356
- Vị trí ô: **U356** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 349: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 653. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/357
- Vị trí ô: **U357** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 350: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 654. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/358
- Vị trí ô: **U358** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 351: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 655. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1200
- Vị trí ô: **U1200** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1193: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 656. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1218
- Vị trí ô: **U1218** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1211: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 657. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1224
- Vị trí ô: **U1224** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1217: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 658. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1229
- Vị trí ô: **U1229** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1222: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 659. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1231
- Vị trí ô: **U1231** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1224: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 660. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1235
- Vị trí ô: **U1235** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1228: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 661. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1245
- Vị trí ô: **U1245** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1238: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 662. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1250
- Vị trí ô: **U1250** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1243: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 663. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1254
- Vị trí ô: **U1254** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1247: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 664. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1264
- Vị trí ô: **U1264** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1257: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 665. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1293
- Vị trí ô: **U1293** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1286: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 666. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1324
- Vị trí ô: **U1324** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1317: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 667. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1329
- Vị trí ô: **U1329** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1322: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 668. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1336
- Vị trí ô: **U1336** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1329: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 669. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1340
- Vị trí ô: **U1340** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1333: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 670. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1342
- Vị trí ô: **U1342** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1335: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 671. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1349
- Vị trí ô: **U1349** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1342: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 672. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1352
- Vị trí ô: **U1352** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1345: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 673. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1357
- Vị trí ô: **U1357** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1350: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 674. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1362
- Vị trí ô: **U1362** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1355: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 675. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1372
- Vị trí ô: **U1372** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1365: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 676. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1375
- Vị trí ô: **U1375** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1368: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 677. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1381
- Vị trí ô: **U1381** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1374: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 678. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1382
- Vị trí ô: **U1382** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1375: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 679. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1441
- Vị trí ô: **U1441** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1434: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 680. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1451
- Vị trí ô: **U1451** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1444: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 681. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1454
- Vị trí ô: **U1454** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1447: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 682. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1476
- Vị trí ô: **U1476** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1469: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 683. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1492
- Vị trí ô: **U1492** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1485: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 684. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1501
- Vị trí ô: **U1501** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1494: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 685. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1504
- Vị trí ô: **U1504** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1497: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 686. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1527
- Vị trí ô: **U1527** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1520: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 687. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1533
- Vị trí ô: **U1533** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1526: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 688. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1534
- Vị trí ô: **U1534** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1527: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 689. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1557
- Vị trí ô: **U1557** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1550: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 690. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1568
- Vị trí ô: **U1568** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1561: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 691. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1577
- Vị trí ô: **U1577** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1570: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 692. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1584
- Vị trí ô: **U1584** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1577: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 693. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1585
- Vị trí ô: **U1585** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1578: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 694. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1591
- Vị trí ô: **U1591** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1584: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 695. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1606
- Vị trí ô: **U1606** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1599: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 696. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1618
- Vị trí ô: **U1618** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1611: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 697. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1639
- Vị trí ô: **U1639** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1632: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 698. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1643
- Vị trí ô: **U1643** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1636: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 699. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1647
- Vị trí ô: **U1647** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1640: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 700. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1656
- Vị trí ô: **U1656** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1649: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 701. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1691
- Vị trí ô: **U1691** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1684: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 702. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1694
- Vị trí ô: **U1694** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1687: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 703. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1696
- Vị trí ô: **U1696** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1689: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 704. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1699
- Vị trí ô: **U1699** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1692: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 705. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1706
- Vị trí ô: **U1706** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1699: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 706. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1724
- Vị trí ô: **U1724** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1717: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 707. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1731
- Vị trí ô: **U1731** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1724: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 708. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1764
- Vị trí ô: **U1764** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1757: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 709. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1776
- Vị trí ô: **U1776** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1769: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 710. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1781
- Vị trí ô: **U1781** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1774: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 711. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1791
- Vị trí ô: **U1791** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1784: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 712. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1793
- Vị trí ô: **U1793** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1786: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 713. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/1821
- Vị trí ô: **U1821** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 1814: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 714. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/2083
- Vị trí ô: **U2083** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 2076: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 715. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/2087
- Vị trí ô: **U2087** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 2080: ngập=, chia cắt=1, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 716. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/2091
- Vị trí ô: **U2091** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 2084: ngập=, chia cắt=1, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 717. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/2092
- Vị trí ô: **U2092** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 2085: ngập=, chia cắt=1, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 718. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/2093
- Vị trí ô: **U2093** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 2086: ngập=, chia cắt=1, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 719. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/2094
- Vị trí ô: **U2094** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 2087: ngập=, chia cắt=1, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 720. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/2095
- Vị trí ô: **U2095** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 2088: ngập=, chia cắt=1, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 721. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/2096
- Vị trí ô: **U2096** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 2089: ngập=, chia cắt=1, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 722. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/2097
- Vị trí ô: **U2097** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 2090: ngập=, chia cắt=1, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 723. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/2098
- Vị trí ô: **U2098** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 2091: ngập=, chia cắt=1, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 724. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/2099
- Vị trí ô: **U2099** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 2092: ngập=, chia cắt=1, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 725. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/2100
- Vị trí ô: **U2100** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 2093: ngập=, chia cắt=1, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 726. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/2101
- Vị trí ô: **U2101** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 2094: ngập=, chia cắt=1, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 727. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/2102
- Vị trí ô: **U2102** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 2095: ngập=, chia cắt=1, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 728. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/2103
- Vị trí ô: **U2103** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 2096: ngập=, chia cắt=1, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 729. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/2104
- Vị trí ô: **U2104** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 2097: ngập=, chia cắt=1, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 730. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/2105
- Vị trí ô: **U2105** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 2098: ngập=, chia cắt=1, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 731. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/2113
- Vị trí ô: **U2113** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 2106: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 732. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/2148
- Vị trí ô: **U2148** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 2141: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 733. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/2490
- Vị trí ô: **U2490** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 2483: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 734. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/2645
- Vị trí ô: **U2645** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 2638: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 735. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/2667
- Vị trí ô: **U2667** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 2660: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 736. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/2676
- Vị trí ô: **U2676** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 2669: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 737. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/2695
- Vị trí ô: **U2695** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 2688: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 738. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/2808
- Vị trí ô: **U2808** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 2801: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 739. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/2869
- Vị trí ô: **U2869** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 2862: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 740. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/2922
- Vị trí ô: **U2922** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 2915: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 741. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/2938
- Vị trí ô: **U2938** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 2931: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 742. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/3038
- Vị trí ô: **U3038** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 3031: ngập=, chia cắt=1H, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 743. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/3114
- Vị trí ô: **U3114** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 3107: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 744. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/3122
- Vị trí ô: **U3122** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 3115: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 745. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/3128
- Vị trí ô: **U3128** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 3121: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 746. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/3132
- Vị trí ô: **U3132** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 3125: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 747. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/3147
- Vị trí ô: **U3147** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 3140: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 748. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/3161
- Vị trí ô: **U3161** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 3154: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 749. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/3197
- Vị trí ô: **U3197** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 3190: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 750. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/3203
- Vị trí ô: **U3203** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 3196: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 751. Trạm ngập/chia cắt phải có phương án ém quân
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DAT** | Mức độ: **CRITICAL**
- Nguồn: Sample.xlsx/BM01_tramUT.VT/3206
- Vị trí ô: **U3206** | Cột: U | Giá trị: 
- Loại bất thường: Thiếu PA ém quân
- Bằng chứng: 3199: ngập=1, chia cắt=, nhân sự trống
- Khoảng thiếu/rủi ro: Không có lực lượng tại chỗ khi thiên tai
- Khuyến nghị: Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS

### 752. Đủ trường dữ liệu tối thiểu
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/TramBKK MPD
- Loại bất thường: Thiếu trường dữ liệu
- Bằng chứng: Nhận diện được: {'generator_plan': 'Lịch sử BKK không chạy được MPĐ'}
- Khoảng thiếu/rủi ro: Thiếu/không nhận diện: site_code, priority, staff, flood, cutoff, ats, battery_hours
- Khuyến nghị: Bổ sung mapping cột hoặc đổi header theo mẫu rule

### 753. Đủ trường dữ liệu tối thiểu
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/Quiz
- Loại bất thường: Thiếu trường dữ liệu
- Bằng chứng: Nhận diện được: {'battery_hours': 'TT'}
- Khoảng thiếu/rủi ro: Thiếu/không nhận diện: site_code, priority, staff, flood, cutoff, ats, generator_plan
- Khuyến nghị: Bổ sung mapping cột hoặc đổi header theo mẫu rule

### 754. Đủ trường dữ liệu tối thiểu
- Nhóm rule: CSDL BTS
- Kết quả: **CAN_BO_SUNG** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/T9.TTr tinh node
- Loại bất thường: Thiếu trường dữ liệu
- Bằng chứng: Nhận diện được: {'site_code': 'Trạm', 'priority': 'Trạm'}
- Khoảng thiếu/rủi ro: Thiếu/không nhận diện: staff, flood, cutoff, ats, generator_plan, battery_hours
- Khuyến nghị: Bổ sung mapping cột hoặc đổi header theo mẫu rule

### 755. Nhận diện cột dữ liệu
- Nhóm rule: CSDL BTS
- Kết quả: **KHONG_DU_DU_LIEU** | Mức độ: **MEDIUM**
- Nguồn: Sample.xlsx/119b vali Kh0 2 cap QBH QTI
- Loại bất thường: Thiếu mapping/header
- Bằng chứng: Sample.xlsx/119b vali Kh0 2 cap QBH QTI: không nhận diện được cột chuẩn
- Khoảng thiếu/rủi ro: Thiếu header hoặc header không rõ
- Khuyến nghị: Chuẩn hóa header hoặc mapping cột trong file CSDL

## 3. Hướng xử lý ưu tiên

1. Xử lý ngay các lỗi CRITICAL/HIGH trước khi phê duyệt phương án.
2. Cập nhật phụ lục nhân sự ém quân, SĐT, vị trí, thời gian tiếp cận và danh sách MPĐ.
3. Rà soát lại CSDL trạm có nguy cơ ngập/chia cắt và trạm TGX ắc quy thấp.

## Đánh giá theo từng mục rule

| rule_source      | rule_group   | rule_name                                        | status      |   so_loi |   so_bat_thuong | o_du_lieu_lien_quan                                                                                                                                                                                                                           | khuyen_nghi                                                      |
|:-----------------|:-------------|:-------------------------------------------------|:------------|---------:|----------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------|
| Rule engine CSDL | CSDL BTS     | 100% trạm UT1/UT1_3321 phải có nhân sự ém quân   | KHONG_DAT   |        3 |               3 | U4, U52, U59                                                                                                                                                                                                                                  | Bổ sung họ tên, SĐT, vị trí ém quân và ca trực                   |
| Rule engine CSDL | CSDL BTS     | Nhận diện cột dữ liệu                            | CAN_BO_SUNG |        0 |               2 |                                                                                                                                                                                                                                               | Chuẩn hóa header hoặc mapping cột trong file CSDL                |
| Rule engine CSDL | CSDL BTS     | Thời gian xả ắc quy không được bất thường bằng 0 | CAN_BO_SUNG |        0 |             302 | AP10, AP1000, AP1010, AP1012, AP1027, AP1028, AP1039, AP1045, AP1046, AP1058, AP1061, AP1068, AP107, AP1081, AP1088, AP1095, AP1096, AP11, AP1104, AP1110, AP1114, AP1120, AP1124, AP1127, AP1129, AP1132, AP1138, AP1140, AP1145, AP1146 ... | Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy        |
| Rule engine CSDL | CSDL BTS     | Trạm ngập/chia cắt phải có phương án ém quân     | KHONG_DAT   |      426 |             426 | AU10, AU11, AU12, AU13, AU14, AU2, AU3, AU4, AU5, AU7, AU8, AU9, DH5, U10, U11, U12, U1200, U1218, U1224, U1229, U1231, U1235, U1245, U1250, U1254, U1264, U1293, U13, U1324, U1329 ...                                                       | Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS |
| Rule engine CSDL | CSDL BTS     | Đủ trường dữ liệu tối thiểu                      | CAN_BO_SUNG |        0 |              22 |                                                                                                                                                                                                                                               | Bổ sung mapping cột hoặc đổi header theo mẫu rule                |