    file_name = 'c:\mypycode\data\coffee201910.txt'
    f=open(file_name)
    header = f.readline()
    headerList=header.split()
    headerList

    espresso=[]
    americano=[]
    cafelatte=[]
    cappucino=[]

    for line in f:
        dataList = line.split()
        espresso.append(int(dataList[1]))
        americano.append(int(dataList[2]))
        cafelatte.append(int(dataList[3]))
        cappucino.append(int(dataList[4]))                   
    f.close
    total_sum = [sum(espresso), sum(americano) ,sum(cafelatte), sum(cappucino)]
    total_mean = [sum(espresso)/len(espresso), sum(americano)/len(americano), sum(cafelatte)/len(cafelatte), sum(cappucino)/len(cappucino)]

    temp1 = file_name.split('.',2)
    temp2 = temp1[0].split('2019',2)
    month = temp2[1]

    for i in range(len(total_sum)):
        print('[{0}] 판매량 : {1}월 중 {2}일 전체 {3}잔, 하루평균 {4:.2f}잔'.format(headerList[i+1],month,len(total_sum),total_sum[i], total_mean[i]))
