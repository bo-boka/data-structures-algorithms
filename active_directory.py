
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

    print(f'group name: {group.get_name()}')

    if user in group.users:
        return True

    for g in group.get_groups():
        if is_user_in_group(user, g):
            return True
    return False


parent = Group("parent")
child = Group("child")
child_2 = Group("child_2")
child_3 = Group("child_3")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child_2)
parent.add_group(child)
parent.add_group(child_3)

print(f'user in grou?: {is_user_in_group("sub_child_user", parent)}')
