''' Course:   DCS 211 Winter 2022
Assignment:   GitHub
Topic:        Make a code for CharList
Purpose:      To practice bash by writing a script to solve a problem of our own design

Names: Team "Alpha", Celia Tolan (CharList)

Other students outside my pair that I received help from (N/A if none):
    N/A

Other students outside my pair that I gave help to (N/A if none):
    N/A '''

class CharList: #in python, "char" is a singe-entry str
    def __init__(self):
        self.list = []

    def __str__(self) -> str:
        return str(self._list).replace(', ',',')
        #returns a str representation of CharList with spaces removed

    def __len__(self) -> int:
        return len(self._list)
        #returns the length of CharList

    def __getitem__(self, index: int) -> str:
        return self._list[index]
        #returns the character at the certain index but also makes exceptions when needed

    def __setitem__(self, index: index, char: str) -> None:
        if index in range(len(self._list)):
            self._list[index] = char
        else:
            self._list.append(char)
        #if the index is "size-legitimate", then put char in index
        #else, append char to the end of the list

    def append(self, char: str) -> None:
        self._list.append(char)
        #append the char to the end of the list

    def appendFloatList(self, float_list: 'FloatList') -> None:
        for i in float_list:
            self._list.append(ord(int(float_list[i])))
        #this function appends the float of each float in float_list to a list called 'FloatList'
        #this makes it the char version of teh int representation of the floats

    def appendIntList(self, int_list: 'IntList') -> None:
        for i in int_list:
            self._list.append(ord(int(int_list[i])))
        #this function appends each of the int in int_list to the 'IntList'
        #this makes it hte char version of the int
