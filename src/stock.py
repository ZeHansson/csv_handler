import constants
import xlsxwriter

class stock:
    def __init__(self, ticker, beginning=False):
        self.ticker = ticker
        self.is_beginning = beginning
        self.rows = []

    def set_beginning(self):
        self.is_beginning = True

    def get_isbeginning(self):
        return self.is_beginning
    
    def convert_to_csv(self, number):
        self.rows.append(self.mk_first_row(number))
        self.rows.append(self.mk_scnd_row(number))
        self.rows.append(self.mk_blank_row())
        self.rows.append(self.mk_frth_row(number))
        self.rows.append(self.mk_blank_row())
        self.rows.append(self.mk_sxth_row(number))
        self.rows.append(self.mk_svnth_row(number))
        self.rows.append(self.mk_blank_row())
        self.rows.append(self.mk_nnth_row(number))
        self.rows.append(self.mk_tnth_row(number))

    def get_rows(self):
        return self.rows
        
    def mk_first_row(self, number):
        if self.get_isbeginning():
            return (f"Start Dato :,01/01/2025, , ,Max/Min start date : ,=TODAY()-15 ,=MAX(INDEX({constants.API}({letter_logic(1,number)}4; \"high\";{letter_logic(6,number)}1;{letter_logic(6,number)}2; \"DAILY\");0;2)) ,Diff is , , ")
        else:
            return (f", , , ,Max/Min start date : ,=TODAY()-15 ,=MAX(INDEX({constants.API}({letter_logic(1,number)}4; \"high\";{letter_logic(6,number)}1;{letter_logic(6,number)}2; \"DAILY\");0;2)) ,Diff is , , ")

    def mk_scnd_row(self, number):
        if self.get_isbeginning():
            return f"Slut Dato :,=TODAY(), , , Max/Min start date : ,=TODAY() ,=MIN(INDEX({constants.API}({letter_logic(1,number)}4; \"high\";{letter_logic(6,number)}1;{letter_logic(6,number)}2; \"DAILY\");0;2)),=( {letter_logic(7,number)}1-{letter_logic(7,number)}2) , ,"
        else :
            return f", , , , Max/Min start date : ,=TODAY() ,=MIN(INDEX({constants.API}({letter_logic(1,number)}4; \"high\";{letter_logic(6,number)}1;{letter_logic(6,number)}2; \"DAILY\");0;2)),=( {letter_logic(7,number)}1-{letter_logic(7,number)}2) , , "
    
    def mk_frth_row(self, number):
        return f"{self.ticker}, ,={constants.API}({letter_logic(1,number)}4;\"name\"), , , , , , , "

    def mk_sxth_row(self, number):
        return f"Outstanding:,={constants.API}({letter_logic(1,number)}4;\"shares\"),PE: ,={constants.API}({letter_logic(1,number)}4;\"pe\") ,Beta : ,={constants.API}({letter_logic(1,number)}4;\"beta\") , , , , "

    def mk_svnth_row(self, number):
        return f"avg Vol : ,={constants.API}({letter_logic(1,number)}4;\"volumeavg\"),EPS: ,={constants.API}({letter_logic(1,number)}4;\"eps\") ,Market cap: ,={constants.API}({letter_logic(1,number)}4;\"marketcap\") , , , , "
    def mk_nnth_row(self, number):
        return f"=SORT(({constants.API}({letter_logic(1,number)}4; \"all\" ; B1;B2; \"DAILY\"));1;FALSE) , , , , , ,Percentage Dif ,AVG DIF , ,"

    def mk_tnth_row(self, number):
        return f" , , , , , ,=IFERROR(100-{letter_logic(4,number)}:{letter_logic(4,number)}/{letter_logic(3,number)}:{letter_logic(3,number)}*100;\"\") ,=AVERAGE({letter_logic(7,number)}:{letter_logic(7,number)}) , , "
    def mk_blank_row(self):
        return ""
        
def letter_logic(position, current ):
    return xlsxwriter.utility.xl_col_to_name((position+ (current*9))-1)    
