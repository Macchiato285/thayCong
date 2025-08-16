import pandas as pd
import tkinter as tk
from tkinter import messagebox
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# 1. Đọc dữ liệu
df = pd.read_csv("Iris.csv")
X = df.drop(["Id", "Species"], axis=1)
y = df["Species"]

# 2. Chia train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 3. Huấn luyện mô hình
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# 4. Tạo cửa sổ Tkinter
root = tk.Tk()
root.title("🌸 Dự đoán loài hoa Iris (KNN)")
root.geometry("400x300")

# Nhãn hướng dẫn
tk.Label(root, text="Nhập thông số hoa Iris:", font=("Arial", 12, "bold")).pack(pady=10)

# Các ô nhập
entries = {}
fields = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"]
for f in fields:
    frame = tk.Frame(root)
    frame.pack(pady=5)
    tk.Label(frame, text=f"{f} (cm):", width=15, anchor="w").pack(side=tk.LEFT)
    entry = tk.Entry(frame)
    entry.pack(side=tk.LEFT)
    entries[f] = entry

# Hàm dự đoán
def predict():
    try:
        sl = float(entries["Sepal Length"].get())
        sw = float(entries["Sepal Width"].get())
        pl = float(entries["Petal Length"].get())
        pw = float(entries["Petal Width"].get())
        sample = [[sl, sw, pl, pw]]
        pred = knn.predict(sample)
        messagebox.showinfo("Kết quả dự đoán", f"🌼 Loài hoa dự đoán: {pred[0]}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ!")

# Nút dự đoán
tk.Button(root, text="Dự đoán", command=predict, bg="lightblue").pack(pady=15)

# Hiển thị độ chính xác
y_pred = knn.predict(X_test)
acc = accuracy_score(y_test, y_pred)
tk.Label(root, text=f"🎯 Độ chính xác mô hình: {acc*100:.2f}%", fg="green").pack()

root.mainloop()
