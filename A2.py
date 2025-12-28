class USA():
    def capital(self):
        print("Capital of USA is: Washington DC")
    def language(self):
        print("National language of USA is English")


class Pakistan():
    def capital(self):
        print("Capital of Pakistan is: Islamabad")
    def language(self):
        print("National language of pakistan is urdu")

class Turkey():
    def capital(self):
        print("Capital of Turkey is: Ankara")
    def language(self):
        print("National language of Turkey is Turkish")

obj_usa=USA()
obj_pk=Pakistan()
obj_turkeye=Turkey()

for country in (obj_usa,obj_pk,obj_turkeye):
    country.capital()
    country.language()
    print("\n") 