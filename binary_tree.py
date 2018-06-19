class Node:
  def __init__(self, val):
    self.l = None
    self.r = None
    self.val = val

class Tree:
  def __init__(self):
    self.root = None

  def get_root(self):
    return self.root

  def add(self, val):
    if self.root is None:
      self.root = Node(val)
    else:
      self._add(val, self.root)

  def _add(self, val, node):
    if val <= node.val:
      if node.l is None:
        node.l = Node(val)
      else:
        self._add(val, node.l)
    else:
      if node.r is None:
        node.r = Node(val)
      else:
        self._add(val, node.r)

  def find(self, value):
    node = self.find_help(self.root, value)
    return node

  def find_help(self, node, value):
    if node.val is value:
      return node
    elif value < node.val:
      self.find_help(node.l, value)
    elif value > node.val:
      self.find_help(node.r, value)
    else:
      return None

  def delete(self, value):
    node = self.find(value)
    if node == None:
      return None
    else:
      node.v = self.replace(node.r)

  def replace(self, node):
    if node.l is None and node.r is None:
      val = node.val
      node = None
      return val
    elif node.l != None:
      return self.replace(node.l)
    else:
      val = node.val
      node = node.r
      return val

  def print_tree(self, node):
    if node is None:
      node = self.root
    return(self.print_help(node))

  def print_help(self, node):
    print("Node->Val: ", node.val)
    if node.l != None:
      self.print_help(node.l)
    if node.r != None:
      self.print_help(node.r)
