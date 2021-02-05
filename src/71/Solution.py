class Solution:
    def simplifyPath(self, path: str) -> str:
        path_arr = path.split('/')
        path_arr = [p for p in path_arr if p != '' and p != '.']
        res_path_arr = []
        for p in path_arr:
            if p == '..':
                if len(res_path_arr):
                    res_path_arr.pop()
            else:
                res_path_arr.append(p)
        return "/" + "/".join(res_path_arr)
