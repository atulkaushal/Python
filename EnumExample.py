from enum import Enum

class Color(Enum):
    RED='red'
    GREEN='green'
    BLUE='blue'

color=Color(input("Enter your choice of 'red' , 'green' or 'blue : " ))

match color:
    case Color.RED:
        print('I see red')
    case Color.BLUE:
        print('I see blue')
    case Color.GREEN:
        print('I see green')