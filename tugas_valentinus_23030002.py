import shutil

def tampilkan_penggunaan_hdd():
    # Mendapatkan informasi penggunaan disk
    total, digunakan, gratis = shutil.disk_usage("/")
    
    # Konversi ke GB untuk lebih mudah dibaca
    total_gb = total / (2**30)
    digunakan_gb = digunakan / (2**30)
    gratis_gb = gratis / (2**30)
    
    # Menghitung persentase penggunaan
    persentase = (digunakan / total) * 100
    
    # Menampilkan hasil
    print("\n=== Informasi Penggunaan Hard Disk (HDD) ===")
    print(f"Total penyimpanan: {total_gb:.2f} GB")
    print(f"Digunakan: {digunakan_gb:.2f} GB")
    print(f"Tersedia: {gratis_gb:.2f} GB")
    print(f"Persentase digunakan: {persentase:.1f}%")
    
    # Memberikan pesan sederhana berdasarkan persentase penggunaan
    if persentase > 90:
        print("\n⚠️ Peringatan: Penyimpanan hampir penuh!")
    elif persentase > 70:
        print("\nℹ️ Info: Penyimpanan sudah lebih dari 70% terisi")
    else:
        print("\n✅ Penyimpanan masih cukup")

# Memanggil fungsi
if __name__ == "__main__":
    tampilkan_penggunaan_hdd()