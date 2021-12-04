import datetime

def reshapeDate(str):
    splitted = str.split(' ')
    day = splitted[1]
    month = splitted[2]
    year = splitted[3]
    hourminsec = splitted[4]
    reshapedStr = '{} {} {} {}'.format(year, month, day, hourminsec)
    reshapedDatetime = datetime.datetime.strptime(reshapedStr, '%Y %b %d %H:%M:%S')
    return reshapedDatetime

