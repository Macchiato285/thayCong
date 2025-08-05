Mô tả bài toán
Ứng dụng App1 là một phần trong hệ thống web quản lý sinh viên. Mục tiêu của App1 là thêm và lưu thông tin sinh viên vào cơ sở dữ liệu SQL Server thông qua giao diện web. Mỗi sinh viên sẽ được gán vào một lớp cụ thể.
Công nghệ và ngôn ngữ sử dụng
Ngôn ngữ: Python 3
Framework web: Flask
Cơ sở dữ liệu: SQL Server (sử dụng ODBC để kết nối)
Thư viện kết nối SQL Server: pyodbc
Giao diện web: HTML + CSS (sử dụng Jinja2 template của Flask)
Các chức năng chính
Hiển thị form thêm sinh viên
Gửi dữ liệu sinh viên từ form đến backend Flask
Lưu thông tin sinh viên vào SQL Server (các bảng Student, Class, StudentClass)
Hiển thị thông báo khi thêm thành công hoặc thất bại
Một số giao diện cơ bản
Trang web khi chạy sẽ tự động mở trang "Thêm sinh viên"
Form bao gồm:
Mã sinh viên
Họ tên
Mã lớp
Giao diện đơn giản, dễ thao tác, phản hồi rõ ràng sau khi gửi
