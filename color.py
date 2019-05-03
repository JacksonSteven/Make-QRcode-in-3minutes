# 3.有颜色底图二维码
# 在2基础上打开颜色即可，即colorized=True



from MyQR import myqr
myqr.run(words='https://github.com/JacksonSteven',
         picture='nocolorQR.jpg',
         colorized=True,
         save_name='colorQR2.png')
