class Tuple:
    def __init__(self, fio, group, gpa):
        # exception
        if not isinstance(fio, str) or not isinstance(group, str) or not isinstance(gpa, (int, float)) or gpa < 0 or gpa > 5 or len(fio) == 0 or len(group) == 0:
            raise TypeError("Failed to construct tuple. Wrong data")
        
        # fio
        self.fio = list(dict.fromkeys(fio.split(' ')))
        if '' in self.fio:
            self.fio.remove('')
        self.fio = [name.capitalize() for name in self.fio]
        
        # group
        self.group = group.replace(" ", "")
        
        # gpa
        self.gpa = format(gpa, '.3g')

    def format_record(self):
        second_name = self.fio[0]
        first_name_short = self.fio[1][0]
        if len(self.fio) == 3:
            third_name_short = self.fio[2][0]
            a = f"{second_name} {first_name_short}. {third_name_short}."
        else:
            a = f"{second_name} {first_name_short}."
        return f"{a}, гр. {self.group}, GPA {self.gpa}"
    

def format_record(rec: tuple[str, str, float]) -> str:
    fio = list(dict.fromkeys(rec[0].split(' ')))
    if '' in fio:
        fio.remove('')
    fio = [name.capitalize() for name in fio]
    
    # group
    group = rec[1].replace(" ", "")
    
    # gpa
    gpa = format(rec[2], '.3g')

    second_name = fio[0]
    first_name_short = fio[1][0]
    if len(fio) == 3:
        third_name_short = fio[2][0]
        a = f"{second_name} {first_name_short}. {third_name_short}."
    else:
        a = f"{second_name} {first_name_short}."
    return f"{a}, гр. {group}, GPA {gpa}"