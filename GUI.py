from Tkinter import *
from ttk import Frame, Label, Entry, Button
from CDPMatcher import patternMatcher
from DNAMatcher import DNAMatch
from tkFileDialog import askopenfilename
from tkFileDialog import asksaveasfile
import plotly
import plotly.graph_objs as go
import plotly.tools as tls

tls.set_credentials_file('tezivanovic', 'yBwgXttg6ATSQtFrD2iK')
'''Creates a simple GUI for the user to use'''

class GUI(Frame):
    text = ""
    pattern = ''
    variable = 0
    dnabool = False
    onlymatch = []
    onlyResults = []
    indexresults = []
    dictresults = {}

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        #elf.launch()
        self.initUI()
        self.buttonPattern = Button
        self.buttonSequence = Button
        self.entrySequence = Entry
        self.entryPattern = Entry
        self.entryVariable = Entry
        self.okButton = Button
        self.closeButton =Button

    def initDNA(self):
        self.dnabool = True
        frame = Frame(self)
        frame.pack(fill=BOTH, expand=True)

    def plotScatter(self):
        trace1 = go.Scatter(
            # y=self.dictresults.keys(),
            y=self.onlyResults, mode='markers'

        )
        data = [trace1]
        plotly.offline.plot(data)

    '''Initiates GUI with buttons, entry boxs lables and functions'''
    def initUI(self):

        def noFile():
            toplevel = Toplevel()
            label1 = Label(toplevel, text="please select file")
            label1.pack()

        def importFile():
            filename = askopenfilename(parent=self.parent)
            if filename:
                f = open(filename)
                self.text = f.read()
                self.entrySequence.insert(txt, 0, filename)
            else:
                noFile()
                raise ImportError

        def importPattern():
            filename = askopenfilename(parent=self.parent)
            if filename:
                f = open(filename)
                self.pattern = f.read()
                self.entryPattern.insert(entry1, 0, filename)
            else:
                noFile()
                raise ImportError

        def launchDNAIU():
            self.initDNA()
            buttonDNA.config(state="disabled")
            buttonPattern.config(state="disabled")
            entry1.config(state="disabled", text="DNA patterns in use")

        def onButtonClick():
            pm = {}

            def match():
                if self.text:
                    pm = DNAMatch(self.text)
                    self.onlymatch = pm.onlymatch
                    self.dictresults = pm.results
                    self.onlyResults = pm.fullset
                    self.indexresults = pm.indexset
                    quit()
                elif txt:
                    self.text = txt.get()
                    if len(self.text) < 1:
                        raise ValueError("Input sequence // or Import file")
                    elif len(self.text) < len(self.pattern):
                        raise AttributeError("Pattern longer than sequence")

            def normMatch():
                    self.variable = int(variable.get())
                    self.text = txt.get()
                    self.pattern = entry1.get()

                    if len(self.text) < 1:
                        raise ValueError('input a sequence')
                    if len(self.pattern) < 1:
                        raise ValueError('input a pattern')
                    print 'The Sequence ' + self.text
                    print 'Searching for pattern ' + self.pattern
                    pm = patternMatcher(self.pattern, self.text, self.variable)
                    self.onlymatch = pm

                    if not self.dictresults:
                        self.dictresults.setdefault(1)

            if self.dnabool:
                match()
            else:
                normMatch()

            self.newFrame()
            #plotScatter()

        def quit():
            self.parent.destroy()

        buttonDNA = Button(self, text="Check DNA sequence", command=launchDNAIU)
        buttonDNA.pack(fill=X, padx=5, pady=5)

        self.parent.title("Conservative Degenerate Pattern Matcher")
        self.pack(fill=BOTH, expand=True)

        frame1 = Frame(self)
        frame1.pack(fill=X, padx=5, pady=5)

        lbl1 = Label(frame1, text="Pattern", width=7)
        lbl1.pack(side=LEFT, padx=5, pady=5)

        self.entryPattern = entry1 = Entry(frame1, text="INPUT PATTERN HERE")
        entry1.pack(fill=X, padx=5, expand=True)

        self.buttonPattern = buttonPattern = Button(self, text="Import pattern", command=importPattern)
        buttonPattern.pack(fill=X, padx=5, pady=5)

        frame2 = Frame(self)
        frame2.pack(fill=X, padx=5, pady=5)

        lbl2 = Label(frame2, text="Upper Bound", width=9)
        lbl2.pack(side=LEFT, padx=5, pady=5)

        variable = self.entryVariable = Entry(frame2)
        variable.pack(fill=X, padx=5, pady=5)

        frame3 = Frame(self)
        frame3.pack(fill=X, expand=True, padx=5, pady=5)

        lbl3 = Label(frame3, text="Sequence", width=7)
        lbl3.pack(side=LEFT, anchor=N, padx=5, pady=5)

        self.entrySequence = txt = Entry(frame3)
        txt.pack(fill=BOTH, pady=5, padx=5, expand=True)

        self.buttonSequence = buttonImport = Button(self, text="Import sequence file", command=importFile)
        buttonImport.pack(fill=X, padx=5, pady=5)

        closeButton = self.closeButton = Button(self, text="Close", command=quit)
        closeButton.pack(side=RIGHT, padx=5, pady=5)

        okButton = self.okButton = Button(self, command=onButtonClick, text="OK")
        okButton.pack(side=RIGHT, padx=5, pady=5)

    def newFrame(self):

        def exportResults():
            filename = asksaveasfile(mode="w")
            if filename:
                filename.write(str(self.onlymatch))
                filename.close()

        window = Toplevel().title("Results")
        frame1 = Frame(window)
        frame1.pack(fill=X, expand=True)
        label1 = Label(window, text="There were " + len(self.dictresults.keys()).__str__()+
                                    " different patterns matched")
        label1.pack()
        text = Text(window)
        text.insert(INSERT, "{}".format(self.indexresults))
        text.insert(END, "{}".format(self.onlymatch)+"These are all indexes where positive matches occured")
        text.pack()

        buttonExport = Button(window, text="Export Results", command=exportResults)
        buttonExport.pack(side=BOTTOM, pady=5, padx=5)

        buttonGraph = Button(window, text="Load Graph", command=self.plotScatter)
        buttonGraph.pack(side=BOTTOM, pady=5, padx=5)


def main():
    root = Tk()
    app = GUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()
