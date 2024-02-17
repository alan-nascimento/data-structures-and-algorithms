from typing import List


class Group:
    def __init__(self, _name: str) -> None:
        self.name = _name
        self.groups: List[Group] = []
        self.users: List[str] = []

    def add_group(self, group: "Group") -> None:
        self.groups.append(group)

    def add_user(self, user: str) -> None:
        self.users.append(user)

    def get_groups(self) -> List["Group"]:
        return self.groups

    def get_users(self) -> List[str]:
        return self.users

    def get_name(self) -> str:
        return self.name


def is_user_in_group(user: str, group: Group) -> bool:
    if user in group.get_users():
        return True
    for sub_group in group.get_groups():
        if is_user_in_group(user, sub_group):
            return True
    return False


# Test Case 1: User exists in a nested sub-group
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

assert is_user_in_group("sub_child_user", parent) == True

# Test Case 2: User does not exist in any group
assert is_user_in_group("non_existing_user", parent) == False

# Test Case 3: Edge case where the group is empty
empty_group = Group("empty_group")
assert is_user_in_group("any_user", empty_group) == False

print("All test cases passed successfully!")
