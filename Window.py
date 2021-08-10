import wx
import wx.grid as gridlib
from wx.grid import GridCellAutoWrapStringRenderer
from Operation import Operation
import csv
from datetime import datetime

 
class Window(wx.Frame):
     
    def __init__(self):
        wx.Frame.__init__(self, None, title="Power Method for Page Rank", style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX), size= (640,480))
        self.Center()
        p = wx.Panel(self)
       
        box = wx.StaticBox(p, wx.ID_ANY, "Control Panel",  pos=(5,0),size=(630, 200))
        
        lblList = ['Random Stochastic Matrix', 'Comma-Separated Values (CSV) File']     
        self.rbox = wx.RadioBox(box,label = 'Select the matrix source', pos = (10,10), choices = lblList ,  majorDimension = 1, style = wx.RA_SPECIFY_COLS)
       
        self.rbox.Bind(wx.EVT_RADIOBOX,self.radioBox)
       
        self.btn1 = wx.Button(box, label = "Open a File", pos=(290,50)) 
        self.btn1.Bind(wx.EVT_BUTTON, self.OnClick) 
        self.btn1.Disable()
        self.lbl1 = wx.StaticText(box, -1, 'Number of Iterations:', pos =(10,100))
        self.txt1 = wx.TextCtrl(box, style=wx.TE_LEFT, size=(70, -1), name = "txt1", pos = (150,95))
        self.txt1.SetMaxLength(6)
        self.txt1.Bind(wx.EVT_CHAR, self.block_non_numbers)
        self.txt2 = wx.TextCtrl(box, style=wx.TE_LEFT| wx.TE_READONLY, size=(230, -1),pos=(390,50), name= "txt2")
        self.txt2.Disable()
        self.lbl2 = wx.StaticText(box, -1, 'Square Matrix Size:', pos =(290,25))
        self.txt3 = wx.TextCtrl(box, style=wx.TE_LEFT, size=(40, -1), pos = (420,17))
        self.txt3.Bind(wx.EVT_CHAR, self.block_non_numbers)
        self.txt3.SetMaxLength(2)
        self.btn2 = wx.Button(box, label='Execute',size=(70, -1), pos=(150, 140))
        self.btn2.Bind(wx.EVT_BUTTON, self.press)
        self.btn3 = wx.Button(box, label = "Export to CSV", pos=(530,140)) 
        self.btn3.Bind(wx.EVT_BUTTON, self.export) 
        
        #grid
        self.grid = gridlib.Grid(p,-1,pos=(5,220))
        self.grid.SetDefaultRenderer(GridCellAutoWrapStringRenderer())
        self.grid.CreateGrid(1, 2)
        self.grid.SetColLabelValue(0, "Iteration")
        self.grid.SetColLabelValue(1, "Values")
      
        
        self.grid.SetCellValue(0,0,"Empty")
        self.grid.SetCellValue(0,1,"Empty")
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(box, 1, wx.EXPAND)
        sizer.Add(self.grid, 2, wx.EXPAND)
        p.SetSizer(sizer) 
     
     
    def export(self,e):
        with open('iteration_' + str(datetime.now()) +'.csv', 'w') as csvfile:
            fieldnames = ['Iteration', 'Values']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for i in range(self.grid.GetNumberRows()):
                    writer.writerow({'Iteration': self.grid.GetCellValue(i,0), 'Values': self.grid.GetCellValue(i,1)})
            wx.MessageBox("A CSV file was created successfully!", "Info", wx.OK | wx.ICON_INFORMATION)
    def press(self,e): 
        
        if self.rbox.GetSelection() == 0:
            if self.txt1.GetValue() == '' and self.txt3.GetValue() == '':
                wx.MessageBox("The number of iterations and square matrix size are empty!", "Info", wx.OK | wx.ICON_INFORMATION)
            elif self.txt1.GetValue() == '':
                wx.MessageBox("The number of iterations is empty!", "Info", wx.OK | wx.ICON_INFORMATION)
            elif self.txt3.GetValue() == '':
                wx.MessageBox("The square matrix size is empty!", "Info", wx.OK | wx.ICON_INFORMATION)
            elif self.txt1.GetValue() != '' and self.txt3.GetValue() != '':
                operation = Operation(int(self.txt1.GetValue()),int(self.txt3.GetValue()))
                result =operation.powerMethod()
                if result == False:
                    wx.MessageBox("The matrix is not stochastic!", "Info", wx.OK | wx.ICON_INFORMATION)
                else:
                    self.refreshGrid(self.grid.GetNumberRows(),int(self.txt1.GetValue()),operation.getIteration())
                    self.grid.SetColSize(1, 470)
             
        elif self.rbox.GetSelection() == 1:
            if self.txt1.GetValue() == '' and self.txt2.GetValue() == '':
                wx.MessageBox("The number of iterations and filename are empty!", "Info", wx.OK | wx.ICON_INFORMATION)
            elif self.txt1.GetValue() == '':
                wx.MessageBox("The number of iterations is empty!", "Info", wx.OK | wx.ICON_INFORMATION)
            elif self.txt2.GetValue() == '':
                wx.MessageBox("The filename is empty!", "Info", wx.OK | wx.ICON_INFORMATION)
            elif self.txt1.GetValue() != '' and self.txt2.GetValue() != '':
                operation = Operation(int(self.txt1.GetValue()),self.txt2.GetValue())
                result = operation.powerMethod()
                if result == False:
                    wx.MessageBox("The matrix is not stochastic!", "Info", wx.OK | wx.ICON_INFORMATION)
                else:
                    self.refreshGrid(self.grid.GetNumberRows(),int(self.txt1.GetValue()),operation.getIteration())
                    self.grid.SetColSize(1, 470)
               
    def refreshGrid(self,nRows, iteration, data ):

        current, new = (nRows, iteration)

        if new < current:
            #- Delete rows:
            self.grid.DeleteRows(0, current-new, True)

        if new > current:
            #- append rows:
            self.grid.AppendRows(new-current)

        #- Populate the grid with new data:
        for i in range(len(data)):
            self.grid.SetCellValue(i, 0, str(i+1))
            str1 = "["
            # traverse in the string   
            for ele in data[i][0]:  
              
                str1 += str(ele)+ " ; "  
            str1 = str1[:len(str1)-2] + "]"
            self.grid.SetCellValue(i, 1, str1)
            
        
    def radioBox(self,event):
        if self.rbox.GetSelection() == 0:
            self.txt3.Enable()
            self.txt2.Disable()
            self.txt2.SetValue("")
            self.txt1.SetValue("")
            self.txt3.SetValue("")
            self.btn1.Disable()
        elif self.rbox.GetSelection() == 1:
            self.txt3.Disable()
            self.txt2.Enable()
            self.btn1.Enable()
            self.txt1.SetValue("") 
            self.txt2.SetValue("")
            self.txt3.SetValue("")
            
    def block_non_numbers(self,event):
        key_code = event.GetKeyCode()

        # Allow ASCII numerics
        if ord('0') <= key_code <= ord('9'):
            event.Skip()
            return

        # Allow delete
        if key_code == ord('8'):
            event.Skip()
            return

        # Block everything else
        return

      
    def OnClick(self, e): 
        # otherwise ask the user what new file to open
        with wx.FileDialog(self, "CSV file", wildcard="CSV files (*.csv)|*.csv",
                       style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return     # the user changed their mind

            # Proceed loading the file chosen by the user
            pathname = fileDialog.GetPath()
            children = self.GetChildren()
            for uChild in children:
                if isinstance(uChild,wx.Panel):
                    children =  uChild.GetChildren() 
                    for child in children:
                        if isinstance(child, wx.StaticBox):
                            children = child.GetChildren()
                            for nChild in children:
                                if isinstance(nChild, wx.TextCtrl):
                                    if nChild.GetName() == "txt2":
                                        nChild.SetValue(pathname)
