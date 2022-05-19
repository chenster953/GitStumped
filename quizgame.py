print('This will be a simple quiz game. \n'
      'You will be able to select a category \n'
      'There will be 10 question for each category. \n'
      'Good Luck!')

TOTAL_SCORE = 0

while True:
    CATEGORY = input('Select from the following list of categories: \n'
                     'Geography, Numbers, Slogans, Science, Entertainment, Astrophysics: \n'
                     'Type \'total\' to see your total score. \n'
                     'Or type \'quit\' to exit the program').lower()

    while CATEGORY != 'geography' and CATEGORY != 'numbers' and CATEGORY != 'slogans' and CATEGORY != 'science' \
        and CATEGORY != 'entertainment' and CATEGORY != 'astrophysics' and CATEGORY != 'total' and CATEGORY != 'quit':
        CATEGORY = input('Please select a category listed above. ')

# GEOGRAPHY CATEGORY

    if CATEGORY == 'geography':
        GEO_SCORE = 0
        geo_q1 = input('Which is the largest country in the world?: ').lower()
        if geo_q1 == 'russia':
            print('Correct')
            GEO_SCORE += 1
        else:
            print('Incorrect')
        geo_q2 = input('Which country has the largest population in the world?: ').lower()
        if geo_q2 == 'china':
            print('Correct')
            GEO_SCORE += 1
        else:
            print('Incorrect')
        geo_q3 = input('What are the names of the five oceans?: ').lower()
        OCEANS_LIST = ['Pacific', 'Atlantic', 'Indian', 'Arctic', 'Southern']
        OCEANS_LIST_LOWER = [x.lower() for x in OCEANS_LIST]
        if geo_q3 in OCEANS_LIST_LOWER:
            ocean1 = input('Yup, next: ')
            if ocean1 in OCEANS_LIST_LOWER:
                ocean2 = input('Yup, next: ')
                if ocean2 in OCEANS_LIST_LOWER:
                    ocean3 = input('Yup, next: ')
                    if ocean3 in OCEANS_LIST_LOWER:
                        ocean4 = input('Yup, next: ')
                        if ocean4 in OCEANS_LIST_LOWER:
                            print('Correct')
                            GEO_SCORE += 1
                    else:
                        print('Incorrect')
                else:
                    print('Incorrect')
            else:
                print('Incorrect')
        else:
            print('Incorrect')
        geo_q4 = input('What is the capital city of India?: ').lower()
        if geo_q4 == 'new delhi':
            print('Correct')
            GEO_SCORE += 1
        else:
            print('Incorrect')
        geo_q5 = input('In which country would you find the Leaning Tower of Pisa?: ').lower()
        if geo_q5 == 'italy':
            print('Correct')
            GEO_SCORE += 1
        else:
            print('Incorrect')
        geo_q6 = input('Which are the 7 continents in the world from largest in area to smallest?: ').lower()
        if geo_q6 == 'asia':
            a = input('Yup, next: ')
            if a == 'africa':
                b = input('Yup, next: ')
                if b == 'north america':
                    c = input('Yup, next: ')
                    if c == 'south america':
                        d = input('Yup, next: ')
                        if d == 'antarctica':
                            e = input('Yup, next: ')
                            if e == 'europe':
                                f = input('Yup, next: ')
                                if f == 'australia':
                                    print('Correct')
                                    GEO_SCORE += 1
                            else:
                                print('Incorrect')
                        else:
                            print('Incorrect')
                    else:
                        print('Incorrect')
                else:
                    print('Incorrect')
            else:
                print('Incorrect')
        else:
            print('Incorrect')
        geo_q7 = input('Which is colder: The North Pole or the South Pole?: ').lower()
        if geo_q7 == 'south pole' or geo_q7 == 'the south pole':
            print('Correct')
            GEO_SCORE += 1
        else:
            print('Incorrect')
        geo_q8 = input('What is the name of the biggest ocean on Earth?: ').lower()
        if geo_q8 == 'pacific' or geo_q7 == 'pacific ocean' or geo_q7 == 'the pacific ocean':
            print('Correct')
            GEO_SCORE += 1
        else:
            print('Incorrect')
        geo_q9 = input('The United States consists of how many states?: ')
        if geo_q9 == '50' or geo_q9 == 'fifty':
            print('Correct')
            GEO_SCORE += 1
        else:
            print('Incorrect')
        geo_q10 = input('What is taxation?: ').lower()
        if geo_q10 == 'theft':
            print('Damn right it is')
            GEO_SCORE += 1
        else:
            print('Incorrect')
        print('You got ' + str(GEO_SCORE) + ' questions correct in the Geography category! ')
        TOTAL_SCORE += GEO_SCORE
        KEEP_PLAYING = input('Type \'quit\' to quit playing, or type \'main\' to choose a different category: ').lower()
        if KEEP_PLAYING == 'main':
            continue
        elif KEEP_PLAYING == 'quit':
            quit()
        else:
            print('You did not select a valid option, goodbye. ')
            quit()

# NUMBERS CATEGORY

    if CATEGORY == 'numbers':
        MATH_SCORE = 0
        math_q1 = input('What is the only number that has the same number of letters as it’s meaning?: ').lower()
        if math_q1 == '4' or math_q1 == 'four':
            print('Correct')
            MATH_SCORE += 1
        else:
            print('Incorrect')
        math_q2 = input('What number does not have its own Roman numeral?: ').lower()
        if math_q2 == '0' or math_q2 == 'zero':
            print('Correct')
            MATH_SCORE += 1
        else:
            print('Incorrect')
        math_q3 = input('What is the only even prime number?: ').lower()
        if math_q3 == '2' or math_q3 == 'two':
            print('Correct')
            MATH_SCORE += 1
        else:
            print('Incorrect')
        math_q4 = input('What is the most popular lucky number?: ').lower()
        if math_q4 == '7' or math_q4 == 'seven':
            print('Correct')
            MATH_SCORE += 1
        else:
            print('Incorrect')
        math_q5 = input('What is the only number spelled with letters in alphabetical order?: ').lower()
        if math_q5 == '40' or math_q5 == 'forty':
            print('Correct')
            MATH_SCORE += 1
        else:
            print('Incorrect')
        math_q6 = input('How many cupcakes are in a baker’s dozen?: ').lower()
        if math_q6 == '13' or math_q6 == 'thirteen':
            print('Correct')
            MATH_SCORE += 1
        else:
            print('Incorrect')
        math_q7 = input('How many lives are cats said to have?: ').lower()
        if math_q7 == '9' or math_q7 == 'nine':
            print('Correct')
            MATH_SCORE += 1
        else:
            print('Incorrect')
        math_q8 = input('What is the perimeter of a circle called?: ').lower()
        if math_q8 == 'circumference':
            print('Correct')
            MATH_SCORE += 1
        else:
            print('Incorrect')
        math_q9 = input('What is five to the power of zero?: ').lower()
        if math_q9 == '1' or math_q9 == 'one':
            print('Correct')
            MATH_SCORE += 1
        else:
            print('Incorrect')
        math_q10 = input('What is five squared?: ').lower()
        if math_q10 == '25' or math_q10 == 'twenty five' or math_q10 == 'twenty-five':
            print('Correct')
            MATH_SCORE += 1
        else:
            print('Incorrect')
        print('You got ' + str(MATH_SCORE) + ' questions correct in the Numbers category! ')
        TOTAL_SCORE += MATH_SCORE
        KEEP_PLAYING1 = input('Type \'quit\' to quit playing, or type \'main\' to choose a different category: ').lower()
        if KEEP_PLAYING1 == 'main':
            continue
        elif KEEP_PLAYING1 == 'quit':
            quit()
        else:
            print('You did not select a valid option, goodbye. ')
            quit()

# SLOGAN CATEGORY

    if CATEGORY == 'slogans':
        SLOGAN_SCORE = 0
        slo_q1 = input('Guess the company that has this slogan:\n'
                       'The happiest place on earth.: ').lower()
        if slo_q1 == 'disneyland':
            print('Correct')
            SLOGAN_SCORE += 1
        else:
            print('Incorrect')
        slo_q2 = input('Guess the company that has this slogan:\n'
                       'Leave the driving to us.: ').lower()
        if slo_q2 == 'greyhound':
            print('Correct')
            SLOGAN_SCORE += 1
        else:
            print('Incorrect')
        slo_q3 = input('Guess the company that has this slogan:\n'
                       'Betcha can\'t eat just one.: ').lower()
        if slo_q3 == 'lays' or 'lay\'s':
            print('Correct')
            SLOGAN_SCORE += 1
        else:
            print('Incorrect')
        slo_q4 = input('Guess the company that has this slogan:\n'
                       'Believe In Your Smellf.: ').lower()
        if slo_q4 == 'old spice':
            print('Correct')
            SLOGAN_SCORE += 1
        else:
            print('Incorrect')
        slo_q5 = input('Guess the company that has this slogan:\n'
                       'The taste of a new generation.: ').lower()
        if slo_q5 == 'pepsi':
            print('Correct')
            SLOGAN_SCORE += 1
        else:
            print('Incorrect')
        slo_q6 = input('Guess the company that has this slogan:\n'
                       'A Passion For the Road.: ').lower()
        if slo_q6 == 'mazda':
            print('Correct')
            SLOGAN_SCORE += 1
        else:
            print('Incorrect')
        slo_q7 = input('Guess the company that has this slogan:\n'
                       'Get your own box.: ').lower()
        if slo_q7 == 'cheeze it' or 'cheeze-it':
            print('Correct')
            SLOGAN_SCORE += 1
        else:
            print('Incorrect')
        slo_q8 = input('Guess the company that has this slogan:\n'
                       'The best a man can get.: ').lower()
        if slo_q8 == 'gillette':
            print('Correct')
            SLOGAN_SCORE += 1
        else:
            print('Incorrect')
        slo_q9 = input('Guess the company that has this slogan:\n'
                       'Don’t dream it. Drive it.: ').lower()
        if slo_q9 == 'jaguar':
            print('Correct')
            SLOGAN_SCORE += 1
        else:
            print('Incorrect')
        slo_q10 = input('Guess the company that has this slogan:\n'
                        'When you care enough to send the very best.: ').lower()
        if slo_q10 == 'hallmark':
            print('Correct')
            SLOGAN_SCORE += 1
        else:
            print('Incorrect')
        print('You got ' + str(SLOGAN_SCORE) + ' questions correct in the Slogans category! ')
        TOTAL_SCORE += SLOGAN_SCORE
        KEEP_PLAYING2 = input(
            'Type \'quit\' to quit playing, or type \'main\' to choose a different category: ').lower()
        if KEEP_PLAYING2 == 'main':
            continue
        elif KEEP_PLAYING2 == 'quit':
            quit()
        else:
            print('You did not select a valid option, goodbye. ')
            quit()

# SCIENCE CATEGORY

    if CATEGORY == 'science':
        SCI_SCORE = 0
        sci_q1 = input('The concept of gravity was discovered by which famous physicist? ').lower()
        if sci_q1 == 'newton' or sci_q1 == 'isaac newton' or sci_q1 == 'sir isaac newton':
            print('Correct')
            SCI_SCORE += 1
        else:
            print('Incorrect')
        sci_q2 = input('How many colors are in the rainbow? ').lower()
        if sci_q2 == '7' or sci_q2 == 'seven':
            print('Correct')
            SCI_SCORE += 1
        else:
            print('Incorrect')
        sci_q3 = input('True or False? Electrons are smaller than atoms. ').lower()
        if sci_q3 == 'true':
            print('Correct')
            SCI_SCORE += 1
        else:
            print('Incorrect')
        sci_q4 = input('What is the name of the tallest grass on earth? ').lower()
        if sci_q4 == 'bamboo':
            print('Correct')
            SCI_SCORE += 1
        else:
            print('Incorrect')
        sci_q5 = input('Which is the most abundant element in the universe? ').lower()
        if sci_q5 == 'hydrogen':
            print('Correct')
            SCI_SCORE += 1
        else:
            print('Incorrect')
        sci_q6 = input('What is the hardest natural substance on Earth? ').lower()
        if sci_q6 == 'diamond':
            print('Correct')
            SCI_SCORE += 1
        else:
            print('Incorrect')
        sci_q7 = input('Which oath of ethics taken by doctors is named after an Ancient Greek physician? ').lower()
        if sci_q7 == 'hippocratic' or sci_q7 == 'hippocratic oath' or sci_q7 == 'the hippocratic oath':
            print('Correct')
            SCI_SCORE += 1
        else:
            print('Incorrect')
        sci_q8 = input('What does DNA stand for? ').lower()
        if sci_q8 == 'deoxyribonucleic acid.':
            print('Correct')
            SCI_SCORE += 1
        else:
            print('Incorrect')
        sci_q9 = input('At what temperature are Celsius and Fahrenheit equal? ').lower()
        if sci_q9 == '40' or sci_q9 == 'forty':
            print('Correct')
            SCI_SCORE += 1
        else:
            print('Incorrect')
        sci_q10 = input('Which freezes faster, hot water or cold water? ').lower()
        if sci_q10 == 'hot water' or sci_q10 == 'hot':
            print('Correct')
            SCI_SCORE += 1
        else:
            print('Incorrect')
        print('You got ' + str(SCI_SCORE) + ' questions correct in the Science category! ')
        TOTAL_SCORE += SCI_SCORE
        KEEP_PLAYING3 = input(
            'Type \'quit\' to quit playing, or type \'main\' to choose a different category: ').lower()
        if KEEP_PLAYING3 == 'main':
            continue
        elif KEEP_PLAYING3 == 'quit':
            quit()
        else:
            print('You did not select a valid option, goodbye. ')
            quit()

# ENTERTAINMENT CATEGORY

    if CATEGORY == 'entertainment':
        ENT_SCORE = 0
        ent_q1 = input('Who is the superhero that is also known as the “Man of Steel"? ').lower()
        if ent_q1 == 'superman':
            print('Correct')
            ENT_SCORE += 1
        else:
            print('Incorrect')
        ent_q2 = input('What year was the first Iron Movie movie released? ').lower()
        if ent_q2 == '2008':
            print('Correct')
            ENT_SCORE += 1
        else:
            print('Incorrect')
        ent_q3 = input('What is Batman’s real name? ').lower()
        if ent_q3 == 'bruce wayne' or ent_q3 == 'bruce':
            print('Correct')
            ENT_SCORE += 1
        else:
            print('Incorrect')
        ent_q4 = input('Who is the superhero twin brother of Scarlet Witch? ').lower()
        if ent_q4 == 'quicksilver':
            print('Correct')
            ENT_SCORE += 1
        else:
            print('Incorrect')
        ent_q5 = input('What is Superman’s weakness? ').lower()
        if ent_q5 == 'kryptonite':
            print('Correct')
            ENT_SCORE += 1
        else:
            print('Incorrect')
        ent_q6 = input('In the Spider-man movie, Uncle Ben said something to Peter. “With great power, comes great __”').lower()
        if ent_q6 == 'responsibility':
            print('Correct')
            ENT_SCORE += 1
        else:
            print('Incorrect')
        ent_q7 = input('Which superhero has the magic lasso and bullet-proof bracelets? ').lower()
        if ent_q7 == 'wonder woman' or ent_q7 == 'wonderwoman':
            print('Correct')
            ENT_SCORE += 1
        else:
            print('Incorrect')
        ent_q8 = input('Who has an indestructible shield? ').lower()
        if ent_q8 == 'captain america':
            print('Correct')
            ENT_SCORE += 1
        else:
            print('Incorrect')
        ent_q9 = input('Who is the Scarlet Speedster?').lower()
        if ent_q9 == 'the flash' or ent_q9 == 'flash':
            print('Correct')
            ENT_SCORE += 1
        else:
            print('Incorrect')
        ent_q10 = input('Who gets his power from a ring? ').lower()
        if ent_q10 == 'green lantern' or ent_q10 == 'the green lantern':
            print('Correct')
            ENT_SCORE += 1
        else:
            print('Incorrect')
        print('You got ' + str(ENT_SCORE) + ' questions correct in the Science category! ')
        TOTAL_SCORE += ENT_SCORE
        KEEP_PLAYING4 = input(
            'Type \'quit\' to quit playing, or type \'main\' to choose a different category: ').lower()
        if KEEP_PLAYING4 == 'main':
            continue
        elif KEEP_PLAYING4 == 'quit':
            quit()
        else:
            print('You did not select a valid option, goodbye. ')
            quit()

# ASTROPHYSICS CATEGORY

    if CATEGORY == 'astrophysics':
        print('You don\'t know astrophysics, I don\'t know astrophysics, nobody knows astrophysics')
        KEEP_PLAYING5 = input(
            'Type \'quit\' to quit playing, or type \'main\' to choose a different category: ').lower()
        if KEEP_PLAYING5 == 'main':
            continue
        elif KEEP_PLAYING5 == 'quit':
            quit()
        else:
            print('You did not select a valid option, goodbye. ')
            quit()

# TOTAL SCORE

    if CATEGORY == 'total':
        print('Your total score is ' + str(TOTAL_SCORE) + '!')

# QUIT GAME

    if CATEGORY == 'quit':
        quit()
