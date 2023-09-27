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
# def test_add():
#     assert add(1,2) == 3
#     assert add(-1, 0) == -1
#     assert add(0,0) == 0

# def test_subtract():
#     assert subtract(8,5) == 3
#     assert subtract(-2,3) == -5
#     assert subtract(2,2) == 5
# # subtract = 0 salah
    
# def test_multiply():
#     assert multiply(2,5) == 10
#     assert multiply(-9,2) == -18
#     assert multiply(2,0) == 0
    
# def test_div():
#     assert div(10,5) == 2
#     assert div(8,-4) == -2
#     assert div(0,5) == 0

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
@pytest.fixture(params=[(5,3),(4,0),(-1,1),(-3,-3),(0,0),(-8,2),(0,7)])
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