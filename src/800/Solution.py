class Solution:
    def similarRGB(self, color: str) -> str:
        init_r, init_g, init_b = int(color[1:3], base=16), int(color[3:5], base=16), int(color[5:7], base=16)
        def get_closest(x: int) -> int:
            ans = 0
            min_dis = float('inf')
            for i in range(16):
                dis = (x - i * 17) ** 2
                if dis < min_dis:
                    ans = i
                    min_dis = dis
            return ans
        
        def to_hex(x: int) -> int:
            return hex(x)[-1] * 2
        
        r, g, b = get_closest(init_r), get_closest(init_g), get_closest(init_b)
    
        return f'#{to_hex(r)}{to_hex(g)}{to_hex(b)}'
                    
                    