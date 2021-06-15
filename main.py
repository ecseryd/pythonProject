# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import os


# Complete the isValid function below.
def isValid(s):
    if len(s) <= 3:     # either one char appears twice, or each appears once
        return "YES"
    c_freqs = {}        # how often does each character occur?
    for c in s:
        if c in c_freqs:
            c_freqs[c] += 1
        else:
            c_freqs[c] = 1
    # print("c_freqs = " + str(c_freqs))
    freq_freqs = {}     # how often does each frequency occur?
    for f in c_freqs.values():
        if f in freq_freqs:
            freq_freqs[f] += 1
        else:
            freq_freqs[f] = 1
    # print("freq_freqs = " + str(freq_freqs))

    if len(freq_freqs) == 1:
        # All chars have the same frequency
        return "YES"
    elif len(freq_freqs) > 2:
        # Can't adjust for 3+ different frequencies
        return "NO"
    else:   # == 2; more to do
        if 1 in freq_freqs and freq_freqs[1] == 1:
            # Drop the single character; all the rest have the same count
            return "YES"
        else:
            f_f_k = freq_freqs.keys()
            if (max(f_f_k) == min(f_f_k) + 1) and (freq_freqs[max(f_f_k)] == 1):
                # A single char can have a count 1 higher than the rest
                return "YES"
            else:
                # No adjustment possible; we can only drop one character
                return "NO"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    v = isValid("aabbccd")
    print(v)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
