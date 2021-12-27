#num發票號碼 specail1特別獎 specail2 特獎 win1,win2,win3頭獎 addsix 加開六獎
#輸入輸出皆為string 若沒中即輸出0
#redeem("發票號碼","特別獎號碼","特獎號碼","頭獎號碼1","頭獎號碼2","頭獎號碼3","加開六獎號碼")
def redeem(num="",special1="",special2="",win1="",win2="",win3="",addsix=""):
    
    if num==special1 :
        return "special1"
    elif num==special2 :
        return "special2"
    elif num[-3:]==addsix:
        return "6"
    elif num==win1 or num==win2 or num==win3:
        return "1"
    elif num[1:]==win1[1:] or num[1:]==win2[1:] or num[1:]==win3[1:]:
        return "2"
    elif num[2:]==win1[2:] or num[2:]==win2[2:] or num[2:]==win3[2:]:
        return "3"
    elif num[3:]==win1[3:] or num[3:]==win2[3:] or num[3:]==win3[3:]:
        return "4"
    elif num[4:]==win1[4:] or num[4:]==win2[4:] or num[4:]==win3[4:]:
        return "5"
    elif num[5:]==win1[5:] or num[5:]==win2[5:] or num[5:]==win3[5:]:
        return "6"
    else:
        return "0"     
print(redeem("12345678","","","22345678","32412367","29304857","234"))