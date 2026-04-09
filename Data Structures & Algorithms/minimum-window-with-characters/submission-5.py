class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        t_map = {}
        
        for c in t:
            t_map[c] = 1 + t_map.get(c, 0)
        
        need = len(t_map)
        have = 0
        s_map = {}
        l = 0
        res = [1001, 1001]
        res_len = 1001

        for r in range(len(s)):
            s_map[s[r]] = 1 + s_map.get(s[r], 0)
            
            if s[r] in t_map and s_map[s[r]] == t_map[s[r]]:
                have += 1

            while have == need:
                if r - l + 1 < res_len:
                    res_len = r - l + 1
                    res = [l, r]

                s_map[s[l]] -= 1
                if s[l] in t_map and s_map[s[l]] < t_map[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if res_len != 1001 else ""

