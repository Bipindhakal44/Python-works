import pickle

v=['ear','eye','nose']
s=['ole','rou','bin']
pf=open('pick.pkl','wb')
pickle.dump(v,pf)
pickle.dump(s,pf)
pf.close()
