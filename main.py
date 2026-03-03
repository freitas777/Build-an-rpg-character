full_dot = '●'
empty_dot = '○'

def create_character(name, strenght, intelligence, charisma):
    if not isinstance(name, str):
        return 'The character name should be a string'
    elif name == '':
        return 'The character should have a name'
    elif len(name) > 10:
        return 'The character name is too long'
    elif ' ' in name:
        return 'The character name should not contain spaces'
    
    if not isinstance(strenght, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return 'All stats should be integers'
    elif strenght < 1 or intelligence < 1 or charisma < 1:
        return 'All stats should be no less than 1'
    elif strenght > 4 or intelligence > 4 or charisma > 4:
        return 'All stats should be no more than 4'
    elif strenght + intelligence + charisma != 7:
        return 'The character should start with 7 points'

    full_power = empty_dot * 10

    return f'{name}\nSTR {full_dot * strenght}{full_power[strenght:]}\nINT {full_dot * intelligence}{full_power[intelligence:]}\nCHA {full_dot * charisma}{full_power[charisma:]}'

print(create_character('ren', 2, 4, 1))



