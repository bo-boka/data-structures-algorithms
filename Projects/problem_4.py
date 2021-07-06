

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    if user in group.users:
        return True

    for g in group.get_groups():
        if is_user_in_group(user, g):
            return True
    return False


# Test case 1
print('======== Test 1: Happy Path')
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

print(f'user in group?: {is_user_in_group("sub_child_user", parent)}')      # True


# Test case 2
print('======== Test 2: Multiple children, user in middle child group')
parent_1 = Group("parent")
child_1 = Group("child")
child_1_2 = Group("child_2")
child_1_3 = Group("child_3")
sub_child_1 = Group("subchild")

sub_child_1_user = "sub_child_user"
sub_child_1.add_user(sub_child_user)

child_1_2.add_group(sub_child)
parent_1.add_group(child_1)
parent_1.add_group(child_1_2)
parent_1.add_group(child_1_3)

print(f'user in group?: {is_user_in_group("sub_child_user", parent_1)}')    # True


# Test case 3
print('======== Test 3: No user found')
parent_1 = Group("parent")
child_1 = Group("child")
child_1_2 = Group("child_2")
child_1_3 = Group("child_3")
sub_child_1 = Group("subchild")

sub_child_1_user = "sub_child_user"
sub_child_1.add_user(sub_child_user)

child_1.add_group(sub_child)
parent_1.add_group(child_1_2)
parent_1.add_group(child_1)
parent_1.add_group(child_1_3)

print(f'user in group?: {is_user_in_group("non-existent_user", parent_1)}')     # False


# Test case 4
print('======== Test 4: user has no parent')
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

parent_user = "parent_user"
parent.add_user(parent_user)

child.add_group(sub_child)
parent.add_group(child)

print(f'user in group?: {is_user_in_group("parent_user", parent)}')      # True
