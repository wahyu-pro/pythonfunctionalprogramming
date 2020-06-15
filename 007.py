def TrimWords(arg1, arg2 = 5):
        text = arg1.split()
        twords = list(text[0:arg2])
        str1 = ' '.join(twords)
        return str1 

tulisanPanjang = TrimWords("ini adalah tulisan yang sangat panjang",3)
print(tulisanPanjang)