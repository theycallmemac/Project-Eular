u = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
t = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
others = ['hundred', 'thousand', 'and']

answer = 0

for i in range(1, 1001):
    units = i % 10
    tens = (i // 10) % 10
    hundreds = (i//100)%10
    thousands = (i // 1000) % 10
    
    if thousands != 0:
        answer += len(u[0]) + len(others[1])
        
    if i % 1000 != 0:
        if hundreds != 0:
            answer += len(u[hundreds-1]) + len(others[0])
            if i % 100 != 0:
                answer += len(others[2])
                
        if i % 100 != 0:
            if tens < 2:
                answer += len(u[i % 100 - 1])
            else:
                answer += len(t[tens-2])
                if units != 0:
                    answer += len(u[units-1])
print(answer)
