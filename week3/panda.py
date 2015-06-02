class Panda:
    def __init__(self, name, email, gender):
        self.name = name
        self.email = email
        self.gender = gender

    def __name__(self):
        return self.name

    def __email__(self):
        return '@' in self.email and '.' in self.email

    def __gender__(self):
        return self.gender

    def __isMale__(self):
        return self.gender == "male"

    def __isFemale__(self):
        return self.gender == "female"

    def __eq__(self, other):
        return self.name == other.name and self.email == other.email and self.gender == other.gender

    def __hash__(self):
        return hash(str(self.name))

ivo = Panda(ivo asd@afd.fd 15)

class PandaSocialNetwork:

    def __init__(self):
        self.network = {}

    def has_panda(self, panda):
        return panda in self.network

    def __add_panda__(self, panda):
        if panda in self.network:
            print("Panda_already_in!")
        else:
            self.network[panda] = []

    def __make_friends__(self, panda1, panda2):
        if has_panda(panda1):
            self.add_panda(panda1)

        if has_panda(panda2):
            self.add_panda(panda2)

        if panda2 not in self.network[panda1]:
            self.network[panda1].append(panda2)
            self.network[panda2].append(panda1)
        else:
            print("already friends!")

    def __are_friends__(self,panda1,panda2):
        return panda1 in self.network[panda2]

    def __friends_of__(self,panda):
        if panda not in self.network:
            return False
        else:
            return self.network[panda]

    def __connection_level__(self, panda1,panda2):
        mass = []
        mass2 = []
        count = 0
        len_netw = len(self.network)
        while len_netw:
            mass.append(panda1)
            mass2 = [panda in self.network[panda1]]
            if panda2 not in mass2:
                mass2_len = len(mass2)
                for i in self.network[mass2[1:mass2_len]]:
                    for j in mass:
                        if i != j:
                            mass2.append(i)
                len_netw -= mass2_len

        return count

    def __are_connected__(panda1,panda2):
        pass

    def __how_many_gender_in_network(level,panda,gender):
        pass

