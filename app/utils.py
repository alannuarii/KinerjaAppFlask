months = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']

def get_month(input):
    month = months.index(input) + 1
    if month in [1,2,3,4,5,6,7,8,9]:
        return f'0{month}'
    else:
        return str(month)



