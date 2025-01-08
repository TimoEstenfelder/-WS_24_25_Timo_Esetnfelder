#Übung 1 

def string_to_array(input_string):
    words = input_string.split()
    print(words)

# Test cases
string_to_array("Robin Singh")  # Should print: ["Robin", "Singh"]
string_to_array("I love arrays they are my favorite")  # Should print: ["I", "love", "arrays", "they", "are", "my", "favorite"]

def maskify(input_string):
    if len(input_string) <= 4:
        return input_string
    return '#' * (len(input_string) - 4) + input_string[-4:]

# Testfälle
print(maskify("Skippy"))                                   # Output: "##ippy"
print(maskify("Nananananananananananananananana Batman!")) # Output: "####################################man!"
print(maskify("4556364607935616"))                         # Output: "############5616"
print(maskify("64607935616"))                              # Output: "#######5616"
print(maskify("1"))                                        # Output: "1"
print(maskify(""))                                         # Output: ""


def basic_op(operation, value1, value2):
    if operation == '+':
        return value1 + value2
    elif operation == '-':
        return value1 - value2
    elif operation == '*':
        return value1 * value2
    elif operation == '/':
        return value1 / value2
    else:
        return "Das war falsch!"

# Testfälle
print(basic_op('+', 4, 7))         # Output: 11
print(basic_op('-', 15, 18))       # Output: -3
print(basic_op('*', 5, 5))         # Output: 25
print(basic_op('/', 49, 7))        # Output: 7



def how_much_i_like_you(nb_petals):
    phrases = [
        "I like you",
        "a little",
        "a lot",
        "passionately",
        "madly",
        "not at all",
        "totally",
        "pamybelly",
        "hardly", #Liste auf 9 erhöht. 
    ]
    return phrases[(nb_petals - 1) % len(phrases)]


for i in range(1, 10): #Einfacheres Testen von allen Fällen 
    print(f"{i}: {how_much_i_like_you(i)}")


def find_even_index(arr):
    for n in range(len(arr)):
        Link_Index = sum(arr[:n])  
        recht_Index = sum(arr[n+1:]) 
        # Überprüfe, ob die Summen gleich sind
        if Link_Index == recht_Index:
            return n 
    return -1  

# Testfälle
print(find_even_index([1, 2, 3, 4, 3, 2, 1]))  # Output: 3
print(find_even_index([1, 100, 50, -51, 1, 1]))  # Output: 1
print(find_even_index([1, 2, 3, 4, 5, 6]))  # Output: -1
print(find_even_index([20, 10, 30, 10, 10, 15, 35]))  # Output: 3
print(find_even_index([20, 10, -80, 10, 10, 15, 35]))  # Output: 0
print(find_even_index([10, -80, 10, 10, 15, 35, 20]))  # Output: 6
print(find_even_index(range(1, 100)))  # Output: -1
print(find_even_index([-1, -2, -3, -4, -3, -2, -1]))  # Output: 3
print(find_even_index(range(-100, -1)))  # Output: -1
print(find_even_index([0, 0, 0, 0, 0]))  # Output: 0


def numericals(input_string):
    char_count = {}
    result = ""      

    for char in input_string:
        if char in char_count:
            char_count[char] += 1  
        else:
            char_count[char] = 1  
        result += str(char_count[char]) 

    return result

# Testfälle
print(numericals("Hello, World!"))  # Output: "1112111121311"
print(numericals("Hello, World! It's me, JomoPipi!"))  # Output: "11121111213112111131224132411122"
print(numericals("hello hello"))  # Output: "11121122342"
print(numericals("Hello"))  # Output: "11121"
print(numericals("aaaaaaaaaaaa"))  # Output: "123456789101112"


def solve(a, b):
    return [a.count(word) for word in b]

# Testfälle
print(solve(['abc', 'abc', 'xyz', 'abcd', 'cde'], ['abc', 'cde', 'uap']))  # Output: [2, 1, 0]
print(solve(['abc', 'xyz', 'abc', 'xyz', 'cde'], ['abc', 'cde', 'xyz']))  # Output: [2, 1, 2]
print(solve(['quick', 'brown', 'fox', 'is', 'quick'], ['quick', 'abc', 'fox']))  # Output: [2, 0, 1]
