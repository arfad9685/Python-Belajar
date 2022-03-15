#ketikkan skrip di bawah ini di cmd:
#PS D:\MAF\MAF\belajarpython> & C:/Python34/python.exe d:/MAF/MAF/belajarpython/setup.py py2exe - jika menggunakan VScode
#arahkan ke folder penyimpanan setup.py (d:/MAF/MAF/belajarpython/setup.py)
#lihat .exe di folder :dist
#utk menjalankannya harus di folder dist,,tidak bs di pindah


from distutils.core import setup
import py2exe

setup(console=['miniMusicPlayer.py']) 
