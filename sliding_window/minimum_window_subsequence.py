def min_window(s1, s2):
    min_sequence_len = float('inf')
    min_subsequence = ""
    s1_index = s2_index = 0
    while s1_index < len(s1):
        if s1[s1_index] == s2[s2_index]:
            s2_index += 1
            
            if s2_index == len(s2):
                start = end = s1_index
                s2_index -= 1
                
                while s2_index >=0:
                    if s2[s2_index] == s1[start]:
                        s2_index -= 1
                    start -= 1
                start += 1
                
                seq_len = end - start
                if seq_len < min_sequence_len:
                    min_sequence_len = seq_len
                    min_subsequence = s1[start: end+1]
            
                s2_index = 0
                s1_index = start
            
        s1_index += 1
        
    return min_subsequence

# driver code
def main():
    str1 = ["abcdedeaqdweq", "fgrqsqsnodwmxzkzxwqegkndaa", "zxcvnhss", "alpha", "beta"]
    str2 = ["adeq", "kzed", "css", "la", "ab"]

    for i in range(len(str1)):
        print(i+1, ". \tInput string: (" + str1[i]+", " + str2[i]+")", sep="")
        print("\tSubsequence string: ", min_window(str1[i], str2[i]))
        print("-"*100)

if __name__ == '__main__':
    main()