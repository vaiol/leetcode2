class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.map = dict()
        for i in range(length):
            self.map[f'{i}_{self.snap_id}'] = 0
            self.map[f'{i}_snaps'] = [self.snap_id]
        

    def set(self, index: int, val: int) -> None:
        if f'{index}_{self.snap_id}' not in self.map:
            self.map[f'{index}_snaps'].append(self.snap_id)
        self.map[f'{index}_{self.snap_id}'] = val
        
        
        

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1
        
    def get_prev_snap_id(self, index: int, snap_id: int) -> int:
        snaps = self.map[f'{index}_snaps']
        left, right = 0, len(snaps) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if snaps[mid] >= snap_id:
                right = mid - 1
            else:
                left = mid + 1
        return snaps[right]
                

    def get(self, index: int, snap_id: int) -> int:
        if f'{index}_{snap_id}' in self.map:
            return self.map[f'{index}_{snap_id}']
        prev_snap_id = self.get_prev_snap_id(index, snap_id)
        # print(index, prev_snap_id)
        # print(self.map[f'{index}_snaps'])
        return self.map[f'{index}_{prev_snap_id}']
        
            
            
        
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)