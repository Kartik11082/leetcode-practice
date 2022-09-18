class Solution(object):
    def isValid(self, s):
        st = []
        op = ['(', '[', '{']
        cl = [')', ']', '}']
        if len(s) <= 1:
            return False
        for b in s:
            if b in op:
                st.append(b)
            elif b in cl:
                # Check if the brackets are matching
                if st and (cl.index(b) == op.index(st[-1])):
                    st.pop()
                # Means the opening and closing are not same
                else:
                    return False
        if not st:
            return True