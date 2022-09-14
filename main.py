def main():
    f = open('puzzle2.txt')
    puzzle_text = f.read()
    puzzle_lines = puzzle_text.split('\n')
    solved = False
    guesses = []
    guess = ''
    while not solved:
        if len(guess) > 0 and guess not in guesses:
            guesses.append(guess)
        first_line = True
        for line in puzzle_lines:
            words = line.split(' ')
            newline = ''
            correct_count = 0
            for word in words:
                has_period = False
                if len(word) > 0 and word[-1] == '.':
                    has_period = True
                    word = word.replace('.', '')
                if solved:
                    newline += word
                elif 0 < len(word) <= 3:
                    newline += word
                    correct_count += 1
                elif word.lower() in guesses:
                    newline += word
                    correct_count += 1
                else:
                    newline += '_'.rjust(len(word), '_')
                if has_period:
                    newline += '.'
                newline += ' '
            if first_line and len(words) == correct_count:
                solved = True
            first_line = False
            print(newline)

        if not solved:
            print('guesses: %s' % ', '.join(guesses))
            guess = input('Guess a word. ')
        else:
            print('\nYou solved it!')
            input('Press ENTER to exit.')


if __name__ == '__main__':
    main()
