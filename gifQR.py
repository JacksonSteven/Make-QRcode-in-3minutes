# 在3的基础上，把输入换成gif图片即可，切记输出格式也要是gif格式，否则动不起来



from MyQR import myqr
myqr.run(words='https://github.com/JacksonSteven',
         picture='snowball.gif',
         colorized=True,
         save_name='gifQR.gif')
