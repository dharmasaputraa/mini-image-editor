# github.com/dharmasaputraa

import PySimpleGUI as sg
import os.path
from PIL import Image, ImageOps
from processing_list import *

sg.theme("DefaultNoMoreNagging")

op_button = ""
coldepth = 0
coldepth1 = 0
img_input = None
img_input1 = None

# Kolom Area No 1: Area open folder and select image
file_list_column = [
    [
        sg.Frame(
            "Image 1 Information",
            [
                [sg.Text("Image Size : "), sg.Text(size=(13, 1), key="ImgSize")],
                [sg.Text("Color Depth : "), sg.Text(size=(13, 1), key="ImgColorDepth")],
            ],
            font=("OpenSans", 10),
        )
    ],
    [
        sg.Frame(
            "Choose image 1",
            [
                [
                    sg.In(size=(19, 1), enable_events=True, key="ImgFolder"),
                    sg.FolderBrowse(),
                ],
                [
                    sg.Listbox(
                        values=[], enable_events=True, size=(25, 10), key="ImgList"
                    )
                ],
            ],
            font=("OpenSans", 10),
        )
    ],
    [
        sg.Frame(
            "Image 2 Information",
            [
                [sg.Text("Image Size : "), sg.Text(size=(13, 1), key="ImgSize1")],
                [
                    sg.Text("Color Depth : "),
                    sg.Text(size=(13, 1), key="ImgColorDepth1"),
                ],
            ],
            font=("OpenSans", 10),
            visible=False,
            key="infoImage2",
        )
    ],
    [
        sg.Frame(
            "Choose image 2",
            [
                [
                    sg.In(
                        size=(19, 1),
                        enable_events=True,
                        key="ImgFolder1",
                    ),
                    sg.FolderBrowse(),
                ],
                [
                    sg.Listbox(
                        values=[], enable_events=True, size=(25, 10), key="ImgList1"
                    )
                ],
            ],
            font=("OpenSans", 10),
            visible=False,
            key="chooseImage2",
        ),
    ],
    [
        sg.Button("Clear", size=(25, 1), key="clearImage"),
    ],
    [
        sg.Frame(
            "Basic Image Processing",
            [
                [
                    sg.Button("Negative", size=(11, 1), key="ImgNegative"),
                    sg.Button("Grayscale", size=(11, 1), key="ImgGrayscale"),
                ],
                [
                    sg.Frame(
                        "Brightness",
                        [
                            [
                                sg.Slider(
                                    range=(-255, 255),
                                    default_value=0,
                                    size=(21, 10),
                                    orientation="horizontal",
                                    key="Brightness",
                                    enable_events=True,
                                    visible=True,
                                )
                            ],
                            [
                                sg.Text("(*):", key="TitleMulConst", visible=True),
                                sg.In(
                                    size=(7, 1),
                                    enable_events=True,
                                    key="MulConst",
                                    visible=True,
                                ),
                                sg.Text(
                                    "(/):",
                                    key="TitleDivConst",
                                    visible=True,
                                ),
                                sg.In(
                                    size=(8, 1),
                                    enable_events=True,
                                    key="DivConst",
                                    visible=True,
                                ),
                            ],
                        ],
                        font=("OpenSans", 10),
                    ),
                ],
                [
                    sg.Frame(
                        "",
                        [
                            [
                                sg.Button(
                                    "Threshold", size=(22, 1), key="ImgThreshold"
                                ),
                            ],
                            [
                                sg.Button("Logarithm", size=(10, 1), key="ImgLog"),
                                sg.Button("Power-low", size=(10, 1), key="ImgGamma"),
                            ],
                            [
                                sg.Slider(
                                    range=(0, 255),
                                    default_value=0,
                                    size=(21, 10),
                                    orientation="horizontal",
                                    key="otherConst",
                                    enable_events=True,
                                    visible=True,
                                )
                            ],
                        ],
                        font=("OpenSans", 10),
                    )
                ],
            ],
            font=("OpenSans", 10),
        )
    ],
]
# Kolom Area No 2: Area viewer image input
image_viewer_column = [
    [sg.Text("Image 1 Input :")],
    [sg.Text(size=(40, 1), key="FilepathImgInput")],
    [sg.Image(key="ImgInputViewer")],
    [sg.Text("", key="inputImage2")],
    [sg.Text(size=(40, 1), key="FilepathImgInput1")],
    [sg.Image(key="ImgInputViewer1")],
]
# Kolom Area No 3: Area Image info dan Tombol list of processing
list_processing = [
    # [
    #   sg.Frame('Basic Image Processing', [
    #     [
    #       sg.Button("Negative", size=(11, 1), key="ImgNegative"),
    #       sg.Button("Grayscale", size=(11, 1), key="ImgGrayscale"),
    #     ],
    #     [
    #       sg.Frame("Brightness", [
    #         [
    #           sg.Slider(range=(-255,255), default_value=0, size=(21, 10), orientation='horizontal', key="Brightness", enable_events=True, visible = True)
    #         ],
    #         [
    #           sg.Text("(*):", key="TitleMulConst", visible = True),
    #           sg.In(size=(7, 1), enable_events=True, key="MulConst", visible = True),
    #           sg.Text("(/):", key="TitleDivConst", visible = True,),
    #           sg.In(size=(8, 1), enable_events=True, key="DivConst", visible = True),
    #         ],
    #       ], font = ("OpenSans", 10)),
    #     ],
    #     [
    #       sg.Frame("", [
    #         [
    #           sg.Button("Threshold", size=(22, 1), key="ImgThreshold"),
    #         ],
    #         [
    #           sg.Button("Logarithm", size=(10, 1), key="ImgLog"),
    #           sg.Button("Power-low", size=(10, 1), key="ImgGamma"),
    #         ],
    #         [
    #           sg.Slider(range=(0,255), default_value=0, size=(21, 10), orientation='horizontal', key="otherConst", enable_events=True, visible = True)
    #         ]
    #       ], font = ("OpenSans", 10))
    #     ],
    #   ], font = ("OpenSans", 10))
    # ],
    [
        sg.Frame(
            "Image Processing",
            [
                [
                    sg.Frame(
                        "Rotate",
                        [
                            [
                                sg.Slider(
                                    range=(0, 3),
                                    default_value=0,
                                    size=(21, 10),
                                    orientation="horizontal",
                                    key="RotateConst",
                                    enable_events=True,
                                    visible=True,
                                )
                            ],
                        ],
                        font=("OpenSans", 10),
                    ),
                ],
                [
                    sg.Frame(
                        "Flip",
                        [
                            [
                                sg.Button("x", size=(6, 1), key="ImgFlipHorizontal"),
                                sg.Button("y", size=(6, 1), key="ImgFlipVertikal"),
                                sg.Button(
                                    "x,y", size=(6, 1), key="ImgFlipHorizontalVertikal"
                                ),
                            ],
                        ],
                        font=("OpenSans", 10),
                    ),
                ],
                [
                    sg.Frame(
                        "Translation",
                        [
                            [
                                sg.Button(
                                    "Translation", size=(22, 1), key="ImgTranslation"
                                ),
                            ],
                            [
                                sg.Text("x:", visible=True),
                                sg.In(
                                    size=(8, 1),
                                    enable_events=True,
                                    key="XTrans",
                                    visible=True,
                                    default_text=0,
                                ),
                                sg.Text(
                                    "y:",
                                    visible=True,
                                ),
                                sg.In(
                                    size=(9, 1),
                                    enable_events=True,
                                    key="YTrans",
                                    visible=True,
                                    default_text=0,
                                ),
                            ],
                        ],
                        font=("OpenSans", 10),
                    ),
                ],
                [
                    sg.Frame(
                        "Zoom",
                        [
                            [
                                sg.Button("Zoom In", size=(10, 1), key="ZoomIn"),
                                sg.Button("Zoom Out", size=(10, 1), key="ZoomOut"),
                            ],
                            [
                                sg.Slider(
                                    range=(1, 3),
                                    default_value=1,
                                    size=(21, 10),
                                    orientation="horizontal",
                                    key="ZoomValue",
                                    enable_events=True,
                                    visible=True,
                                )
                            ],
                        ],
                        font=("OpenSans", 10),
                    ),
                ],
                [
                    sg.Frame(
                        "Blending",
                        [
                            [
                                sg.Button("Blending", size=(16, 1), key="ImgBlend"),
                                sg.Button(">", size=(4, 1), key="ImgBlendProcess"),
                            ],
                            [
                                sg.Text("a:", visible=True),
                                sg.In(
                                    size=(7, 1),
                                    enable_events=True,
                                    key="alpha1",
                                    visible=True,
                                    default_text="1",
                                ),
                            ],
                            [
                                sg.Text("x:", visible=True),
                                sg.In(
                                    size=(8, 1),
                                    enable_events=True,
                                    key="x1",
                                    visible=True,
                                    default_text="0",
                                ),
                                sg.Text(
                                    "y:",
                                    visible=True,
                                ),
                                sg.In(
                                    size=(9, 1),
                                    enable_events=True,
                                    key="y1",
                                    visible=True,
                                    default_text="0",
                                ),
                            ],
                            [
                                sg.Text(
                                    "Range a1&a2 = 0.0 - 1",
                                    visible=True,
                                    font=("OpenSans", 8),
                                ),
                            ],
                            [
                                sg.Text(
                                    "Range x,y = sesuai dengan wxh image",
                                    visible=True,
                                    font=("OpenSans", 8),
                                ),
                            ],
                        ],
                        font=("OpenSans", 10),
                    ),
                ],
            ],
            font=("OpenSans", 10),
            visible=True,
        )
    ]
]
# Kolom Area No 4: Area viewer image output
image_viewer_column2 = [
    [sg.Text("Image Processing Output:")],
    [sg.Text(size=(40, 1), key="ImgProcessingType")],
    [sg.Image(key="ImgOutputViewer")],
]

# Kolom Area No 5: Area Image info dan Tombol list of processing UTS
list_processing_2 = [
    [
        sg.Frame(
            "Ujian Praktikum 1",
            [
                [
                    sg.Frame(
                        "Negative",
                        [
                            [
                                sg.Frame(
                                    "",
                                    [
                                        [
                                            sg.Button(
                                                "Diamond", size=(7, 1), key="NegDiamond"
                                            ),
                                            sg.Button(
                                                "RevDiamond",
                                                size=(9, 1),
                                                key="NegRevDiamond",
                                            ),
                                        ],
                                        # [
                                        #   sg.Button("Circle", size=(8, 1), key="NegCircle"),
                                        #   sg.Button("RevCircle", size=(10, 1), key="NegRevCircle"),
                                        # ],
                                        [
                                            sg.Slider(
                                                range=(0, 255),
                                                default_value=0,
                                                size=(17, 10),
                                                orientation="horizontal",
                                                key="whNegative",
                                                enable_events=True,
                                                visible=True,
                                            )
                                        ],
                                    ],
                                )
                            ],
                            [
                                sg.Button("X", size=(9, 1), key="NegX"),
                                sg.Button("RevX", size=(9, 1), key="NegRevX"),
                            ],
                        ],
                        font=("OpenSans", 10),
                    ),
                ],
                [
                    sg.Frame(
                        "Mirror",
                        [
                            [
                                sg.Button("Merge", size=(20, 1), key="MirrorMerge"),
                            ],
                        ],
                        font=("OpenSans", 10),
                    ),
                ],
            ],
            font=("OpenSans", 10),
        )
    ],
    [
        sg.Frame(
            "UTS",
            [
                [sg.Button("UTS", size=(22, 1), key="UTS")],
                [
                    sg.Text("a:", visible=True),
                    sg.In(
                        size=(6, 1),
                        enable_events=True,
                        key="utsAlpha1",
                        visible=True,
                        default_text="1",
                    ),
                ],
                [
                    sg.Text("Note: value 0.0 - 1", visible=True, font=("OpenSans", 8)),
                ],
            ],
            font=("OpenSans", 10),
        ),
    ],
    [
        sg.Frame(
            "Filter",
            [
                [
                    sg.Button("Max", size=(10, 1), key="MaxFilter"),
                    sg.Button("Min", size=(10, 1), key="MinFilter"),
                ],
                [
                    sg.Button("Median", size=(10, 1), key="MedianFilter"),
                ],
                [
                    sg.Button("Mean", size=(10, 1), key="MeanFilter"),
                    sg.Button("Gaussian", size=(10, 1), key="GaussianFilter"),
                ],
                [
                    sg.Button("Sobel", size=(10, 1), key="SobelFilter"),
                    sg.Button("Prewitt", size=(10, 1), key="PrewittFilter"),
                ],
                [
                    sg.Button("Robert", size=(10, 1), key="RobertFilter"),
                    sg.Button("Laplacian", size=(10, 1), key="LaplacianFilter"),
                ],
                [
                    sg.Button("Scharr", size=(10, 1), key="ScharrFilter"),
                    sg.Button("Compass", size=(10, 1), key="CompassFilter"),
                ],
                [
                    sg.Button("Erosi", size=(10, 1), key="Erosi"),
                    sg.Button("Delusi", size=(10, 1), key="Delusi"),
                ],
                [
                    sg.Button("Opening", size=(10, 1), key="Opening"),
                    sg.Button("Closing", size=(10, 1), key="Closing"),
                ],
                [
                    sg.Button("WhiteTH", size=(10, 1), key="WhiteTopHat"),
                    sg.Button("BlackTH", size=(10, 1), key="BlackTopHat"),
                ],
            ],
            font=("OpenSans", 10),
        )
    ],
    # [
    #   sg.Frame('Tambahan', [
    #     [
    #       sg.Button("Max", size=(10, 1), key="MaxFilter"),
    #       sg.Button("Min", size=(10, 1), key="MinFilter"),
    #     ],
    #     [
    #       sg.Button("HSV", size=(10, 1), key="HSV"),
    #     ]
    #   ], font = ("OpenSans", 10))
    # ],
]
# Gabung Full layout
layout = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(image_viewer_column),
        sg.VSeperator(),
        sg.Column(list_processing),
        sg.VSeperator(),
        sg.Column(image_viewer_column2),
        sg.VSeperator(),
        sg.Column(list_processing_2),
    ]
]

window = sg.Window("Mini Image Editor by Dharma Saputra", layout)
# Run the Event Loop

# nama image file temporary setiap kali processing output
filename_out = "out.png"

while True:
    event, values = window.read()

    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    # Folder name was filled in, make a list of files in the folder
    if event == "ImgFolder":
        folder = values["ImgFolder"]

        try:
            # Get list of files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".gif"))
        ]
        window["ImgList"].update(fnames)

    # Folder name was filled in, make a list of files in the folder
    elif event == "ImgFolder1":
        folder = values["ImgFolder1"]

        try:
            # Get list of files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".gif"))
        ]
        window["ImgList1"].update(fnames)

    elif event == "ImgList":  # A file was chosen from the listbox
        try:
            filename = os.path.join(values["ImgFolder"], values["ImgList"][0])
            window["FilepathImgInput"].update(filename)
            window["ImgInputViewer"].update(filename=filename)
            window["ImgProcessingType"].update(filename)
            window["ImgOutputViewer"].update(filename=filename)
            img_input = Image.open(filename)

            # img_input.show()

            # Size
            img_width, img_height = img_input.size
            window["ImgSize"].update(str(img_width) + " x " + str(img_height))

            # Color depth
            mode_to_coldepth = {
                "1": 1,
                "L": 8,
                "P": 8,
                "RGB": 24,
                "RGBA": 32,
                "CMYK": 32,
                "YCbCr": 24,
                "LAB": 24,
                "HSV": 24,
                "I": 32,
                "F": 32,
            }
            coldepth = mode_to_coldepth[img_input.mode]
            window["ImgColorDepth"].update(str(coldepth))
        except:
            pass

    elif event == "ImgList1":  # A file was chosen from the listbox
        try:
            filename = os.path.join(values["ImgFolder1"], values["ImgList1"][0])
            window["FilepathImgInput1"].update(filename)
            window["ImgInputViewer1"].update(filename=filename)
            window["ImgProcessingType"].update(filename)
            window["ImgOutputViewer"].update(filename=filename)
            img_input1 = Image.open(filename)

            # img_input.show()

            # Size
            img_width1, img_height1 = img_input1.size
            window["ImgSize1"].update(str(img_width1) + " x " + str(img_height1))

            # Color depth
            mode_to_coldepth1 = {
                "1": 1,
                "L": 8,
                "P": 8,
                "RGB": 24,
                "RGBA": 32,
                "CMYK": 32,
                "YCbCr": 24,
                "LAB": 24,
                "HSV": 24,
                "I": 32,
                "F": 32,
            }
            coldepth1 = mode_to_coldepth1[img_input1.mode]
            window["ImgColorDepth1"].update(str(coldepth1))
        except:
            pass

    elif event == "clearImage":
        try:
            op_button = ""
            window["FilepathImgInput"].update("")
            window["ImgInputViewer"].update(visible=None)
            window["ImgSize"].update("")
            window["ImgColorDepth"].update("")

            window["chooseImage2"].update(visible=False)
            window["infoImage2"].update(visible=False)
            window["inputImage2"].update("")
            window["FilepathImgInput1"].update("")
            window["ImgInputViewer1"].update(visible=None)
            window["ImgSize1"].update("")
            window["ImgColorDepth1"].update("")

            window["ImgProcessingType"].update("")
            window["ImgOutputViewer"].update("")
        except:
            pass
    # button in basic image processing
    elif event == "ImgThreshold":
        op_button = "ImgThreshold"
    elif event == "ImgLog":
        op_button = "ImgLog"
    elif event == "ImgGamma":
        op_button = "ImgGamma"
    elif event == "ZoomIn":
        op_button = "ZoomIn"
    elif event == "ZoomOut":
        op_button = "ZoomOut"

    elif event == "ImgNegative":
        try:
            window["ImgProcessingType"].update("Image Negative")
            img_output = ImgNegative(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgGrayscale":
        try:
            window["ImgProcessingType"].update("Image Grayscale")
            img_output = ImgGrayscale(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgRotate" or event == "RotateConst":
        try:
            if values["RotateConst"] == 0:
                deg = 0
                window["ImgProcessingType"].update(
                    "Image Rotate " + str(deg) + "deg, clockwise"
                )
                img_output = img_input
                img_output.save(filename_out)
                window["ImgOutputViewer"].update(filename=filename_out)
            elif values["RotateConst"] == 1:
                deg = 90
            elif values["RotateConst"] == 2:
                deg = 180
            elif values["RotateConst"] == 3:
                deg = 270

            if values["RotateConst"] != 0:
                window["ImgProcessingType"].update(
                    "Image Rotate " + str(deg) + "deg, Clockwise"
                )
                img_output = ImgRotate(img_input, coldepth, deg, "C")
                img_output.save(filename_out)
                window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "Brightness":
        try:
            value_bright = int(values["Brightness"])
            window["ImgProcessingType"].update(
                "Image Brightness +" + str(value_bright)
            ) if value_bright > 0 else window["ImgProcessingType"].update(
                "Image Brightness " + str(value_bright)
            )
            img_output = ImgPLusMinus(img_input, coldepth, value_bright)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "MulConst":
        try:
            constant = values["MulConst"]
            window["ImgProcessingType"].update(
                "Image Brightness x " + values["MulConst"]
            )
            img_output = ImgMulti(img_input, coldepth, int(constant))
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "DivConst":
        try:
            constant = values["DivConst"]
            window["ImgProcessingType"].update(
                "Image Brightness / " + values["DivConst"]
            )
            img_output = ImgDiv(img_input, coldepth, int(constant))
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif op_button == "ImgThreshold" and event == "otherConst":
        try:
            if event == "ImgThreshold":
                window["otherConst"].update(visible=True, value=70)
                window["ImgProcessingType"].update("Image Threshold 70")
            value_threshold = int(values["otherConst"])
            window["ImgProcessingType"].update(
                "Image Threshold " + str(value_threshold)
            )
            img_output = ImgThreshold(img_input, coldepth, value_threshold)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif op_button == "ImgLog" and event == "otherConst":
        try:
            constant = int(values["otherConst"])
            window["ImgProcessingType"].update("Image Log (" + str(constant) + ")")
            img_output = ImgLogaritma(img_input, coldepth, int(constant))
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif op_button == "ImgGamma" and event == "otherConst":
        try:
            constant = values["otherConst"]
            window["ImgProcessingType"].update(
                "Gamma Correction +" + str(int(constant))
            ) if constant > 0 else window["ImgProcessingType"].update(
                "Gamma Correction " + str(int(constant))
            )
            img_output = ImgGamma(img_input, coldepth, constant)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgFlipHorizontal":
        try:
            window["ImgProcessingType"].update("Flip Horizontal")
            img_output = ImgFlipHorizontal(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgFlipVertikal":
        try:
            window["ImgProcessingType"].update("Flip Vertikal")
            img_output = ImgFlipVertical(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgFlipHorizontalVertikal":
        try:
            window["ImgProcessingType"].update("Flip Horizontal & Vertikal")
            img_output = ImgFlipHorizontalAndVertical(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgBlend":
        window["inputImage2"].update("Image 2 Input :")
        window["chooseImage2"].update(visible=True)
        window["infoImage2"].update(visible=True)

    elif event == "ImgBlendProcess":
        # try:
        window["ImgProcessingType"].update("Image Blend")

        alpha1 = float(values["alpha1"])
        x1 = int(values["x1"])
        y1 = int(values["y1"])

        coldepth2 = mode_to_coldepth[img_input1.mode]

        img_output = ImgBlend(
            img_input, coldepth, img_input1, coldepth2, alpha1, x1, y1
        )

        img_output.save(filename_out)
        window["ImgOutputViewer"].update(filename=filename_out)
    # except:
    #   pass

    elif op_button == "ZoomIn" and event == "ZoomValue":
        # elif event == "ZoomIn":
        try:
            window["ImgProcessingType"].update("Image Zoom In")
            # get value
            scaleVal = int(values["ZoomValue"])

            # calling function
            img_output = ZoomIn(img_input, coldepth, scaleVal)

            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif op_button == "ZoomOut" and event == "ZoomValue":
        # elif event == "ZoomOut":
        try:
            window["ImgProcessingType"].update("Image Zoom Out")
            scaleVal = int(values["ZoomValue"])
            img_output = ZoomOut(img_input, coldepth, scaleVal)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgTranslation":
        try:
            window["ImgProcessingType"].update(
                "Image Translation X = "
                + str(values["XTrans"])
                + " and Y = "
                + str(values["YTrans"])
            )

            transX = int(values["XTrans"])
            transY = int(values["YTrans"])
            img_output = ImgTranslation(img_input, coldepth, transX, transY)

            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "MirrorMerge":
        try:
            window["ImgProcessingType"].update("Image Mirror Merge")

            img_output = merge_flipped_images(img_input, coldepth)

            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "NegDiamond":
        try:
            window["ImgProcessingType"].update("Image Diamond Pattern Negative")

            whValue = values["whNegative"]

            img_output = diamond_negative(img_input, coldepth, whValue)

            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "NegRevDiamond":
        try:
            window["ImgProcessingType"].update("Image Diamond Pattern Negative")

            whValue = values["whNegative"]

            img_output = reverse_diamond_negative(img_input, coldepth, whValue)

            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "NegCircle":
        try:
            window["ImgProcessingType"].update("Image Negative Circle")

            whValue = values["whNegative"]

            img_output = circular_negative(img_input, coldepth, whValue)

            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "NegRevCircle":
        try:
            window["ImgProcessingType"].update("Image Reverse Negative Circle")

            whValue = values["whNegative"]

            img_output = reverse_circular_negative(img_input, coldepth, whValue)

            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "NegX":
        try:
            window["ImgProcessingType"].update("Image X Pattern Negative")

            img_output = x_simbol_negative(img_input, coldepth)

            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "NegRevX":
        try:
            window["ImgProcessingType"].update("Image Reverse X Pattern Negative")

            img_output = reverse_x_simbol_negative(img_input, coldepth)

            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "UTS":
        # try:
        window["ImgProcessingType"].update("UTS")
        alpha1 = values["utsAlpha1"]
        img_output = uts_1(img_input, coldepth, img_input1, coldepth1, alpha1)

        img_output.save(filename_out)
        window["ImgOutputViewer"].update(filename=filename_out)
    # except:
    #     pass

    elif event == "MaxFilter":
        try:
            window["ImgProcessingType"].update("Max Filter")
            img_output = Max_Filter(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "MinFilter":
        try:
            window["ImgProcessingType"].update("Min Filter")
            img_output = Min_Filter(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "MedianFilter":
        try:
            window["ImgProcessingType"].update("Median Filter")
            img_output = Median_Filter(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "MeanFilter":
        try:
            window["ImgProcessingType"].update("Mean Filter")
            img_output = Mean_Filter(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "SobelFilter":
        try:
            window["ImgProcessingType"].update("Sobel Detection")
            img_output = Sobel_Edge(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "PrewittFilter":
        try:
            window["ImgProcessingType"].update("Prewitt Detection")
            img_output = Prewitt_Edge(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "LaplacianFilter":
        try:
            window["ImgProcessingType"].update("Laplacian Detection")
            img_output = Laplacian_Edge(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ScharrFilter":
        try:
            window["ImgProcessingType"].update("Scharr Detection")
            img_output = Scharr_Edge(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "RobertFilter":
        try:
            window["ImgProcessingType"].update("Robert Detection")
            img_output = Robert_Edge(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "GaussianFilter":
        # try:
        window["ImgProcessingType"].update("Gaussian Filter")
        img_output = Gaussian(img_input, coldepth, 1)
        img_output.save(filename_out)
        window["ImgOutputViewer"].update(filename=filename_out)
    # except:
    #     pass

    elif event == "CompassFilter":
        try:
            window["ImgProcessingType"].update("Compass Filter")
            img_output = CompassOperator(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    # elif event == "HSV":
    #     try:
    #         window["ImgProcessingType"].update("Compass Filter")
    #         img_output = hsv(img_input, coldepth)
    #         img_output.save(filename_out)
    #         window["ImgOutputViewer"].update(filename=filename_out)
    #     except:
    #         pass

    elif event == "Delusi":
        try:
            window["ImgProcessingType"].update("Delusi Filter")
            # img_output=dilation(img_input, coldepth)
            img_output = Max_Filter(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "Erosi":
        try:
            window["ImgProcessingType"].update("Erosi Filter")
            # img_output=erosion(img_input, coldepth)
            img_output = Min_Filter(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "Opening":
        try:
            window["ImgProcessingType"].update("Opening Filter")
            img_output = Opening(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "Closing":
        try:
            window["ImgProcessingType"].update("Closing Filter")
            img_output = Closing(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "WhiteTopHat":
        # try:
        window["ImgProcessingType"].update("White Top Hat Filter")
        img_output = WhiteTopHat(img_input, coldepth)
        img_output.save(filename_out)
        window["ImgOutputViewer"].update(filename=filename_out)
    # except:
    #     pass

    elif event == "BlackTopHat":
        # try:
        window["ImgProcessingType"].update("Black Top Hat Filter")
        img_output = BlackTopHat(img_input, coldepth)
        img_output.save(filename_out)
        window["ImgOutputViewer"].update(filename=filename_out)
    # except:
    #     pass


# github.com/dharmasaputraa
