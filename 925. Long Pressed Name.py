class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        previousCh = ""
        nIndex = 0
        tIndex = 0

        if len(name) > len(typed):
            return False
        while nIndex < len(name) and tIndex < len(typed):
            if name[nIndex] == typed[tIndex]:
                previousCh = name[nIndex]
                nIndex += 1
                tIndex += 1
            elif previousCh == typed[tIndex]:
                tIndex += 1
            else:
                return False

        if nIndex == len(name) and tIndex == len(typed):
            return True
        elif nIndex == len(name):
            while tIndex < len(typed):
                if previousCh != typed[tIndex]:
                    return False
                tIndex += 1
            else:
                return True
        elif tIndex == len(typed):
            return False

        raise Exception("unexpected!")

 
sln=Solution()
assert False==sln.isLongPressedName(name ="pyplrz",typed="ppyypllr")
assert True==sln.isLongPressedName(name ="alex",  typed="aaleex")
assert True==sln.isLongPressedName(name ="vtkgn",typed="vttkgnn")
assert True==sln.isLongPressedName(name = "leelee", typed ="lleeelee")
assert True==sln.isLongPressedName(name = "laiden", typed ="laiden")