'''Gully Boy for his new rap, creating a list of characters, so that list can be arranged in different manners, as per the mood of crowd. They seek help from GLA students because they feel this is "Boht Hard" to create. Your task is to keep a linked list of characters for creating rap, but do not keep "white space" character in linked list

-Whenever anyone from the crowd gave gully boy a position of node they have to sing all the linked character N times to create a rap.

for example charsequence is "hello world", int position is 6, N is 1.
we have to store each character in node except white-space, so node position 6 will have 'w' stored in it. And we have to print all characters once so the output will be:
w o r l d h e l l o
Input Format

first line contains an sequence of characters to be stored as linked list of characters
Second line contains an int node position
Third line contains an integer N denoting how many times you have to sing all characters from given node.
Constraints

position>0 & position< total length of char sequence - totla nunber of spaces
N>0 & N<10
Output Format

print space seprated characters from given position, print them N times
Sample Input 0

hello world
6
1
Sample Output 0

w o r l d h e l l o 
Explanation 0

charaequence is "hello world"
int position is 6th node
int N is 1
so we have to print all characters in space seprated manner
w o r l d h e l l o 
there is a space after last character also.
Sample Input 1

apna time ayega
5
3
Sample Output 1

t i m e a y e g a a p n a t i m e a y e g a a p n a t i m e a y e g a a p n a '''


st = input()

node = int(input())
rp = int(input())


print(*(st[node:] + st[:node]).replace(' ', '')*rp)
