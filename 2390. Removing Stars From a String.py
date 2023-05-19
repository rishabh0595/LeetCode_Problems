def removeStars(s):
    st = []
    for i in range(0, len(s)):
        if s[i] == '*'and st is not None:
            st.pop()
        else:
            st.append(s[i])

    return ''.join(st)

s = "leet**cod*e"
print(removeStars(s))