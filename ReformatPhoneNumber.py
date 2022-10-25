class Solution:
    def reformatNumber(self, number: str) -> str:

        mem = [""]
        i = 0
        for ch in number:
            if ch != "-" and ch != " ":
                mem[-1] += ch
                i += 1
                if i == 3:
                    i = 0
                    mem.append("")

        if len(mem[-1]) == 1:
            if len(mem[-2]) == 3:
                s = mem[-2] + mem[-1]
                mem[-2] = s[:2]
                mem[-1] = s[2:]

        if mem[-1] == "":
            mem = mem[:-1]

        return "-".join(mem)


        