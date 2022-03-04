import pyinputplus as pyip

bread_types={'wheat':10, 'white':10, 'sourdough':12}
protein_types={'chicken':15, 'turkey':20, 'ham':12, 'tuna':10}
with_cheese = False
cheese_types={'cheddar':10, 'swiss':15, 'mozzarella':12}
with_sauce = False
sauce_types={'mayo':2, 'mustard':5}
with_veggies = False
veggies_types={'lettuce':1, 'tomato':1}
quantity = 0
selected_options = []
price = 0

def yesNoToBoolean(answer):
    if answer.lower() in ["yes", "y"]:
        return True

    return False

def chooseOption(options, option_type):
    prompt = "Choose %s type (%s): " % (option_type, ' '.join(list(options)))
    return pyip.inputChoice(options, prompt)

def chooseOptionalOption(options_dict, option_type):
    global price
    with_option = pyip.inputYesNo(
        prompt="Would you like %s?: " % option_type,
        postValidateApplyFunc=yesNoToBoolean)
    if with_option:
        selected_option = chooseOption(list(options_dict), option_type)
        price += options_dict[selected_option]
        selected_options.append(selected_option)

print('Sandwich Maker')
bread = chooseOption(list(bread_types), "bread")
price += bread_types[bread]
protein = chooseOption(list(protein_types), "protein")
price += protein_types[protein]

chooseOptionalOption(cheese_types, "cheese")
chooseOptionalOption(sauce_types, "sauce")
chooseOptionalOption(veggies_types, "veggies")

quantity = pyip.inputInt(prompt="How many sandwiches do you want?: ", min=1)

print('You have ordered %s sanwdich(es) with %s bread, %s protein,' % \
        (quantity, bread, protein), end='')
print('and options [%s]' % ' '.join(selected_options))
print('Total: %s' % price)
