from base_read import Read_repo
from base_edit import Add_del_repo


class Choices:

    def choice1(self):

        read_repo = Read_repo()
        rooty = read_repo.root

        print("You have chosen to display a list of plants!", '\n')
        print("You are using the repository: ", rooty.tag, '\n')
        print(read_repo.read_flower())

    def choice2(self):

        read_repo = Read_repo()

        print("Do you want to learn more about the selected plant? Here you are!")
        print(read_repo.read_flower())
        print(read_repo.read_spec())

    def choice3(self):

        add_del_repo = Add_del_repo()
        print(add_del_repo.add_flower())
