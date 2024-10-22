#可以在輸出浮點數時指定精度 
>>> 'example:%.2f' % 19.234
'example:19.23'

#也可以指定輸出時，至少要預留的字元寬度
#由於預留了6個字元寬度，不足的部份要由空白字元補上。使用%運算子來格式化字串，會產生新的字串物件。
>>> "example:%6.2f" % 19.234
'example: 19.23'
>>>

#在格式化時，也可以使用關鍵字來指定
>>> '%(real)s is %(nick)s!!' % ({'real' : 'Justin', 'nick' : 'caterpillar'})
'Justin is caterpillar!!'
>>>