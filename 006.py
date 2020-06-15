def Trim(arg1, arg2 = 10, arg3 = '...'):
        text = arg1 
        return text[0:arg2] + arg3

tulisanPanjang = Trim("ini adalah tulisan yang sangat panjang",8)
print(tulisanPanjang)
