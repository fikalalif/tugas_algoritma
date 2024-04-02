tukang = ['andri', 'dadank', 'slamet', 'ujank', 'janggar']
pilih = ['ya', 'tidak']
lokasi = ['slawi', 'lebaksiu', 'balapulang', 'adiwerna', 'pangkah']
nama = str(input('masukan nama anda : '))

print ('pilih lokasi anda')
str(input(lokasi))
alamat_desa = str(input('Nama Desa : '))
alamat_rt = int(input('RT : '))
alamat_no = int(input('NO RUMAH : '))
alamat_lengkap = {'Desa' : alamat_desa, 'RT' : alamat_rt, 'NO RUMAH' : alamat_no}
print(alamat_lengkap)

masalah = str(input('Apa masalah anda? : '))

if masalah == 'tembok luntur':
    print('Kami merekomendasikan andri, karena sudah memilki skill mengecat selama 3 tahun')
    print('apakah anda setuju? ya/tidak ')
    memilih = str(input(pilih))
    if memilih == 'ya':
        print('mohon menunggu kami akan menghubungi pak andri')
    if memilih == 'tidak':
        print('silahkan pilih tukang anda')
        str(input(tukang))
        print('mohon menunggu kami akan segera menghubungi tukang yang anda pilih')  

elif masalah == 'genteng bocor':
    print('kami merekomendasikan slamet, karena sudah memiliki pengalaman dengan genteng bocor selama 5 tahun')
    print('apakah anda setuju? ya/tidak ')
    memilih = str(input(pilih))
    if memilih == 'ya':
        print('mohon menunggu kami akan menghubungi pak slamet')
    if memilih == 'tidak':
        print('silahkan pilih tukang anda')
        str(input(tukang))
        print('mohon menunggu kami akan segera menghubungi tukang yang anda pilih')

else:
    print('silahkan pilih tukang anda')
    str(input(tukang))
    print('mohon menunggu kami akan segera menghubungi tukang yang anda pilih')

print('tukang segera datang ke lokasi anda')