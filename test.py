from PyQt5 import QtGui
from qtnodes import (Header, Node, InputKnob,
                     OutputKnob, NodeGraphWidget)

class Multiply(Node):

    def __init__(self, *args, **kwargs):
        super(Multiply, self).__init__(*args, **kwargs)
        self.addHeader(Header(node=self, text=self.__class__.__name__))
        self.addKnob(InputKnob(name="x"))
        self.addKnob(InputKnob(name="y"))
        self.addKnob(OutputKnob(name="value"))

app = QtGui.QApplication([])
graph = NodeGraphWidget()
graph.registerNodeClass(Multiply)
graph.addNode(Multiply())
graph.show()
app.exec_()