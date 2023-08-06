import os
import time
from datetime import datetime, timedelta

import cv2
import easygui
import numpy as np
import xlsxwriter
from easygui import multenterbox, boolbox, msgbox
from sklearn.cluster import KMeans
from tqdm import trange


def main():
    # UI Section: all settings are entered by user here
    def user_interface():
        def print_art():
            print(" |  __ \(_)    | |             ( )      / ____|    | |           ")
            print(" | |__) |_  ___| |__  _ __ ___ |/ ___  | |     ___ | | ___  _ __ ")
            print(" |  _  /| |/ _ | '_ \| '_ ` _ \  / __| | |    / _ \| |/ _ \| '__|")
            print(" | | \ \| |  __| | | | | | | | | \__ \ | |___| (_) | | (_) | |   ")
            print(" |_|  \_|_|\___|_| |_|_| |_| |_| |___/  \_____\___/|_|\___/|_|   ")
            print("     /\               | |                    \ \    / |__ \      ")
            print("    /  \   _ __   __ _| |_   _ _______ _ __   \ \  / /   ) |     ")
            print("   / /\ \ | '_ \ / _` | | | | |_  / _ | '__|   \ \/ /   / /      ")
            print("  / ____ \| | | | (_| | | |_| |/ |  __| |       \  /   / /_      ")
            print(" /_/    \_|_| |_|\__,_|_|\__, /___\___|_|        \/   |____|     ")
            print("                          __/ |                                  ")
            print("                         |___/         ")

        def selectMultROI_graphical(img):
            # Read image
            # img = cv2.imread(filepath)
            # Select ROI
            window_name = 'Select Multiple ROIs'
            cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
            cv2.resizeWindow(window_name, 1280, 720)
            boundingBoxes = cv2.selectROIs(window_name, img, True, False)
            # twoCornerBoundingBox = [0, 0, 0, 0]
            # print(boundingBoxes)

            for i in range(0, len(boundingBoxes)):
                # print(i)
                # print("ROI[", i, "] = ", boundingBoxes[i])
                r = boundingBoxes[i]
                imCrop = img[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
                # twoCornerBoundingBox[i] = [int(r[1]): int(r[1] + r[3]), int(r[0]): int(r[0] + r[2])]

                # twoCornerBoundingBox[i] = [int(r[1] + r[3]), int(r[0] + r[2])]
                # imCrop = img[twoCornerBoundingBox[i][0], twoCornerBoundingBox[i][1]]
                # imCrop = img[twoCornerBoundingBox[i]]
                # twoCornerBoundingBox[i] = i

                # Display cropped image
                windowname = "ROI {}"
                cv2.imshow(windowname.format(i), imCrop)
            # print(getAvgColor(imCrop))
            cv2.waitKey(0)
            return boundingBoxes

        def start_end_k_msgbox(fps, totalframes):
            msg = "Selected video is " + str(fps) + " fps and " + str(int(totalframes)) + " frames long."
            title = "colorAnalyzer V2"
            fieldNames = ["Start Frame", "End Frame", "k-Means"]
            fieldValues = [0, int(totalframes), 1]  # we start with blanks for the values
            fieldValues = multenterbox(msg, title, fieldNames, fieldValues)

            # fieldValues = multenterbox("", title, fieldNames, fieldValues)
            # if fieldValues == None: fieldValues = [0, int(totalframes), 1]

            return int(fieldValues[0]), int(fieldValues[1]), int(fieldValues[2])

        # return twoCornerBoundingBox

        def numericROImsgbox(roiNum):
            msg = "Specify ROI {}"
            title = "Numeric ROI Entry"
            fieldNames = ["A", "B", "C", "D"]
            # img[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
            fieldValues = []  # we start with blanks for the values
            fieldValues = multenterbox(msg.format(roiNum), title, fieldNames)

            # make sure that none of the fields was left blank
            while 1:
                if fieldValues == None: break
                errmsg = ""
                for i in range(len(fieldNames)):
                    if fieldValues[i].strip() == "":
                        errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
                if errmsg == "": break  # no problems found
                fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
            for i in range(0, len(fieldValues)):
                fieldValues[i] = int(fieldValues[i])
            return fieldValues

        def selectROIs_full_routine(img):
            # Graphical ROI selection? if not, specify number and dimensions
            if boolbox("Graphical ROI Selection?", "", ["Yes", "No"]):
                retval = selectMultROI_graphical(img)
                cv2.destroyAllWindows()
                return retval
            else:
                # Specify number of ROIs
                global_ROIs = []
                for i in range(0, easygui.integerbox('Specify number of ROIs', '', 1, 1, 255, None, None)):
                    global_ROIs.append(numericROImsgbox(i))
                cv2.destroyAllWindows()
                return global_ROIs

        # print("Riehm's Color Analyzer V2")
        print_art()
        # file select dialog
        path = easygui.fileopenbox()
        opt_filepath = path
        print("Selected File: " + path)
        if path.__contains__(".wmv"):
            print("WARNING!!! wmv files do not always play nicely with OpenCV. Results may vary...")
            msgbox("WARNING!!! wmv files do not always play nicely with OpenCV. Results may vary...")

        cap = cv2.VideoCapture(path)
        cap.set(cv2.CAP_PROP_POS_FRAMES, cap.get(cv2.CAP_PROP_FRAME_COUNT) / 2)

        ret, roi_selection_image = cap.read()

        # ROI selection (DONE, both graphical and numerical!)
        analysis_opt_rois = (selectROIs_full_routine(roi_selection_image))

        # analysis_opt_startframe = int(0)
        # analysis_opt_endframe = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        # analysis_opt_kmeans = int(3)  # 1 kmeans is just averaging, must be higher than 1 to enable

        # create image showing labeled rois here
        def draw_roi_image(img, boundingBoxes):
            def draw_bounding_box(img, label, roi):
                cv2.rectangle(img, (roi[0], roi[1]), (roi[0] + roi[2], roi[1] + roi[3]), (0, 255, 0), 2)
                cv2.putText(img, label, (roi[0] - 10, roi[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            for i in range(0, len(boundingBoxes)):
                draw_bounding_box(img, "ROI_" + str(i), boundingBoxes[i])

        draw_roi_image(roi_selection_image, analysis_opt_rois)
        # cv2.imshow("test", roi_selection_image)
        # cv2.waitKey(0)
        # save roi image to file
        head, tail = os.path.split(path)
        if head[0] == "/":
            head = head + '/'  # linux filepath fix
        else:
            head = head + '\\'  # windows filepath fix
        cv2.imwrite(head + "roi_reference.png", roi_selection_image)

        analysis_opt_startframe, analysis_opt_endframe, analysis_opt_kmeans = start_end_k_msgbox(
            cap.get(cv2.CAP_PROP_FPS),
            cap.get(
                cv2.CAP_PROP_FRAME_COUNT))
        # all user config done by here
        cap.release()
        return path, analysis_opt_startframe, analysis_opt_endframe, analysis_opt_rois, analysis_opt_kmeans

    setting_filepath, setting_start_frame, setting_end_frame, setting_ROIs, setting_kmeans = user_interface()

    def print_user_settings():
        print("setting_filepath = " + str(setting_filepath))
        print("setting_start_frame = " + str(setting_start_frame))
        print("setting_end_frame = " + str(setting_end_frame))
        print("setting_ROIs = " + str(setting_ROIs))
        print("setting_kmeans = " + str(setting_kmeans))

    print_user_settings()
    print("Starting Analysis...")

    #########################################
    # Analysis Section: extract color data from video. store into sensible array for excel section in part 3
    # extracted_data[n][roi] = [absoluteFrame, avgR, avgG, avgB, dom%_0, ...]
    def analysis_section(setting_filepath, setting_start_frame, setting_end_frame, setting_ROIs, setting_kmeans):
        # read a frame
        # for each roi, get avg and kmeans
        # store that to extracted_data array
        # repeat
        total_regions = len(setting_ROIs) * (setting_end_frame - setting_start_frame)

        def get_absolute_frame():
            return int(cap.get(cv2.CAP_PROP_POS_FRAMES))

        def get_average(img):
            return img.mean(axis=0).mean(axis=0)

        def get_kmeans(img):
            def getDominantColorsKmeans(image, k):
                def sort_list(colors, dominance):
                    zipped_pairs = zip(dominance, colors)
                    z = [x for _, x in sorted(zipped_pairs)]
                    z.reverse()
                    dominance.sort()
                    dominance.reverse()
                    return z, dominance

                # convert image into list of RGBs
                # load the image and convert it from BGR to RGB so that
                # we can dispaly it with matplotlib
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

                # reshape the image to be a list of pixels
                image = image.reshape((image.shape[0] * image.shape[1], 3))

                # cluster the pixel intensities
                clt = KMeans(n_clusters=k)
                clt.fit(image)

                counts = np.unique(clt.labels_, return_counts=True)

                formatted_output = []  # follow convention: %fraction of color cluster, r g b. order in descending order of dominance
                # find index of largest count, print color at that index
                total_samples = counts[1].sum()

                domcolors, percents = sort_list(clt.cluster_centers_, counts[1].tolist())

                # print("centers " + str(domcolors))
                # print("percents " + str(percents))

                for i in range(0, k):
                    formatted_output.append(100 * (percents[i] / total_samples))
                    formatted_output.extend(domcolors[i])

                # print(formatted_output)
                # print("----------------- kmeans done ---------------")
                return formatted_output

            if setting_kmeans <= 1:
                return []
            else:
                return getDominantColorsKmeans(img, setting_kmeans)

        # this is a good place for a progress bar
        def analyze_roi(img, progress_current=None):
            # should return [absoluteFrame, avgR, avgG, avgB, dom%_0, ...]
            retval = [get_absolute_frame()]
            retval.extend(get_average(img))
            # get_kmeans(img)
            retval.extend(get_kmeans(img))

            return retval

        def analyzeEachROI(img, boundingBoxes):
            retval = []  # REMEMBER retval[roi][data_field]
            for i in range(0, len(boundingBoxes)):
                r = boundingBoxes[i]
                imCrop = img[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
                # pass imCrop to analyze_roi
                retval.append(analyze_roi(imCrop))

            return retval

        # open capture
        cap = cv2.VideoCapture(setting_filepath)
        # goto start frame
        cap.set(cv2.CAP_PROP_POS_FRAMES, setting_start_frame)

        items = range(setting_end_frame - setting_start_frame)  # retrieve your set of items

        # extracted_data[n][roi] = [absoluteFrame, avgR, avgG, avgB, dom%_0, ...]
        # in other words extracted_data[n][roi][data_field]
        extracted_data = []
        # while within specified frame range
        for i in trange(int(setting_start_frame), int(setting_end_frame), bar_format='{l_bar}{bar:50}{r_bar}{bar:-1b}'):
            # read a frame
            good_frame, fullFrameBuffer = cap.read()  # create full frame buffer and read from current capture position
            # pass to analyzeEachROI
            extracted_data.append(analyzeEachROI(fullFrameBuffer, setting_ROIs))

        cap.release()  # close video file
        return extracted_data

    start = time.time()
    extracted_data = analysis_section(setting_filepath, setting_start_frame, setting_end_frame, setting_ROIs,
                                      setting_kmeans)
    end = time.time()
    analysis_time = ("analysis_time = " + str(timedelta(seconds=(end - start))))
    print(analysis_time)

    ##########################################
    # Output Section: record extracted data to excel file
    # extracted_data[n][roi] = [absoluteFrame, avgR, avgG, avgB, dom%_0, ...]
    def output_section(setting_filepath, setting_start_frame, setting_end_frame, setting_ROIs, setting_kmeans, data):
        date_time = datetime.now()
        head, tail = os.path.split(setting_filepath)
        if head[0] == "/":
            head = head + '/'  # linux filepath fix
        else:
            head = head + '\\'  # windows filepath fix

        name = head + tail.split(".")[0] + "_colorAnalysis_" + date_time.strftime("%m-%d-%Y_%H-%M") + ".xlsx"

        workbook = xlsxwriter.Workbook(name)
        roi_sheets = []
        headersheet = []

        def write_header_page():
            cap = cv2.VideoCapture(setting_filepath)
            header_sheet = workbook.add_worksheet('Header')
            headersheet = header_sheet
            header_sheet.write(0, 0, "Analysis of " + setting_filepath)  # filepath
            # resolution @ frames
            header_sheet.write(1, 0, "Resolution: " + str(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))) + 'x' + str(
                int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))) + '@' + str((cap.get(cv2.CAP_PROP_FPS))) + 'fps')
            # timestamp of analysis
            # analysis time
            header_sheet.write(2, 0, ("start_frame = " + str(setting_start_frame)))
            header_sheet.write(3, 0, ("end_frame = " + str(setting_end_frame)))
            header_sheet.write(4, 0, ("kmeans = " + str(setting_kmeans)))
            header_sheet.write(5, 0, analysis_time)
            for i in range(0, len(setting_ROIs)):
                header_sheet.write(6 + i, 0, ("ROI_" + str(i) + " = " + str(setting_ROIs[i])))
            cap.release()
            # insert roi reference image
            header_sheet.insert_image("B3", head + "roi_reference.png")

        def create_roi_pages():
            # create roi sheets
            for i in range(0, len(setting_ROIs)):
                roi_sheets.append(workbook.add_worksheet("ROI_" + str(i)))
                roi_sheets[i].write(0, 0, "frame")
                roi_sheets[i].write(0, 1, "avgR")
                roi_sheets[i].write(0, 2, "avgG")
                roi_sheets[i].write(0, 3, "avgB")

                # if enabled, do kmeans labels too
                if setting_kmeans > 1:
                    for j in range(0, setting_kmeans):
                        roi_sheets[i].write(0, 4 + (4 * j), "domPercent_" + str(j))  # 6 9
                        roi_sheets[i].write(0, 5 + (4 * j), "domR_" + str(j))  # 7 10
                        roi_sheets[i].write(0, 6 + (4 * j), "domG_" + str(j))  # 8 11
                        roi_sheets[i].write(0, 7 + (4 * j), "domB_" + str(j))  # 6 9

        def write_data():
            def write_roi_data(r):
                for n in range(len(extracted_data)):
                    # print(extracted_data[n][r])
                    for f in range(len(extracted_data[n][r])):
                        roi_sheets[r].write(n + 1, f, extracted_data[n][r][f])

            for i in range(len(setting_ROIs)):
                write_roi_data(i)

        def create_roi_charts():
            # create roi sheets
            for i in range(0, len(setting_ROIs)):
                chart = workbook.add_chart({'type': 'line'})
                chart.add_series(
                    {'values': (("ROI_" + str(i))) + "!$B$1:$B$" + (str(setting_end_frame - setting_start_frame)),
                     'name': "R", 'line': {'color': 'red'}})  # R
                chart.add_series(
                    {'values': (("ROI_" + str(i))) + "!$C$1:$C$" + (str(setting_end_frame - setting_start_frame)),
                     'name': "G", 'line': {'color': 'green'}})  # R
                chart.add_series(
                    {'values': (("ROI_" + str(i))) + "!$D$1:$D$" + (str(setting_end_frame - setting_start_frame)),
                     'name': "B", 'line': {'color': 'blue'}})  # R

                roi_sheets[i].insert_chart('A7', chart)
            # headersheet[0].insert_chart('A'+str(i), chart)

        write_header_page()
        create_roi_pages()
        write_data()
        create_roi_charts()
        print("Saving to " + name)
        workbook.close()

    output_section(setting_filepath, setting_start_frame, setting_end_frame, setting_ROIs, setting_kmeans,
                   extracted_data)
    print("All done!")

#main()