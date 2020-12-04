# لمعرفة بيانات الفيديو
# from pafy import new
# test = new('https://www.youtube.com/watch?v=8ijsxKzgROM')
# print(test)

# https://www.youtube.com/watch?v=dNxNU-SPUW0

# لتحميل الفيديو بالدقة التي اريدها
# from pafy import new
# url = input('Enter you link here: ')
# video = new(url)
# stream = video.streams
for i in stream:
    print(i)
# stream[0].download()

# لتحميل الفيديو باقوى دقة بدون إختيار
# from pafy import new
# url = input('Enter you link here: ')
# video = new(url)
# dl = video.getbest()
# dl.download()

# لتحميل الفيديو بصيغة صوت فقط
# from pafy import new
# url = input('Enter you link here: ')
# video = new(url)
# audio = video.audiostreams
# for i in audio:
#     print(i)
# audio[0].download()