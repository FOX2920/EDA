import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io

def main():
    # Initialize data variable
    data = None
    st.title("Khám phá dữ liệu")
    # Upload file dữ liệu
    file = st.file_uploader("Chọn tệp dữ liệu (CSV/Excel)", type=["csv", "xlsx"])
    if file is not None:
        data = pd.read_csv(file)  # or pd.read_excel(file) for Excel files

    # Check if data is available before displaying
    if data is not None:
        # Hiển thị dữ liệu
        st.header("Show data")
        st.dataframe(data.head())

        # Thống kê mô tả dữ liệu
        st.table(data.describe())

        # Mô tả các thuộc tính
        st.header("Show data info")
        buffer = io.StringIO()
        data.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)
        st.header("Show data visualization")
        # Vẽ biểu đồ histogram biểu diễn sự phân bố giá trị của các thuộc tính
        for col in data.columns:
            st.write(f"Biểu đồ histogram cho thuộc tính {col}")
            fig, ax = plt.subplots()
            ax.hist(data[col], bins=20)
            plt.xlabel(col)
            plt.ylabel('Quantity')
            st.pyplot(fig)
        # Tính hệ số tương quan giữa các thuộc tính
        st.header('Biểu đồ Ma trận tương quan')
        fig, ax = plt.subplots()
        sns.heatmap(data.corr(method = 'pearson'), cmap="Blues", annot=True, ax=ax, vmax=1, square=True)
        st.write(fig)
        # Chọn biến phụ thuộc và vẽ biểu đồ phân tán biểu diễn mối liên hệ giữa biến phụ thuộc và từng biến độc lập
        y = st.selectbox("Chọn biến phụ thuộc", data.columns)
        for x in data.columns:
            if x != y:
                fig, ax = plt.subplots()
                ax.scatter(data[x], data[y])
                ax.set_xlabel(f"{x}")
                ax.set_ylabel(f"{y}")
                st.write(f"Biểu đồ phân tán cho biến phụ thuộc {y} và biến độc lập {x}")
                st.pyplot(fig)
    else:
        st.warning("Hãy chọn một tệp dữ liệu CSV hoặc Excel dưới 500KB để xem và phân tích.")

if __name__ == "__main__":
    main()
