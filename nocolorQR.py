# 2.生成黑白底图二维码

from MyQR import myqr
myqr.run(words='https://github.com/JacksonSteven',
         picture='nocolorQR.jpg',
         
         save_name='colorQR2.png')
#  wods输入网址
# picture输入图片，新手输入图片绝对地址，我的代码中为相对地址
# save_name 是输出图片的保存名
# 输入图片和输出结果都上传了
