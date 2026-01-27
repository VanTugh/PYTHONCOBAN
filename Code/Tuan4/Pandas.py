import pandas as pd
from pandas import DataFrame
# # lam quen voi pandas
# data = [10,2,3,5,1]
# my_data = pd.Series(data)
# #print(my_data)

# dictionary = {
#     "name":"Tung",
#     "age" :12
# }
# my_dict = pd.Series(dictionary)
# # print(my_dict)
# sinhvien={
#     "Alice" :85,
#     "Bob" : 72,
#     "Charlie": 90,
#     "David": 68 ,
#     "Emma": 95
# }
# my_dssv = pd.Series(sinhvien)
# print(my_dssv)
# my_dssv["Frank"] = 88
# print(my_dssv)
# tont = my_dssv.sum(axis="index")
# print(tont)

# bai 4.6
def bai_4_6():
    danhsach = [
        ['Messi', '34','the falsen 9'],
        ['Ronanldo','36','Striker'],
        ['NeyMar','30','Winger']
    ]
    my_list = pd.DataFrame(danhsach,columns=['Name','Age','Position'])
    print(my_list)

    diction = {
        'Name' : ['Messi' , 'Ronanldo', 'Neymar'],
        'Age'   : [34,36,30],
        'Position' : ['flasen 9', 'Striker','Winger']
    }
    my_dict = pd.DataFrame(diction)
    print(my_dict)
    return my_dict
def in_ra_dau_cuoi(my_dict : DataFrame ):
    # in dong dau tien
    print(my_dict.head(1))
    # in 2 dong cuoi
    print(my_dict.tail(2))
def xu_ly_nghiep_vu(my_dict : DataFrame):
    # them 
    my_dict["Goal"] = [900,1000,700]
    
    my_dict.loc[len(my_dict)] = ['Haaland', 24, 'Striker', 300]
    print("sau khi them :  \n" ,my_dict)
    #xoa
    # my_dict.drop(1,axis = 0,inplace=True )
    # print(" sau khi xoa :  \n", my_dict)
    my_dict.drop('Age',axis=1 , inplace= True)
    print(" sau khi xoa :  \n", my_dict)
def bai4_7():
    data={
        'Name':['A','B','C'],
        'Age':[22,23,19],
        'Language':['Python','C++','Java']
    }
    my_data = pd.DataFrame(data)
    print(my_data)
    return my_data
def them_du_lieu(my_dict : DataFrame):
    my_dict['Gender'] = ['Female','Female','Male']
    return my_dict
def xoa_AGE(my_dict : DataFrame):
    my_dict.drop('Age',axis=1,inplace=True )
    return my_dict
def xoa_hang(my_dict : DataFrame):
    my_dict.drop(0,axis=0, inplace=True)
    return my_dict
def main():
    # my_dict = bai_4_6()
    # # in_ra_dau_cuoi(my_dict)
    # xu_ly_nghiep_vu(my_dict)
    my_dict = bai4_7()
    new_one = them_du_lieu(my_dict)
    print("sau khi them ")
    print(new_one)
    new_one_2 = xoa_AGE(my_dict)
    print("sau khi xoa cot age ")
    print(new_one_2)
    new_one_3 = xoa_hang(my_dict)
    print("sau khi xoa hang : ")
    print(new_one_3)
    print(my_dict[['Name']])
if __name__ =="__main__":
    main()