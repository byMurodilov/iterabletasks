# 1
# class WeekDay:
#     def __init__(self):
#         self.kunlar = ["Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba", "Yakshanba"]
#         self.gl_kun = 0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.gl_kun < len(self.kunlar):
#             sutka = self.kunlar[self.gl_kun]
#             self.gl_kun +=1
#             return sutka
#         raise StopIteration
# haftani_one_kuni = WeekDay()
# for sutka in haftani_one_kuni:
#     print(sutka)


# 2
# class YilOylari:
#     def __init__(self):
#         self.oylar = ["Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun", "Iyul", "Avgust", "Sentyabr", "Oktyabr", "Noyabr", "Dekabr"]
#         self.gl_oy = 0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.gl_oy < len(self.oylar):
#             month = self.oylar[self.gl_oy]
#             self.gl_oy +=1
#             return month
#         raise StopIteration
# yilning_br_oyi = YilOylari()
# for month in yilning_br_oyi:
#     print(month)


# 3
# class User:
#     def __init__(self, first_name, last_name, email):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#     def __iter__(self):
#         return self
#     def __next__(self):
#         raise StopIteration
# user1 = User("Nick", "Uail", "nickuailfox@gmail.com")
# user2 = User("Jacky", "Chan", "jackychanoff@gmail.com")
# for user in [user1, user2]:
#     print(f"Foydalanuvchining ismi: <{user.first_name}>, familiyasi: <{user.last_name}> va emaili: <{user.email}>")