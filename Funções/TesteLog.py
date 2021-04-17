class Log:
    def __init__(self, filename):
        self.filename = filename
        self.fp = None

    def logging(self, text):
        self.fp.write(text + '\n') # Escrever no arquivo TXT

    def __enter__(self):
        print("__enter__")  # Primeira saida
        self.fp = open(self.filename, "a+")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__")  # Terceira Saida
        self.fp.close()


with Log(r'\Users\t3163829\Desktop\Notas Televendas.txt') as logfile:
    print("Main")  # Segunda Saida
    logfile.logging("Test1")
    logfile.logging("Test2")
