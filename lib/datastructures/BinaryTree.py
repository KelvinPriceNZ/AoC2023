from typing import Self

class BinaryTree:
  label: str
  cond: bool
  left: Self | None = None
  right: Self | None = None

  def __init__(self, label: str, cond: bool) -> Self:
    self.label = label
    self.cond = cond

  def addNode(self, label: str, cond: bool) -> None:
    node = BinaryTree(label, cond)
    if cond:
      self.left = node
    else:
      self.right = node

  def __str__(self) -> str:
    return f"{self.label} : [ L:{self.left} ^ R:{self.right} ]"


if __name__ == "__main__":
  def dfs(tree, depth=0):
    print(f"{depth * "--"}{tree.label}")

    if tree.left:
      dfs(tree.left, depth + 1)
    if tree.right:
      dfs(tree.right, depth + 1)


  def bfs(tree, depth=0):
    q = [(tree, depth)]
    while q:
      (branch, depth), q = q[0], q[1:]
      print(f"{depth * "--"}{branch.label}")
      if branch.left:
        q.append((branch.left, depth + 1))
      if branch.right:
        q.append((branch.right, depth + 1))


  t = BinaryTree("root", "a>2000")

  t.addNode("left", True)
  t.addNode("right", False)

  t.left.addNode("left.left", True)
  t.left.addNode("left.right", False)
  t.right.addNode("right.right", False)
  t.right.addNode("right.left", True)

  print("Binary tree")
  print(t)

  print("DFS")
  dfs(t)

  print("BFS")
  bfs(t)
