#04.クラス継承
#クラス継承の基礎

#親のクラス
class country:
    def __init__(self,country_name):
        self.country_name=country_name

#()で継承
class City(country):
    def __init__(self,country_name,city_name):
        #継承したクラスを呼び出し
        super().__init__(country_name)
        self.city_name=city_name

classes =[]
classes.append(City('Japan','Toky'))
classes.append(City('USA','Washington D.C.'))

for test_cls in classes:
    print("======Class=======")
    print("country_name ---> " + test_cls.country_name)
    print("city_name ---> " + test_cls.city_name)
