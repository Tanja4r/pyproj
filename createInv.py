# comment

gameid = 9802
f = open (str(gameid)+'.inv', 'r+')
f.write ('HH'+str(gameid)+'\n')
for i in range (80000):
    box = i/100 +1
    palett = (box-1) / 96 + 1
    f.write ('BB98021'+ str(i).zfill(5)+'025'+'C'+str(box).zfill(5)+str(palett).zfill(4) + '\n')
f.close()
