class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('Creating the instance')
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")
