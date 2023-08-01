#%%
class TreeNode():
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        current_parent = self.parent
        while current_parent:
            current_parent = current_parent.parent
            level += 1

        return level

    def print_tree(self):
        current_level = self.get_level()
        blanks = ' ' * current_level * 2 + '|--' if self.parent else ""
        print(blanks + self.data)
        for child in self.children:
            child.print_tree()

#%%

names_list = ["Hashirama",
              "Sarutobi",
              "Orochimaru",
              "Jiraya",
              "Tsunade",
              "Shizune",
              "Kabuto",
              "Sasuke",
              "Minato",
              "Sakura",
              "Kakashi",
              "Naruto"
              ]


# %%

tree_dict = {}

for name in names_list:

    tree_dict[name] = TreeNode(name)


# %%

tree_dict["Hashirama"].add_child(tree_dict["Sarutobi"])
tree_dict["Sarutobi"].add_child(tree_dict["Orochimaru"])
tree_dict["Sarutobi"].add_child(tree_dict["Jiraya"])
tree_dict["Sarutobi"].add_child(tree_dict["Tsunade"])
tree_dict["Orochimaru"].add_child(tree_dict["Kabuto"])
tree_dict["Jiraya"].add_child(tree_dict["Minato"])
tree_dict["Minato"].add_child(tree_dict["Kakashi"])
tree_dict["Kakashi"].add_child(tree_dict["Naruto"])
tree_dict["Kakashi"].add_child(tree_dict["Sakura"])
tree_dict["Kakashi"].add_child(tree_dict["Sasuke"])
tree_dict["Tsunade"].add_child(tree_dict["Shizune"])


# %%

tree_dict["Hashirama"].print_tree()

#%%