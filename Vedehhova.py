from random import *

inimesed = []
palgad = []

def sisesta_andmed(i,p):
	c = int(input("How many people: "))
	for n in range(c):
		inim = input("Enter Name: ")
		i.append(inim)
		palg = randint(100,10000)
		p.append(palg)
	return i,p

def andmed_ekranile(i,p):
	N=len(i)
	for n in range(N):
		print(i[n],"-",p[n])

def kustutamine(i,p): #Удалить человека и его зарплату(вводим имя)
	nimi = input("Sisesta nimi, keda vaja kustutada: ")
	n = i.count(nimi) #Кол-во
	abi_list = []
	if n>0:
		t=0
		for e in range(len(i)):
			if i[e]==nimi:
				t+=1
				abi_list.append(e)
				print(i[e],"-",p[e])
				print(t,". ",i[e],"-",i[e])
		j=int(input("Järjekordne number: "))
		andmed_ekranile(i,p)

	return i,p

def suurim_palk(i,p):
    max_palk = max(p)
    x = p.count(max_palk)
    start_ind = 0
    for j in range(x):
        ind = p.index(max_palk)
    print("Inimene", i[ind],"-tema palk: ",p[ind])
    start_ind += ind + 1
    return i,p

def suurim_palk2(i,p):
    p_copy = p.copy()
    i_copy = i.copy()
    palk_max = max(p)
    kogus = copy.count(palk_max)
    t = 0
    for j in range(kogus):
        ind = p_copy.index(palk_max)
    print(ind, i[ind + t], "-1on suurim palk, mis võrdub", palk_max)
    p_copy.pop(ind)
    i_copy.pop(ind)
    t += 1
    print(p,i)

def vaiksem_palk(i,p):
    max_palk = min(p)
    x = p.count(max_palk)
    start_ind = 0
    for j in range(x):
        ind = p.index(max_palk)
    print("Inimene", i[ind],"-tema palk: ",p[ind])
    start_ind += ind + 1
    return i,p

def sorteerimine(i,p,v):
	N=len(p)
	if v==1:
		for n in range(0,N):
			for m in range(n,N):
				if p[n]<p[m]:
					abi=p[n]
					p[n]=p[m]
					p[m]=abi
					abi=i[n]
					i[n]=i[m]
					i[m]=abi
		andmed_ekranile(i,p)
	else:
		for n in range(0,N):
			for m in range(n,N):
				if p[n]>p[m]:
					abi=p[n]
					p[n]=p[m]
					p[m]=abi
					abi=i[n]
					i[n]=i[m]
					i[m]=abi
		andmed_ekranile(i,p)
		print(n)


def vordsed_palgad(i,p):
	N=len(p)
	dublikatid=[x for x in palgad if palgad.count(x)>1 ]
	dublikatid=list(set(dublikatid))
	print(dublikatid)
	for palk in dublikatid:
		n=p.count(palk)
		K=0
		for j in range(n):
			k=p.index(palk,j+k)
			print(k)
			nimi=i[k]
			print(palk,"saab kätte",nimi)
def keskmine(i,p):
	summa=0
	for palk in p:
		summa+=palk
	summa/=len(p)
	print("keskmine palk:",summa)
	for palk in p:
		if palk==summa:
			n=p.index(palk)
			print("saab katte",i[n])
		else:
			print("sellised inimesed puudubad")
def sort_nimi_jargi(p,i,v):
	N=len(p)
	if v==1:
		for n in range(0,N):
			for m in range(n,N):
				if p[n]<p[m]:
					abi=p[n]
					p[n]=p[m]
					p[m]=abi
					abi=i[n]
					i[n]=i[m]
					i[m]=abi
	else:
		for n in range(0,N):
			for m in range(n,N):
				if p[n]>p[m]:
					abi=p[n]
					p[n]=p[m]
					p[m]=abi
					abi=i[n]
					i[n]=i[m]
					i[m]=abi
					print(i[n])

		
while True:
	print("a-andmete sisestamine\ne-andmed ekranile\nk-kustutamine\nm-suurim_palk\nv-vaiksem_palk\ns-sorteerimine\nvp-vordsed_palgad\nkes-keskmine\nsn-sort_nimi_jargi")
	valik=input()
	if valik.lower()=="a":
		ininimesed,palgad = sisesta_andmed(inimesed,palgad)
	elif valik.lower()=="e":
		andmed_ekranile(inimesed,palgad)
	elif valik.lower()=="k":
		inimesed,palgad = kustutamine(inimesed,palgad)
	elif valik.lower()=="m":
		suurim_palk(inimesed,palgad)
	elif valik.lower()=="vm":
		vaiksem_palk(inimesed,palgad)
	elif valik.lower()=="s":
		sorteerimine(inimesed,palgad,int(input("1-kahaneb,2-kasvab: ")))
	elif valik.lower()=="vp":
		vordsed_palgad(inimesed,palgad)
	elif valik.lower()=="kes":
		keskmine(inimesed,palgad)
	elif valik.lower()=="sn":
		sort_nimi_jargi(inimesed,palgad,int)


