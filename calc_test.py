import pytest
from calc_functions import *

# Gunakan pytest untuk menulis pengujian unit untuk fungsi-fungsi yang telah Anda buat. 
'''
Buat pengujian yang mencakup skenario berikut:
• Pengujian untuk setiap fungsi dengan argumen positif.
• Pengujian untuk setiap fungsi dengan argumen negatif.
• Pengujian untuk setiap fungsi dengan argumen nol.
• Pengujian untuk kasus khusus, seperti hasil penjumlahan nol, hasil perkalian nol, dan lain-lain.
• Pastikan pengujian menguji kasus yang beragam dan memeriksa apakah fungsi-fungsi Anda menghasilkan output yang benar
'''
'''
Buatlah sebuah fixture yang menghasilkan data input yang berbeda untuk pengujian Anda. 
Anda bisa menggunakan parameterisasi fixture untuk menguji berbagai kombinasi input.
• Terapkan marker pada pengujian Anda untuk mengkategorikan mereka. Misalnya, Anda 
dapat menggunakan marker ”tambahkurang" untuk pengujian yang berkaitan dengan
operasi penjumlahan dan pengurangan. Dan marker “kalibagi” untuk operasi perkalian dan 
pembagian. Anda juga dapat menambahkan deskripsi singkat pada marker tersebut. 
• Pelaporan: Buat sebuah dokumen atau laporan yang mencakup hasil pengujian Anda, 
termasuk hasil dari pytest. Jelaskan pengujian apa yang telah Anda lakukan dan apa yang 
Anda pelajari dari hasilnya
'''

@pytest.fixture(params=[(2,3),(0,0),(-1,1),(-1,-1),(100,-100)])
def input_data(request):
    return request.param

@pytest.mark.tambahkurang
def test_add_positif(input_data):
    x,y = input_data
    result = add(x,y)
    assert result > 0


@pytest.mark.tambahkurang
def test_add_negatif(input_data):
    x,y = input_data
    result = add(x,y)
    assert result < 0

@pytest.mark.tambahkurang
def test_add_nol(input_data):
    x,y = input_data
    result = add(x,y)
    assert result == 0

@pytest.mark.tambahkurang
def test_subtract_positif(input_data):
    x,y = input_data
    result = subtract(x,y)
    assert result > 0


@pytest.mark.tambahkurang
def test_subtract_negatif(input_data):
    x,y = input_data
    result = subtract(x,y)
    assert result < 0

@pytest.mark.tambahkurang
def test_subtract_nol(input_data):
    x,y = input_data
    result = add(x,y)
    assert result == 0


