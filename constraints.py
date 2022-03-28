colors = ['Red', 'Blue', 'Green', 'Yellow', 'Black']
states = ['Andhra', 'Karnataka', 'TamilNadu', 'Kerala']
neighbors = {}
neighbors['Andhra'] = ['Karnataka', 'TamilNadu']
neighbors['Karnataka'] = ['Andhra', 'TamilNadu', 'Kerala']
neighbors['TamilNadu'] = ['Andhra', 'Karnataka', 'Kerala']
neighbors['Kerala'] = ['Karnataka', 'TamilNadu']
colors_of_states = {}
def promising(state, color):
for neighbor in neighbors.get(state):
color_of_neighbor = colors_of_states.get(neighbor)
if color_of_neighbor == color:
return False

return True
def get_color_for_state(state):
for color in colors:
if promising(state, color):
return color

def main():
for state in states:
colors_of_states[state] = get_color_for_state(state)
print (colors_of_states)

main()
Output:

Code:
def isSolvable(words, result):
mp = [-1]*(26)
Hash = [0]*(26)

CharAtfront = [0]*(26)
uniq = ""

for word in range(len(words)):
for i in range(len(words[word])):
ch = words[word][i]
Hash[ord(ch) - ord('A')] += pow(10, len(words[word]) - i - 1)
if mp[ord(ch) - ord('A')] == -1:
mp[ord(ch) - ord('A')] = 0
uniq += str(ch)
if i == 0 and len(words[word]) > 1:
CharAtfront[ord(ch) - ord('A')] = 1

for i in range(len(result)):
ch = result[i]
Hash[ord(ch) - ord('A')] -= pow(10, len(result) - i - 1)
if mp[ord(ch) - ord('A')] == -1:

mp[ord(ch) - ord('A')] = 0
uniq += str(ch)

if i == 0 and len(result) > 1:
CharAtfront[ord(ch) - ord('A')] = 1

mp = [-1]*(26)
return True

def solve(words, i, S, mp, used, Hash, CharAtfront):
if i == len(words):
return S == 0
ch = words[i]
val = mp[ord(words[i]) - ord('A')]
if val != -1:
return solve(words, i + 1, S + val * Hash[ord(ch) - ord('A')], mp,

used, Hash, CharAtfront)

x = False
for l in range(10):
if CharAtfront[ord(ch) - ord('A')] == 1 and l == 0:
continue
if used[l] == 1:
continue
mp[ord(ch) - ord('A')] = l
used[l] = 1

x |= solve(words, i + 1, S + l * Hash[ord(ch) - ord('A')], mp,

used, Hash, CharAtfront)

mp[ord(ch) - ord('A')] = -1
used[l] = 0
return x
arr = [ "SIX", "SEVEN", "SEVEN" ]
S = "TWENTY"
print(arr)
print(S)
if isSolvable(arr, S):
print("Yes")
else:
print("No")
