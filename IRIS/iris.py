import pandas as pd
import streamlit as st
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

# 3. Huấn luyện mô hình KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# 4. Giao diện Streamlit
st.title("🌸 Dự đoán loài hoa Iris bằng KNN")

# Hiển thị độ chính xác
y_pred = knn.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
st.write(f"🎯 Độ chính xác mô hình: **{accuracy*100:.2f}%**")

# Form nhập thông số
st.subheader("🔍 Nhập thông số hoa để dự đoán:")
sl = st.number_input("Sepal Length (cm)", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
sw = st.number_input("Sepal Width (cm)", min_value=0.0, max_value=10.0, value=3.0, step=0.1)
pl = st.number_input("Petal Length (cm)", min_value=0.0, max_value=10.0, value=4.0, step=0.1)
pw = st.number_input("Petal Width (cm)", min_value=0.0, max_value=10.0, value=1.0, step=0.1)

if st.button("🌼 Dự đoán"):
    sample = [[sl, sw, pl, pw]]
    prediction = knn.predict(sample)
    st.success(f"👉 Loài hoa dự đoán: **{prediction[0]}**")
