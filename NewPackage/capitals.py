list_of_capitals = {'Aland Islands':'Mariehamn',
'Albania':'Tirana',
'Andorra':'Andorra la Vella',
'Armenia':'Yerevan',
'Austria':'Vienna',
'Azerbaijan':'Baku',
'Belarus':'Minsk',
'Belgium':'Brussels',
'Bosnia and Herzegovina':'Sarajevo',
'Bulgaria':'Sofia',
'Croatia':'Zagreb',
'Cyprus':'Nicosia',
'Czech Republic':'Prague',
'Denmark':'Copenhagen',
'Estonia':'Tallinn',
'Faroe Islands':'Torshavn',
'Finland':'Helsinki',
'France':'Paris',
'Georgia':'Tbilisi',
'Germany':'Berlin',
'Gibraltar':'Gibraltar',
'Greece':'Athens',
'Guernsey':'Saint Peter Port',
'Hungary':'Budapest',
'Iceland':'Reykjavik',
'Ireland':'Dublin',
'Isle of Man':'Douglas',
'Italy':'Rome',
'Jersey':'Saint Helier',
'Kosovo':'Pristina',
'Latvia':'Riga',
'Liechtenstein':'Vaduz',
'Lithuania':'Vilnius',
'Luxembourg':'Luxembourg',
'Macedonia':'Skopje',
'Malta':'Valletta',
'Moldova':'Chisinau',
'Monaco':'Monaco',
'Montenegro':'Podgorica',
'Netherlands':'Amsterdam',
'Northern Cyprus':'North Nicosia',
'Norway':'Oslo',
'Poland':'Warsaw',
'Portugal':'Lisbon',
'Romania':'Bucharest',
'Russia':'Moscow',
'San Marino':'San Marino',
'Serbia':'Belgrade',
'Slovakia':'Bratislava',
'Slovenia':'Ljubljana',
'Spain':'Madrid',
'Svalbard':'Longyearbyen',
'Sweden':'Stockholm',
'Switzerland':'Bern',
'Turkey':'Ankara',
'Ukraine':'Kyiv',
'United Kingdom':'London',
'Vatican City':'Vatican City'}

def check_capital(state_name):
    if args.name in list_of_capitals:
        if args.verbosity >= 2:
            print(" We are checking your input in order to understand if it is contained in the list of capitals,The capital of {} is {}".format(state_name, list_of_capitals[state_name] ))
        elif args.verbosity >= 1:
            print("The capital of {} is {}".format(state_name, list_of_capitals[state_name])
        else:
            print(list_of_capitals[state_name]) 

def check_state(capital_name):
    for state, capital in list_of_capitals.items():
        if capital == capital_name:
            if args.verbosity >= 2:
                print(" We are checking your input in order to understand if it is contained in the list of capitals,The European state whose capital is {} is {}".format(capital_name, state))
            elif args.verbpsoty >= 1:
                print("The European state whose capital is {} is {}".format(capital_name, state))
            else:
                print(state)
    if capital not in list_of_capitals.values():
        print("Sorry, {} is not the capital of any European state".format(capital_name))
    elif state not in list_of_capitals.keys():
        print("Sorry, {} is not a European state".format(state))
