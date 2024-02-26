class Printer:
    def print_document(self):
        pass


class Scanner:
    def scan_document(self):
        pass


class Fax:
    def fax_document(self):
        pass


class MultiFunctionPrinter(Printer, Scanner, Fax):
    def __init__(self, Model):
        self.Model = Model

    def print_document(self):
        print(f"{self.Model} Printing document...")

    # No need to redefine scan_document and fax_document methods here


mfp = MultiFunctionPrinter("Canon")
mfp.print_document()  # Output: Printing document...
