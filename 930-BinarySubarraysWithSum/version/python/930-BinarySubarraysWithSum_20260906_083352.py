# Last updated: 9/6/2026, 8:33:52 AM
1class Codec:
2    def serialize(self, root):
3        if not root: return "#"
4        return str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right)
5    
6    def deserialize(self, data):
7        vals = iter(data.split(","))
8        def build():
9            v = next(vals)
10            if v == "#": return None
11            node = TreeNode(int(v))
12            node.left = build()
13            node.right = build()
14            return node
15        return build()