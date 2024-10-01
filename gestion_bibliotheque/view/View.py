from tabulate import tabulate
class View : 
    @staticmethod
    def afficher(data, head):
        print(tabulate(data, tablefmt="rounded_grid", headers=head))