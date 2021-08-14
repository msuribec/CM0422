#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.6
#  in conjunction with Tcl version 8.6
#    Aug 11, 2021 04:48:40 PM EDT  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import FourierGUI_FINAL_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    FourierGUI_FINAL_support.set_Tk_var()
    top = Toplevel1 (root)
    FourierGUI_FINAL_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    FourierGUI_FINAL_support.set_Tk_var()
    top = Toplevel1 (w)
    FourierGUI_FINAL_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("789x667+530+136")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1,  1)
        top.title("Fourier")
        top.configure(background="#ffffff")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.choiceSeries = ttk.Combobox(top)
        self.choiceSeries.place(relx=0.266, rely=0.06, relheight=0.039
                , relwidth=0.376)
        self.value_list = ['Fourier sine series','Fourier cosine series','Fourier generalized series',]
        self.choiceSeries.configure(values=self.value_list)
        self.choiceSeries.configure(textvariable=FourierGUI_FINAL_support.combobox)
        self.choiceSeries.configure(takefocus="")

        self.fEntry = tk.Entry(top)
        self.fEntry.place(relx=0.266, rely=0.195, height=24, relwidth=0.385)
        self.fEntry.configure(background="white")
        self.fEntry.configure(disabledforeground="#a3a3a3")
        self.fEntry.configure(font="TkFixedFont")
        self.fEntry.configure(foreground="#000000")
        self.fEntry.configure(highlightbackground="#d9d9d9")
        self.fEntry.configure(highlightcolor="black")
        self.fEntry.configure(insertbackground="black")
        self.fEntry.configure(selectbackground="blue")
        self.fEntry.configure(selectforeground="white")

        self.x0Entry = tk.Entry(top)
        self.x0Entry.place(relx=0.317, rely=0.285, height=24, relwidth=0.132)
        self.x0Entry.configure(background="white")
        self.x0Entry.configure(disabledforeground="#a3a3a3")
        self.x0Entry.configure(font="TkFixedFont")
        self.x0Entry.configure(foreground="#000000")
        self.x0Entry.configure(highlightbackground="#d9d9d9")
        self.x0Entry.configure(highlightcolor="black")
        self.x0Entry.configure(insertbackground="black")
        self.x0Entry.configure(selectbackground="blue")
        self.x0Entry.configure(selectforeground="white")

        self.x1Entry = tk.Entry(top)
        self.x1Entry.place(relx=0.52, rely=0.285, height=24, relwidth=0.132)
        self.x1Entry.configure(background="white")
        self.x1Entry.configure(disabledforeground="#a3a3a3")
        self.x1Entry.configure(font="TkFixedFont")
        self.x1Entry.configure(foreground="#000000")
        self.x1Entry.configure(highlightbackground="#d9d9d9")
        self.x1Entry.configure(highlightcolor="black")
        self.x1Entry.configure(insertbackground="black")
        self.x1Entry.configure(selectbackground="blue")
        self.x1Entry.configure(selectforeground="white")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.076, rely=0.195, height=26, width=101)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Function f(x)=''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.266, rely=0.285, height=26, width=21)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''x0''')

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.469, rely=0.285, height=26, width=21)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#ffffff")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''x1''')

        self.runButton = tk.Button(top)
        self.runButton.place(relx=0.101, rely=0.63, height=43, width=96)
        self.runButton.configure(activebackground="#ececec")
        self.runButton.configure(activeforeground="#000000")
        self.runButton.configure(background="#70b6b0")
        self.runButton.configure(disabledforeground="#a3a3a3")
        self.runButton.configure(font="-family {Segoe UI Black} -size 9 -weight bold")
        self.runButton.configure(foreground="#ffffff")
        self.runButton.configure(highlightbackground="#d9d9d9")
        self.runButton.configure(highlightcolor="black")
        self.runButton.configure(pady="0")
        self.runButton.configure(relief="flat")
        self.runButton.configure(text='''R U N''')
        self.runButton.bind('<ButtonRelease-1>',
                            lambda e: FourierGUI_FINAL_support.runMethod(self.choiceSeries, self.fEntry,
                                                                    self.x0Entry, self.x1Entry, self.iterationsEntry,
                                                                    self.Scrolledtext1,
                                                                    check_error,
                                                                    check_graph,
                                                                    check_print))

        self.iterationsEntry = tk.Entry(top)
        self.iterationsEntry.place(relx=0.266, rely=0.375, height=24
                , relwidth=0.132)
        self.iterationsEntry.configure(background="white")
        self.iterationsEntry.configure(disabledforeground="#a3a3a3")
        self.iterationsEntry.configure(font="TkFixedFont")
        self.iterationsEntry.configure(foreground="#000000")
        self.iterationsEntry.configure(highlightbackground="#d9d9d9")
        self.iterationsEntry.configure(highlightcolor="black")
        self.iterationsEntry.configure(insertbackground="black")
        self.iterationsEntry.configure(selectbackground="#007878d7d777")
        self.iterationsEntry.configure(selectforeground="white")

        self.Label3_1 = tk.Label(top)
        self.Label3_1.place(relx=0.051, rely=0.375, height=26, width=145)
        self.Label3_1.configure(activebackground="#f9f9f9")
        self.Label3_1.configure(activeforeground="black")
        self.Label3_1.configure(background="#ffffff")
        self.Label3_1.configure(disabledforeground="#a3a3a3")
        self.Label3_1.configure(foreground="#000000")
        self.Label3_1.configure(highlightbackground="#d9d9d9")
        self.Label3_1.configure(highlightcolor="black")
        self.Label3_1.configure(text='''Max iterations''')

        self.Scrolledtext1 = ScrolledText(top)
        self.Scrolledtext1.place(relx=0.266, rely=0.525, relheight=0.312
                , relwidth=0.518)
        self.Scrolledtext1.configure(background="white")
        self.Scrolledtext1.configure(font="TkTextFont")
        self.Scrolledtext1.configure(foreground="black")
        self.Scrolledtext1.configure(highlightbackground="#d9d9d9")
        self.Scrolledtext1.configure(highlightcolor="black")
        self.Scrolledtext1.configure(insertbackground="black")
        self.Scrolledtext1.configure(insertborderwidth="3")
        self.Scrolledtext1.configure(selectbackground="blue")
        self.Scrolledtext1.configure(selectforeground="white")
        self.Scrolledtext1.configure(wrap="none")

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.076, rely=0.285, height=26, width=107)
        self.Label4.configure(background="#ffffff")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Graphing limits''')

        check_error = tk.IntVar()
        self.checkError = tk.Checkbutton(top)
        self.checkError.place(relx=0.266, rely=0.45, relwidth=0.15
                              , relheight=0.0, height=26)
        self.checkError.configure(activebackground="#ececec")
        self.checkError.configure(activeforeground="#000000")
        self.checkError.configure(background="white")
        self.checkError.configure(disabledforeground="#a3a3a3")
        self.checkError.configure(foreground="#000000")
        self.checkError.configure(highlightbackground="#d9d9d9")
        self.checkError.configure(highlightcolor="black")
        self.checkError.configure(justify='left')
        self.checkError.configure(text='''Calculate Error''')
        self.checkError.configure(variable=check_error)

        check_graph = tk.IntVar()
        self.checkGraph = tk.Checkbutton(top)
        self.checkGraph.place(relx=0.266 + 0.16, rely=0.45, relwidth=0.08
                              , relheight=0.0, height=26)
        self.checkGraph.configure(activebackground="#ececec")
        self.checkGraph.configure(activeforeground="#000000")
        self.checkGraph.configure(background="white")
        self.checkGraph.configure(disabledforeground="#a3a3a3")
        self.checkGraph.configure(foreground="#000000")
        self.checkGraph.configure(highlightbackground="#d9d9d9")
        self.checkGraph.configure(highlightcolor="black")
        self.checkGraph.configure(justify='left')
        self.checkGraph.configure(text='''Graph''')
        self.checkGraph.configure(variable=check_graph)


        check_print= tk.IntVar()
        self.checkPrint = tk.Checkbutton(top)
        self.checkPrint.place(relx=0.266 + 0.25, rely=0.45, relwidth=0.15
                              , relheight=0.0, height=26)
        self.checkPrint.configure(activebackground="#ececec")
        self.checkPrint.configure(activeforeground="#000000")
        self.checkPrint.configure(background="white")
        self.checkPrint.configure(disabledforeground="#a3a3a3")
        self.checkPrint.configure(foreground="#000000")
        self.checkPrint.configure(highlightbackground="#d9d9d9")
        self.checkPrint.configure(highlightcolor="black")
        self.checkPrint.configure(justify='left')
        self.checkPrint.configure(text='''Print iterations''')
        self.checkPrint.configure(variable=check_print)



# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''
    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                  + tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledText(AutoScroll, tk.Text):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == '__main__':
    vp_start_gui()





