#Here i have defined a function to be called later
def NoVowel(Word):
    #this loop is if the word has not been not been called then nothing is returned
    #if no words are inputted then what ever wasput in is returned
    if len(Word) == 0:
        return Word
    #this inner loop is for if vowels are present that need removing
    else:
        StartingLet = Word[0]
        NewWord = Word[1:len(Word) + 1]
#if the words have vowels within them they are then removed to create a new word
        if StartingLet in "aAeEiIoOuU":

            return NoVowel(NewWord)
        else:
            return StartingLet + NoVowel(NewWord) 
