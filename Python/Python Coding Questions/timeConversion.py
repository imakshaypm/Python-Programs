def timeConversion(s):
    # Write your code here
    
    aOrP = s[-2:]
    hour = s[:2]
    if hour[0] == '0':
        hour = hour[1]
    hour = int(hour)
    if aOrP == 'AM':
        if hour < 12:
            return s[:8]
        if hour == 12:
            h = "00"
            minute = s[3:5]
            sec = s[6:8]
            return h+':'+minute+':'+sec
    else:
        if hour < 12:
            hr = str(12 + hour)
            minu = s[3:5]
            se = s[6:8]
            return hr+':'+minu+':'+se

print(timeConversion("06:40:03AM"))