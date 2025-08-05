from flask import Flask, request, jsonify, render_template
import pyodbc

app = Flask(__name__)

# Kết nối SQL Server
conn_str = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=localhost;"
    "Database=sinhvien;"
    "Trusted_Connection=yes;"
)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Trang giao diện chính
@app.route("/", methods=["GET"])
def index():
    return render_template("add_student.html")

# API thêm sinh viên
@app.route("/add-student", methods=["POST"])
def add_student():
    try:
        data = request.get_json()
        student_id = data.get('student_id')
        full_name = data.get('full_name')
        class_id = data.get('class_id')

        # Kiểm tra sinh viên đã tồn tại
        cursor.execute("SELECT * FROM Student WHERE StudentID = ?", (student_id,))
        if cursor.fetchone():
            return jsonify({"error": "Sinh viên đã tồn tại"}), 400

        # Thêm lớp nếu chưa có
        cursor.execute("SELECT * FROM Class WHERE ClassID = ?", (class_id,))
        if not cursor.fetchone():
            cursor.execute("INSERT INTO Class (ClassID, ClassName) VALUES (?, ?)", (class_id, f"Lớp {class_id}"))

        # Thêm sinh viên và liên kết lớp
        cursor.execute("INSERT INTO Student (StudentID, FullName) VALUES (?, ?)", (student_id, full_name))
        cursor.execute("INSERT INTO StudentClass (StudentID, ClassID) VALUES (?, ?)", (student_id, class_id))
        conn.commit()

        return jsonify({"message": "Thêm sinh viên thành công!"}), 200

    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
