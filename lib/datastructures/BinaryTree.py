from typing import Self, Any

"""
Unbalanced binary tree
"""

class BinaryTree:
  datum: Any
  left: Self | None = None
  right: Self | None = None

  def __init__(self, datum: Any) -> None:
    self.datum = datum

  def __lt__(self, other: Self) -> bool:
    return self.datum < other.datum

  def addNode(self, datum: str) -> Self:
    node = BinaryTree(datum)
    branch = self
    while datum < branch.datum:
      if branch.left:
        branch = branch.left
      else:
        break
    while datum > branch.datum:
      if branch.right:
        branch = branch.right
      else:
        break

    if datum < branch.datum:
      branch.left = node
    if datum > branch.datum:
      branch.right = node

    return node

  def __str__(self) -> str:
    return f"{self.datum} : [ L:{self.left} ^ R:{self.right} ]"


if __name__ == "__main__":
  def dfs(tree, depth=0):
    if tree.left:
      dfs(tree.left, depth + 1)

    print(f"{depth * "--"}{tree.datum}")

    if tree.right:
      dfs(tree.right, depth + 1)


  def bfs(tree, depth=0):
    q = [(tree, depth)]
    while q:
      (branch, depth), q = q[0], q[1:]
      print(f"{depth * "--"}{branch.datum}")
      if branch.left:
        q.append((branch.left, depth + 1))
      if branch.right:
        q.append((branch.right, depth + 1))


  root = BinaryTree((64, "^root"))

  root.addNode((32, "<left"))
  root.addNode((96, ">right"))

  root.addNode((16, "<left <left"))
  root.addNode((48, "<left >right"))
  root.addNode((80, ">right <left"))
  root.addNode((112, ">right >right"))

  print("Binary tree")
  print(root)

  print("DFS")
  dfs(root)

  print("BFS")
  bfs(root)
