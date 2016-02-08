import wx

class Deduplicator(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Deduplicator, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):

        menubar = wx.MenuBar()

        fileMenu = wx.Menu()
        qmi = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+W')
        fileMenu.AppendItem(qmi)

        self.Bind(wx.EVT_MENU, self.OnQuit, qmi)

        menubar.Append(fileMenu, '&File')

        self.SetMenuBar(menubar)
        self.SetSize((350, 250))
        self.SetTitle('Deduplicator')
        self.Centre()
        self.Maximize()
        self.Show(True)

    def OnQuit(self, e):
        self.Close()

def main():

    app = wx.App()
    Deduplicator(None)
    x = app.MainLoop()
    print x

if __name__ == '__main__':
    main()
