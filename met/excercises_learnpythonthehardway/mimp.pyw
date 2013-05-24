import sys
import os
import glob
from Tkinter import *
from tkMessageBox import *
from tkFileDialog import *

# Contact the environemnt variable (if it exists) and the extension, and see
# if the result is an existing directory.  If so, return the result.  Else,
# return False.
def seeif(evar, exten, addme=False):
    if not os.environ.has_key(evar):
        return False
    path = os.environ[evar]
    if exten:
        path = path + os.sep + exten
    if os.path.isdir(path):
        if addme:
            return path + os.sep + addme
        else:
            return path
    else:
        return False

# The directory where the plugins go.
if sys.platform == 'win32':
    plugdir = False
    for p in [ ( 'USERPROFILE', '\\Desktop\\modifiers', '' ),
               ( 'HOMEPATH', '\\Desktop\\modifiers', '' ),
               ( 'SystemDrive', 'modifiers', '' ),
               ( 'USERPROFILE', '\\Desktop', 'modifiers' ),
               ( 'HOMEPATH', '\\Desktop', 'modifiers' ),
               ( 'SystemDrive', '', 'modifiers' ) ]:
        plugdir = seeif(p[0], p[1], p[2])
        if plugdir: break
    if not plugdir:
        plugdir = 'C:\\modifiers'
else:
    plugdir = os.environ['HOME'] + '/modifiers'

# Background colors.
bgcolor='#99FFDD'
abgcolor='#BBFFEE'

# Represent a pixel.  Takes a #hhhhhh for the initial value.
class Pixel:
    def __init__(self, color):
        self.r = int(color[1:3],16)
        self.g = int(color[3:5],16)
        self.b = int(color[5:7],16)

    def color(self):
        return '#%02x%02x%02x' % (self.r&0xff, self.g&0xff, self.b&0xff)

class ImageSyncError(Exception):
    def __init__(self, msg):
        self.message = msg

# Image class extending PhotoImage from Tkinter, adding convenient
# methods for getting and setting individual pixels.
class ImageBender(PhotoImage):
    # Initialize the image.  This is presumably not as generaly, but I 
    # don't know enough to fix that.  Works for what I need.
    def __init__(self, file=''):
        if file == '':
            PhotoImage.__init__(self, width=200, height=150)
            self.put(('{' + (bgcolor + ' ') * 200 + '} ' )*150, (0, 0))
        else:
            PhotoImage.__init__(self, file=file)
        self.cnys()

    # This is a Tk method omitted in Python.  Perl has it!  Nah nah nah nah
    # nah nah!  I have patterned it after  the write method in Tkinter.py
    # which sends similar arguments to Tk.  It should be portable, but if
    # it doesn't work on Windows I'll probably want to invent some new curse
    # words.
    def data(self, background=None, format=None, from_coords=None):
        """Exract image data from the image in FORMAT optionally selecting
        the region in FROM_COORDS replacing transparent pixels with 
        BACKGROUND.  from_coords is (x.y) starting loc, or (x1,y1,x2,y2)
        region, excluding the limit"""
        args = (self.name, 'data')
        if background:
            args = args + ('-background', background)
        if format:
            args = args + ('-format', format)
        if from_coords:
            args = args + ('-from',) + tuple(from_coords)
        return self.tk.call(args)

    # Load the image data into a Python list structure.  Eccch.  But
    # going through Tk a pixel at a time is tooooo sssssllllllooooooowwwwwww
    # Data is loaded in (and out) a row at a time.  That may turn out to have
    # just barely acceptable performance.
    def cnys(self):
        try:
            self.idat = []
            for row in range(0,self.height()):
                # For each row, we get the row data from Tk which is a string
                # { #hhhhhh .... }.  In the last stmt, the { } are removed,
                # the pixels are split, and each is converted into a an
                # integer.  This list of integers for the row is appended to
                # self.idat, a list of the row lists.
                rowdat = self.data(background=bgcolor,
                                   from_coords=(0, row, self.width(), row + 1))
                left = rowdat.find('{')
                right = rowdat.find('}')
                if left < 0 or right < 0:
                    raise ImageSyncError("Format: Missing { or }")
                self.idat.append(map((lambda x: Pixel(x)),
                                     rowdat[left+1:right].split()))
        except Exception, e:
            showerror('Internal Error', 'Image sync failed: ' + str(e))
            throw

    # Load changes made to the Python image data into the image itself.  This
    # is a duzey, which packs the entire modified image data as a string and
    # sends it to self.put, which updates the image with the new data.
    def sync(self):
        self.put(' '.join(map((lambda row: '{'+ ' '.join
                      (map((lambda x: x.color()),row)) + '}'), self.idat)))

# File open.
def getfile():
    global pic
    fn = askopenfilename(filetypes=[("GIF files", '.gif')])
    root.update()
    if fn:
        try:
            lpic = ImageBender(file=fn)
        except:
            showwarning("Open Failed", 'Unable to open ' + fn)
            return
        pic = lpic
        ilab.configure(image=pic)

# File save
def savefile():
    global pic
    fn = asksaveasfilename(filetypes=[("GIF files", '.gif')])
    root.update()
    if fn:
        try:
            pic.write(fn, format='GIF')
        except:
            showwarning("Save Failed", 'Unable to save to ' + fn)
            return

# Exit
def quit():
    root.quit()

root = Tk()
root.title('Pluggable Image Manipulation')
bgframe = Frame(root, bg=bgcolor)
bgframe.grid(row=0,column=0)

# Create the standard file menu (though we don't fill it up 'till later).
top = Menu(bgframe, bg=bgcolor, activebackground=abgcolor)
root.config(menu=top)

# Create the empty image.
pic = ImageBender()

# Create and grid a button for the image modification functions.
def runmod(m):
    try:
	m.modify(pic)
    except Exception, e:
        showerror('Modify Failed', 'Modify operation failed: ' + str(e));
    else:
        pic.sync()

def mkbut(r, c, lab, module):
    ret = Button(bgframe, text=lab, 
                 command=lambda m=module: runmod(m),
                 bg=bgcolor, activebackground=abgcolor)
    ret.grid(row=r, column=c, sticky='news')

    return ret

# This maps extension modules to module objects.
modlist = { }

# Load the extension modules.
def loadmods():
    global modlist, nextmod, plugdir

    # Update the search path 
    oldpath = sys.path
    sys.path = [ plugdir ] + sys.path

    # Load the modules.  Make a list of them, the tuple (name, label, sortkey)
    # for each one.
    mods = [ ]
    for m in glob.glob(plugdir + os.sep + '*.py'):
        mod = m[m.rfind(os.sep)+1:]
        mod = mod[:mod.rfind('.py')]

        # If it is already in our list, we'll reload.
        if modlist.has_key(mod):
            try:
		reload(modlist[mod])
            except Exception, e:
                showerror('Plugin Reload Failed', 'Reload of ' + mod + 
                          ' extension failed: ' + str(e))
                continue
        else:
            try:
		modlist[mod] = __import__(mod)
            except Exception, e:
                showerror('Plugin Load Failed', 'Load of ' + mod + 
                          ' extension failed: ' + str(e))
                continue;
        try:
	    label = modlist[mod].label
        except:
            label = mod
        try:
	    seq = modlist[mod].ordinal
        except:
            seq = 999999
        sortkey = "%06d.%s" % (seq, label.lower())
        mods.append((modlist[mod],label,sortkey))

    # Restore the module search path.
    sys.path = oldpath

    ncol = 3
    if ncol > len(mods): ncol = len(mods)
    if ncol == 0: ncol = 1

    # Create the buttons for them
    mods.sort(key=lambda x: x[2])
    row = 1
    col = 0
    buts = [ ]
    for b in mods:
        buts.append(mkbut(row, col, b[1], b[0]))
        col = col + 1
        if col == ncol:
            row = row + 1
            col = 0

    return (ncol, buts)

(ncol, buts) = loadmods();

# Reload the modules
def modrel():
    global ncol, buts

    for b in buts:
        b.destroy()
    (ncol, buts) = loadmods();
    ilab.grid(row=0, column=0, columnspan=ncol)

# Action for setting the Modifiers directory.
def setmodloc():
    global plugdir
    fn = askdirectory(initialdir=plugdir)
    if fn:
        plugdir = fn
        modrel()

# Menu bar contents
fmenu = Menu(top, bg=bgcolor, activebackground=abgcolor)
fmenu.add_command(label='Open...', command=getfile, underline=0)
fmenu.add_command(label='Save...', command=savefile, underline=0)
fmenu.add_command(label='Exit', command=quit, underline=0)
top.add_cascade(label='File', menu=fmenu, underline=0)

pmenu = Menu(top, bg=bgcolor, activebackground=abgcolor)
pmenu.add_command(label='Reload', command=modrel, underline=0)
pmenu.add_command(label='Location...', command=setmodloc, underline=0)
top.add_cascade(label='Modifiers', menu=pmenu, underline=0)

# Display the image
ilab = Label(bgframe, image=pic)
ilab.grid(row=0, column=0, columnspan=ncol)

class DispLabel(Label):
    """ A label which shows a string of the form name=value, where the
        value is an integer """
    def __init__(self, parent, name, val):
        Label.__init__(self, parent, bg=bgcolor, width=10)
        self.name = name
        self.set(val)
    def set(self, val):
        self.config(text = "%s=%d" % (self.name, val))

cpop = None
class CPop(Toplevel):
    """Color description window.  Describes the color when the user clicks.
       Intended for there to be zero on one instance, stored in global cpop."""
    def mklab(self, name, val, rw, cl, stk):
        "Private.  Make a value-describing label"
        ret = DispLabel(self, name, val) 
	ret.grid(row=rw, column=cl, sticky=stk)
	return ret
    def __init__(self, row, col, r, g, b):
    	"Initialize with a particular position and color."
        Toplevel.__init__(self)
	self.title("Color")
        self.rowlab = self.mklab("row", row, 0, 0, 'e')
        self.collab = self.mklab("col", col, 1, 0, 'e')
	self.redlab = self.mklab("red", r, 0, 1, 'w')
	self.greenlab = self.mklab("green", g, 1, 1, 'w')
	self.bluelab = self.mklab("blue", b, 2, 1, 'w')
	self.colorlab = Label(self, background=("#%02x%02x%02x" %(r,g,b)))
        self.colorlab.grid(row=2, column=0,sticky='news')
        Button(self, text="Ok", command=self.drop,
               bg=bgcolor, activebackground=abgcolor,).\
               		grid(row=3,column=0,columnspan=2,sticky='news')

        global cpop
        cpop = self
    def set(self, row, col, r, g, b):
        "Set to a new position and color"
        self.rowlab.set(row)
        self.collab.set(col)
	self.redlab.set(r)
	self.greenlab.set(g)
	self.bluelab.set(b)
	self.colorlab.config(background=("#%02x%02x%02x" %(r,g,b)))

    def drop(self):
        "Bye."
        global cpop
	cpop = None
        self.destroy()

# Describe the pixel you clicked.
def colorpop(e):
    "Pops up a dialog giving the color at the selected location"
    row = e.y - int(str(ilab.cget('pady')))
    col = e.x - int(str(ilab.cget('padx')))
    if row < pic.height() and col < pic.width():
        global cpop
        if cpop == None:
            cpop = CPop(row, col, pic.idat[row][col].r,
                        pic.idat[row][col].g, pic.idat[row][col].b)
        else:
            cpop.set(row, col, pic.idat[row][col].r,
                     pic.idat[row][col].g, pic.idat[row][col].b)

ilab.bind("<Button-1>", colorpop)

root.mainloop()
