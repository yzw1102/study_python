from enum import Enum,unique

@unique
class Month(Enum):
    Jan = 'January'
    Feb = 'February'
    Mar = 'March'
    Apr = 'April'
    May = 'May'
    Jun = 'June'
    Jul = 'July'
    Aug = 'August'
    Sep = 'September '
    Oct = 'October'
    Nov = 'November'
    Dec = 'December'

if __name__ == '__main__':
    print(Month.Jan,'-------',Month.Jan.name,'-------',Month.Jan.value)

    for name,member in Month.__members__.items():
        print(name,'------',member,'-------',member.value)