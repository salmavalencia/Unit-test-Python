def isAnagram(word1, word2):
    sorted_word1 = sorted(word1.lower())
    sorted_word2 = sorted(word2.lower())
    
    return sorted_word1 == sorted_word2
