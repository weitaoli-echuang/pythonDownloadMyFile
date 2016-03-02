__author__ = 'VDTConstructor'
import os

if __name__ == '__main__':
	url = '\"http://qd.poms.baidupcs.com/file/8bbca60468ce14167e85aad5e4cefc8c?bkt=p3-14008bbca60468ce14167e85aad5e4cefc8caf60fc380000000003e0&fid=3525507348-250528-366277664328187&time=1456908130&sign=FDTAXGERLBH-DCb740ccc5511e5e8fedcff06b081203-v%2FrEJ4oqJvRcZ6BZFCt1anzkM4o%3D&to=qb&fm=Nin,B,U,nc&sta_dx=0&sta_cs=0&sta_ft=gz&sta_ct=5&fm2=Ningbo,B,U,nc&newver=1&newfm=1&secfm=1&flow_ver=3&pkey=14008bbca60468ce14167e85aad5e4cefc8caf60fc380000000003e0&sl=80609359&expires=8h&rt=pr&r=568952563&mlogid=1430903358120920959&vuk=3525507348&vbdid=4032129892&fin=chinese.gz&fn=chinese.gz&slt=pm&uta=0&rtype=1&iv=0&isw=0&dp-logid=1430903358120920959&dp-callid=0.1.1\"'
	command = 'wget -c -O 1.gz '+ url
	os.system(command)

	print 'here'
