#!/bin/python

import os
import array

import subprocess

from argparse import ArgumentParser

import matplotlib.pyplot as plt
import threading

from straintables import Viewer, OutputFile, alignmentData, Definitions
from straintables.Viewer import mapBar

from matplotlib.backends.backend_gtk3agg import FigureCanvas
from matplotlib.backends.backend_gtk3 import (
    NavigationToolbar2GTK3 as NavigationToolbar)

import time

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf

Description = """
straintables' visualization tool.
This will read an output directory from the pipeline and build
navigable dissimilarity matrices for matched regions.

"""


class locusNamesSelectionMenu(Gtk.Grid):
    def __init__(self, matrixViewer):

        Gtk.Grid.__init__(self)
        self.matrixViewer = matrixViewer

        self.optsAllLoci = Gtk.ListStore(str)
        self.left_choice =\
            Gtk.ComboBox.new_with_model_and_entry(self.optsAllLoci)

        self.right_choice =\
            Gtk.ComboBox.new_with_model_and_entry(self.optsAllLoci)

        self.switchAutomaticDropdownLocusJump(Target=True)

        self.left_choice.set_entry_text_column(0)

        self.right_choice.set_entry_text_column(0)

        Refresh = Gtk.Button(label=".")
        Refresh.connect("clicked", self.Refresh)

        # w = Gtk.Button.new(Gdk.RGBA(100,100,100,100))
        # btn = ColoredButton()
        # btn.changeColor("red")
        btn = Gtk.Label.new("<-")
        self.attach(btn, 0, 0, 1, 1)
        self.attach(self.left_choice, 1, 0, 1, 1)
        # self.attach(Refresh, 2, 0, 1, 1)
        self.attach(self.right_choice, 3, 0, 1, 1)
        self.attach(Gtk.Label.new("->"), 4, 0, 1, 1)

        self.allLoci = None
        self.show_all()

    def Refresh(self, n):
        print(self.matrixViewer.figure)

        LOCI = [
            self.left_choice.get_active(),
            self.right_choice.get_active()
        ]

        self.matrixViewer.changeView(LOCI, self.matrixViewer.drawPlot)

    def Update(self, n=None):
        if self.matrixViewer.alnData:
            self.allLoci = self.matrixViewer.alnData.fetchOriginalLociList()

            self.optsAllLoci.clear()
            for l in self.allLoci:
                self.optsAllLoci.append([l])

    def switchAutomaticDropdownLocusJump(self, Target=False):
        if Target:
            self.left_handler = self.left_choice.connect(
                "changed", self.Refresh)
            self.right_handler = self.right_choice.connect(
                "changed", self.Refresh)
        else:
            self.left_choice.disconnect(self.left_handler)
            self.right_choice.disconnect(self.right_handler)

    def updateInfo(self, a, b):
        if self.allLoci:
            # DISCONNECT COMBOBOX SIGNALS;
            self.switchAutomaticDropdownLocusJump(Target=False)

            self.left_choice.set_active(a)
            self.right_choice.set_active(b)

            # RECOONECT COMBOBOX SIGNALS;
            self.switchAutomaticDropdownLocusJump(Target=True)


# COMPLEX DISSIMILARITY MATRIX VIEWER GTK APPLICATION;
class MatrixViewer():
    def __init__(self, inputDirectory=None):

        self.Online = False

        # INITIALIZE STATE VARIABLES;
        self.labelColorsOn = 1
        self.index = 0
        self.zoomedPlot = None
        self.swap = False
        self.alnData = None
        self.infoText = Gtk.Label.new("")
        self.Size = None

        # SELECT DRAWING FUNCTION;
        self.drawPlot = Viewer.plotViewport.MainDualRegionPlot
        self.batchRegionPlot = Viewer.plotViewport.plotRegionBatch
        self.plotIdeogram = Viewer.ideogram.plotIdeogram

        # INITIALIZE GTK WINDOW;
        self.Window = Gtk.Window()
        self.Window.connect("destroy", lambda x: Gtk.main_quit())

        self.Window.set_title("straintables - Walk Chromosome Result")

        # Children structures;
        self.locusMap = mapBar.LocusMapBar()
        self.locusNavigator = locusNamesSelectionMenu(self)

        # LOAD DATA;
        self.loadNewFolder(inputDirectory)

        # self.top_menu()
        self.locus_navigator()
        Layout = self.build_interface()

        self.Online = True
        # SHOW ALL;
        self.Window.add(Layout)

        # HIDE THIS ANNOYING THING.
        self.toolbar.message.hide()

        self.resizetimer = time.time()

        self.Size = self.Window.get_size()
        # self.figurecanvas.connect("draw", lambda x, y: self.navigate(0))
        # self.figurecanvas.connect("show", firstshow)
        self.Window.connect("check-resize", self.check_resize)

        # Initialize image;
        self.navigate(0)
        self.Window.show_all()

        # LAUNCH
        Gtk.main()

        # self.navigate(0)
        while Gtk.events_pending:
            Gtk.main_iteration()

    def res(self):
        time.sleep(0.2)
        self.figure.tight_layout()

    def check_resize(self, w):
        Size = w.get_size()
        if self.Size is not None:
            if Size.height > 100 and Size.width > 100:
                if Size != self.Size:
                    print("Resized")
                    d = threading.Thread(target=self.res)
                    d.start()

        else:
            print("Not resized.")
        self.Size = Size

    def top_menu(self):
        # INITIALIZE TOP MENU BAR;
        self.topMenubar = Gtk.MenuBar()

        # FILE dropdown;
        self.menuFile = Gtk.Menu()

        btn_menuFile = Gtk.MenuItem(label="File")
        btn_menuFile.set_submenu(self.menuFile)

        self.topMenubar.append(btn_menuFile)

        loadAlignment = Gtk.MenuItem(label="Load Alignment")
        loadAlignment.connect("activate", self.selectFolderPath)
        self.menuFile.append(loadAlignment)

        # NAVIGATION dropdown;
        self.menuNav = Gtk.Menu()
        btn_menuNav = Gtk.MenuItem(label="Navigation")
        btn_menuNav.set_submenu(self.menuNav)

        self.topMenubar.append(btn_menuNav)

        btn_jumpTo = Gtk.MenuItem(label="Jump to Loci")
        btn_jumpTo.connect("activate", lambda e: locusNamesSelectionMenu(self))
        self.menuNav.append(btn_jumpTo)

    def locus_navigator(self):
        # PREPARE BUTTON ICON IMAGE;
        dna_icon_left = loadImage(Viewer.button_icons.dna_icon)
        dna_icon_right = loadImage(Viewer.button_icons.dna_icon)
        swap_icon = loadImage(Viewer.button_icons.swap)
        # INITIALIZE LOCUS NAVIGATION BUTTONS;
        self.openSequenceLeft = Gtk.Button()
        self.openSequenceLeft.connect("clicked",
                                      lambda d: self.launchAlignViewer(0))
        self.openSequenceLeft.add(dna_icon_left)

        self.openSequenceRight = Gtk.Button()
        self.openSequenceRight.connect("clicked",
                                       lambda d: self.launchAlignViewer(1))
        self.openSequenceRight.add(dna_icon_right)

        self.btn_back = Gtk.Button(image=Gtk.Image(stock=Gtk.STOCK_GO_BACK))
        self.btn_back.connect("clicked", lambda d: self.navigate(-1))

        self.btn_next = Gtk.Button(image=Gtk.Image(stock=Gtk.STOCK_GO_FORWARD))
        self.btn_next.connect("clicked", lambda d: self.navigate(1))

        self.btn_invert = Gtk.Button()
        self.btn_invert.connect("clicked", self.swapPlot)
        self.btn_invert.add(swap_icon)

        self.btn_toggleColor = Gtk.ToggleButton(
            label=None,
            image=Gtk.Image(stock=Gtk.STOCK_COLOR_PICKER))

        # INITIALIZE PLOT FIGURE;
        self.figure = plt.figure()
        self.figurecanvas = FigureCanvas(self.figure)

        self.outputimagemenu = BuildImageMenu(self)
        self.figurecanvas.mpl_connect('button_press_event', self.onclickCanvas)

    def build_interface(self):
        # BUILD INTERFACE;
        vbox = Gtk.VBox()
        # vbox.pack_start(self.topMenubar, expand=False, fill=False, padding=0)

        self.MainPanel = Gtk.HBox()

        self.FigureBox = Gtk.VBox()
        self.FigureBox.pack_start(self.locusMap,
                                  expand=False, fill=False, padding=0)

        self.FigureBox.pack_start(self.figurecanvas,
                                  expand=True, fill=True, padding=0)

        self.MainPanel.pack_start(self.FigureBox,
                                  expand=True, fill=True, padding=0)

        vbox.pack_start(self.MainPanel,
                        expand=True, fill=True, padding=0)

        # SHOW LOCUS NAVIGATION TOOLBAR;
        buttonBox = Gtk.Grid()

        self.btn_back.set_hexpand(True)
        self.btn_next.set_hexpand(True)

        buttonBox.add(self.openSequenceLeft)
        buttonBox.attach(self.btn_back, 1, 0, 3, 1)
        buttonBox.attach(self.btn_invert, 4, 0, 2, 1)
        buttonBox.attach(self.btn_next, 6, 0, 3, 1)
        buttonBox.attach(self.openSequenceRight, 9, 0, 2, 1)

        self.FigureBox.pack_start(buttonBox,
                                  expand=False, fill=True, padding=0)

        # MODIFY MATPLOTLIB TOOLBAR;
        self.toolbar = NavigationToolbar(self.figurecanvas, self.Window)
        self.toolbar.set_history_buttons()

        panelBox = self.bottom_toolbar()
        vbox.pack_start(panelBox, expand=False, fill=False, padding=0)

        return vbox

    def bottom_toolbar(self):
        # SET BOTTOM TOOLBAR, WHICH INCLUDE MATPLOTLIB BAR;
        panelBox = Gtk.HBox(homogeneous=False, spacing=2)

        self.btn_toggleColor.set_tooltip_text("Show Matrix Label Colors")
        self.btn_toggleColor.set_active(True)
        self.btn_toggleColor.connect("clicked", self.toggleColor)

        export_icon = loadImage(Viewer.button_icons.export)
        chr_icon = loadImage(Viewer.button_icons.chr_icon)

        self.loadAlignment = Gtk.Button(
            image=Gtk.Image(stock=Gtk.STOCK_DND_MULTIPLE))
        self.loadAlignment.connect("clicked", self.selectFolderPath)

        panelBox.pack_start(self.loadAlignment,
                            expand=False, fill=False, padding=3)

        panelBox.pack_start(self.toolbar,
                          expand=False, fill=False, padding=0)

        panelBox.pack_start(self.btn_toggleColor,
                            expand=False, fill=False, padding=0)

        self.infoText.set_hexpand(True)
        panelBox.pack_start(self.infoText, expand=True, fill=True, padding=0)

        # -- MAIN VIEW SELECTORS;
        self.ModifyViewButtons = Gtk.HBox()

        self.btn_viewalignment = Gtk.Button(
            image=Gtk.Image(stock=Gtk.STOCK_MEDIA_PLAY))
        self.btn_viewalignment.connect(
            "clicked",
            lambda d: self.ModifyPanelView("alignment")
        )

        self.btn_openfolder = Gtk.Button(image=Gtk.Image(stock=Gtk.STOCK_OPEN))
        self.btn_openfolder.connect(
            "clicked",
            lambda d: self.ModifyPanelView("openfolder")
        )
        self.btn_openfolder.set_tooltip_text("Load result directory.")

        self.btn_outputimage = Gtk.Button()
        self.btn_outputimage.connect(
            "clicked",
            lambda d: self.ModifyPanelView("outputimage")
        )
        self.btn_outputimage.add(export_icon)
        self.btn_outputimage.set_tooltip_text("Build output image.")

        self.btn_ideogram = Gtk.Button()
        self.btn_ideogram.add(chr_icon)
        self.btn_ideogram.connect("clicked",
                                  self.showIdeogram)
        self.btn_ideogram.set_tooltip_text("Show chromosome ideogram.")

        for WIDGET in [self.btn_viewalignment,
                       self.btn_openfolder,
                       self.btn_outputimage,
                       self.btn_ideogram]:
            self.ModifyViewButtons.pack_start(WIDGET,
                                              expand=True,
                                              fill=True,
                                              padding=0)

        panelBox.pack_start(self.ModifyViewButtons, False, False, 5)

        panelBox.pack_end(self.locusNavigator, False, False, 0)

        return panelBox

    def loadNewFolder(self, inputDirectory):
        if inputDirectory:
            self.alnData = alignmentData.AlignmentData(inputDirectory)
            self.infoText.set_text(self.alnData.inputDirectory)
            self.locusNavigator.Update()
            self.locusMap.loadData(self.alnData)
            if self.Online:
                self.navigate(0)
            self.inputDirectory = inputDirectory
        else:
            self.alnData = None

    def cycleIndexes(self, amt):
        if not self.alnData:
            return

        self.index += amt

        while self.index not in self.alnData.allowedIndexes:
            self.index += amt
            if self.index < 0:
                self.index = self.alnData.PWMData.shape[0] - 1
            if self.index > max(self.alnData.allowedIndexes):
                self.index = min(self.alnData.allowedIndexes)

        print(self.index)

    def navigate(self, value):
        self.swap = False
        self.cycleIndexes(value)
        if self.alnData:
            LOCI = self.alnData.getPWMRegionIndexes(self.index)
            self.changeView(LOCI, self.drawPlot)

    def toggleColor(self, d):
        self.labelColorsOn = 1 - self.labelColorsOn
        self.navigate(0)

    def swapPlot(self, d):
        if self.alnData:
            self.swap = 1 - self.swap
            loci = self.alnData.getPWMRegionIndexes(self.index, fullName=True)
            if self.swap:
                loci.reverse()
            self.changeView(loci, self.drawPlot)

    def showIdeogram(self, d):
        regions = []
        for i, C in enumerate(self.outputimagemenu.Checkboxes):
            if C.get_state():
                regions.append(i)

        InformationFile = OutputFile.AnalysisInformation(self.inputDirectory)

        if InformationFile.check():
            InformationFile.read()
            AnnotationPath = InformationFile.content["annotation"]
            self.changeView(regions,
                            self.plotIdeogram,
                            AnnotationPath=AnnotationPath)

    def changeView(self, regions, plotMethod, **kwargs):
        self.figure.clf()
        if self.alnData:
            # UPDATE LOCUS NAVIGATOR;
            if len(regions) == 2:
                self.locusNavigator.updateInfo(*regions)

            # UPDATE LOCUS MAP;
            Half = len(regions) // 2
            self.locusMap.Active["green"] = regions[:Half]
            self.locusMap.Active["red"] = regions[Half:]

            self.locusMap.queue_draw()

            plotMethod(
                self.figure,
                self.alnData,
                regions,
                showLabelColors=self.labelColorsOn,
                **kwargs
            )

            self.figurecanvas.draw()
            self.figurecanvas.flush_events()

            LocusIndexes = self.alnData.getPWMRegionIndexes(self.index)
            self.LocusNames = [
                self.alnData.MatchData["LocusName"][name]
                for name in LocusIndexes
            ]

            ls_tooltip = "View Alignment For %s" % self.LocusNames[0]
            self.openSequenceLeft.set_tooltip_text(ls_tooltip)

            rs_tooltip = "View Alignment For %s" % self.LocusNames[1]
            self.openSequenceRight.set_tooltip_text(rs_tooltip)

    def onclickCanvas(self, event):
        # print(event)
        if event.inaxes:
            Axis = event.inaxes
            if self.zoomedPlot is None:
                Axis._orig_position = Axis.get_position()
                Axis.set_position([0, 0, 1, 1])
                self.zoomedPlot = Axis

                for otherAxis in event.canvas.figure.axes:
                    if otherAxis is not Axis:
                        otherAxis.set_visible(False)

            elif self.zoomedPlot is not None:
                # JUST REDRAW.. SLOWER BUT GUARANTEED
                # (matplotlib is mystical);
                # self.changeView(self.)
                self.zoomedPlot = None

        else:
            print("OFF AXIS.;")

    def launchAlignViewer(self, side):
        LocusName = self.LocusNames[side]

        alignmentFilePath = os.path.join(self.inputDirectory,
                                         "%s%s.aln" % (
                                             Definitions.FastaRegionPrefix,
                                             LocusName))
        command = ["aliview", alignmentFilePath]
        print(command)

        subprocess.run(command)

    def selectFolderPath(self, n):
        folderPathSelector(self)

    def ModifyPanelView(self, target):
        if target == "outputimage":
            ADD = self.outputimagemenu
        elif target == "openfolder":
            self.folderpathselector = folderPathSelector(self)
            ADD = self.folderpathselector
        elif target == "alignment":
            ADD = self.FigureBox

        if self.FigureBox.get_parent():
            REMOVE = self.FigureBox
        elif self.outputimagemenu.get_parent():
            REMOVE = self.outputimagemenu
        elif hasattr(self, 'folderpathselector') and self.folderpathselector.get_parent():
            REMOVE = self.folderpathselector

        if REMOVE:
            self.MainPanel.remove(REMOVE)
        if ADD:
            self.MainPanel.pack_start(ADD, True, True, 0)


class BuildImageMenu(Gtk.VBox):
    def __init__(self, matrix_viewer):

        self.matrix_viewer = matrix_viewer
        self.interface = self.build_interface(self.matrix_viewer.alnData)
        self.pack_start(self.interface, True, True, 0)

        self.show_all()

    def makeCustomPlot(self, btn):
        states = [
            c.get_active()
            for c in self.Checkboxes
        ]

        guide = [
            c.get_active()
            for c in self.GuideCheckboxes
        ]

        ActiveGuide = guide.index(True)
        ActiveGuide = ActiveGuide if ActiveGuide > -1 else 0

        if sum(states) > 6:
            self.Information.set_text("Maximum region count is six.")

        elif not sum(states):
            self.Information.set_text("Please select at least one region.")

        else:
            # Read matrix normalization checkbox;
            MatrixParameters = {
                "pre_multiplier": 6,
                "normalizer": 2
            }

            MatrixParameters["Normalize"] = self.chk_normalize.get_active()
            MatrixParameters["showNumbers"] = self.chk_showvalues.get_active()

            # Read selected regions;
            Regions = [x for x in range(len(states)) if states[x]]
            self.matrix_viewer.changeView(
                Regions,
                self.matrix_viewer.batchRegionPlot,
                reorganizeIndex=ActiveGuide,
                MatrixParameters=MatrixParameters
            )
            self.matrix_viewer.ModifyPanelView("alignment")

    def build_interface(self, alnData):
        Gtk.VBox.__init__(self)

        Layout = Gtk.VBox()

        btn_Confirm = Gtk.Button.new_with_label("Export.")
        btn_Confirm.connect("clicked", self.makeCustomPlot)

        # Setup normalize menu features;
        def newToggleOption(Label):
            checkbox = Gtk.CheckButton()
            label = Gtk.Label(Label)

            container = Gtk.HBox()
            for piece in [checkbox, label]:
                container.pack_start(piece, False, False, 0)

            return checkbox, container

        # Setup shown values features;
        self.chk_normalize, normalizer =\
            newToggleOption("Normalize Matrix Values")

        self.chk_showvalues, showvalues =\
            newToggleOption("Show Matrix Values")

        # Build selectable region list;
        loci_list = alnData.fetchOriginalLociList()

        loci_list_selector = Gtk.Grid()

        self.Information = Gtk.Label()

        self.Checkboxes = []
        self.GuideCheckboxes = []
        GuideGroup = None

        header_components = [
            "Reference",
            "   Region Name  ",
            "Show"
        ]

        for H, hc in enumerate(header_components):
            component = Gtk.Label(hc)
            loci_list_selector.attach(component, H, 0, 1, 1)

        for l, locus in enumerate(loci_list):
            L = Gtk.Label(locus)
            C = Gtk.CheckButton()
            G = Gtk.RadioButton(group=GuideGroup)

            self.Checkboxes.append(C)
            self.GuideCheckboxes.append(G)
            GuideGroup = self.GuideCheckboxes[0]

            for I, Item in enumerate([G, L, C]):
                Item.set_halign(Gtk.Align.CENTER)
                loci_list_selector.attach(Item, I, l + 1, 1, 1)

        # -- Build Layout;
        RegionSelector = Gtk.HBox()
        RegionSelector.pack_start(btn_Confirm, False, False, 0)

        Scroll = Gtk.ScrolledWindow()
        Scroll.add_with_viewport(loci_list_selector)
        RegionSelector.pack_start(Scroll, True, True, 0)

        Layout.pack_start(RegionSelector, True, True, 5)
        Layout.pack_start(self.Information, False, False, 10)

        Options = Gtk.VBox()
        for opt in [normalizer, showvalues]:
            Options.pack_start(opt, False, False, 2)

        Options.set_valign(Gtk.Align.CENTER)

        Layout.pack_start(Options, False, False, 10)

        return Layout


class folderPathSelector(Gtk.VBox):
    def onResponse(self, btn):

        inputDirectory = self.FileChooser.get_filename()
        try:
            self.mainApplication.loadNewFolder(inputDirectory)
            self.mainApplication.ModifyPanelView("alignment")
        except Exception as e:
            self.errorMessage.set_text("Error: %s" % e)

    def __init__(self, matrix_viewer):
        Gtk.VBox.__init__(self)
        self.FileChooser = Gtk.FileChooserWidget(
            action=Gtk.FileChooserAction.SELECT_FOLDER)

        self.mainApplication = matrix_viewer
        self.errorMessage = Gtk.Label.new("Select file.")
        self.errorMessage.set_hexpand(True)
        btn_ok = Gtk.Button(Gtk.STOCK_OPEN)
        btn_cancel = Gtk.Button(Gtk.STOCK_CANCEL)

        buttonGrid = Gtk.Grid()
        buttonGrid.attach(self.errorMessage, 0, 0, 1, 1)
        buttonGrid.attach(btn_ok, 0, 1, 1, 1)
        buttonGrid.attach(btn_cancel, 0, 2, 1, 1)

        self.pack_start(self.FileChooser, True, True, 5)
        self.pack_start(buttonGrid, False, False, 10)

        btn_ok.connect("clicked", self.onResponse)

        self.show_all()


def loadImage(source_image):
    bsource_image = source_image.tobytes()
    dnd = array.array('B', bsource_image)
    width, height = source_image.size
    image_pixelbuffer = GdkPixbuf.Pixbuf.new_from_data(
        dnd,
        GdkPixbuf.Colorspace.RGB,
        True, 8,
        width, height,
        width * 4
    )

    output_image = Gtk.Image()
    output_image.set_from_pixbuf(image_pixelbuffer)
    return output_image


def Execute(options):

    # SHOW DATA;
    PrimerData = OutputFile.PrimerData(options.inputDirectory)
    if PrimerData.check():
        MatrixViewer(options.inputDirectory)
    else:
        print("Analysis file not found at input directory %s." %
              options.inputDirectory)


def parse_arguments():

    parser = ArgumentParser(description=Description)

    parser.add_argument('inputDir',
                        type=str,
                        nargs=1,
                        metavar="inputDirectory",
                        help='inputDirectory')

    parser.add_argument("-d",
                        metavar="inputDirectory",
                        dest="inputDirectory")

    options = parser.parse_args()

    if not options.inputDirectory:
        options.inputDirectory = options.inputDir[0]

    return options


def main():
    options = parse_arguments()
    Execute(options)


if __name__ == "__main__":
    main()
