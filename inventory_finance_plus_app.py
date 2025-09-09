import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

DB_FILE = "inventory_finance_plus.db"

def show_products():
    conn = sqlite3.connect(DB_FILE)
    df = pd.read_sql("SELECT * FROM products", conn)
    print("\n=== Data Produk ===")
    print(df)
    conn.close()

def show_purchases():
    conn = sqlite3.connect(DB_FILE)
    df = pd.read_sql("SELECT * FROM purchases", conn)
    print("\n=== Barang Masuk ===")
    print(df)
    conn.close()

def show_sales():
    conn = sqlite3.connect(DB_FILE)
    df = pd.read_sql("SELECT * FROM sales", conn)
    print("\n=== Barang Keluar ===")
    print(df)
    conn.close()

def show_report():
    conn = sqlite3.connect(DB_FILE)
    df_sales = pd.read_sql("SELECT * FROM sales", conn)
    if not df_sales.empty:
        total_sales = (df_sales['qty'] * df_sales['price']).sum()
    else:
        total_sales = 0

    df_purchases = pd.read_sql("SELECT * FROM purchases", conn)
    if not df_purchases.empty:
        total_purchases = (df_purchases['qty'] * df_purchases['cost']).sum()
    else:
        total_purchases = 0

    profit = total_sales - total_purchases

    print("\n=== Laporan Keuangan ===")
    print(f"Total Penjualan : {total_sales}")
    print(f"Total Pembelian : {total_purchases}")
    print(f"Keuntungan      : {profit}")

    # Grafik
    plt.bar(['Penjualan', 'Pembelian', 'Keuntungan'], [total_sales, total_purchases, profit])
    plt.title("Grafik Keuangan")
    plt.show()

    conn.close()

if __name__ == "__main__":
    while True:
        print("\n=== MENU INVENTORY ===")
        print("1. Lihat Produk")
        print("2. Barang Masuk")
        print("3. Barang Keluar")
        print("4. Laporan Keuangan + Grafik")
        print("0. Keluar")

        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            show_products()
        elif pilihan == "2":
            show_purchases()
        elif pilihan == "3":
            show_sales()
        elif pilihan == "4":
            show_report()
        elif pilihan == "0":
            break
        else:
            print("Menu tidak valid!")
