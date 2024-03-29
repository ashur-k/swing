# -*- coding: utf-8 -*-
#
# Studio Handler callback methods from Treehouse Swing
#
import os
import glob
import csv
import sys
import traceback
from pymel.core.system import reference
from wildchildanimation.gui.background_workers import TaskFileInfoThread

from wildchildanimation.gui.loader import LoaderDialogGUI
from wildchildanimation.gui.publish import PublishDialogGUI
from wildchildanimation.gui.settings import SwingSettings


_maya_loaded = False    
try:
    import maya.cmds as cmds
    import maya.mel as mel
    import maya.OpenMaya as om
    import maya.OpenMayaUI as omui

    import pymel.core as pm
    from pymel.util import putEnv

    from PySide2 import QtWidgets    
    from shiboken2 import wrapInstance

    _maya_loaded = True
except:
    pass

from wildchildanimation.gui.downloads import DownloadDialogGUI
from wildchildanimation.gui.search import SearchFilesDialog
from wildchildanimation.gui.swing_create import SwingCreateDialog
from wildchildanimation.gui.swing_utils import fcount, friendly_string, write_log
from wildchildanimation.maya.swing_maya import SwingMaya

from wildchildanimation.studio.studio_interface import StudioInterface

from wildchildanimation.gui.swing_playblast import SwingPlayblastUi
from wildchildanimation.maya.swing_export import SwingExportDialog
from wildchildanimation.gui.entity_info import EntityInfoDialog

from wildchildanimation.gui.swing_gui import SwingGUI

def maya_main_window():
    """
    Return the Maya main window widget as a Python object
    """
    main_window_ptr = omui.MQtUtil.mainWindow()
    if sys.version_info.major >= 3:
        return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)
    else:
        return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)

class MayaStudioHandler(StudioInterface, SwingMaya):

    NAME = "MayaStudioHandler"
    VERSION = "0.0.4"
    SUPPORTED_TYPES = [".ma", ".mb", ".fbx", ".obj", ".mov", ".mp4", ".wav", ".jpg", ".png", ".abc" ]

    def __init__(self):
        super(MayaStudioHandler, self).__init__()

    def log_error(self, text):
        if _maya_loaded:
            om.MGlobal.displayError("[MayaStudioHandler] {0}".format(text))
        else:
            write_log("[error] {}".format(text))

    def log_warning(self, text):
        if _maya_loaded:
            om.MGlobal.displayWarning("[MayaStudioHandler] {0}".format(text))
        else:
            write_log("[warn] {}".format(text))

    def log_output(self, text):
        if _maya_loaded:
            om.MGlobal.displayInfo(text)
        else:
            write_log("[info] {}".format(text))    

    def get_param(self, option, value):
        ### runs a custom value request against the local dcc
        if option == "frame_range":

            if value == "Render":
                start_frame = int(cmds.getAttr("defaultRenderGlobals.startFrame"))
                end_frame = int(cmds.getAttr("defaultRenderGlobals.endFrame"))
            elif value == "Playback":
                start_frame = int(cmds.playbackOptions(q=True, minTime=True))
                end_frame = int(cmds.playbackOptions(q=True, maxTime=True))
            elif value == "Animation":
                start_frame = int(cmds.playbackOptions(q=True, animationStartTime=True))
                end_frame = int(cmds.playbackOptions(q=True, animationEndTime=True))
            else:
                raise RuntimeError("Invalid frame range preset: {0}".format(value))

            return (start_frame, end_frame)

        raise None

    def set_globals(self, **kwargs):
        write_log("on_globals")

        if "project" in kwargs:
            putEnv("project", kwargs["project"])

        if "episode" in kwargs:
            putEnv("episode", kwargs["episode"])

        if "sequence" in kwargs:
            putEnv("sequence", kwargs["sequence"])

        if "task_type_name" in kwargs:
            putEnv("task_type_name", kwargs["task_type_name"])

        if "shot" in kwargs:
            putEnv("shot", kwargs["shot"])

        if "asset" in kwargs:
            putEnv("asset", kwargs["asset"])

        if "frame_in" in kwargs:
            putEnv("frame_in", kwargs["frame_in"])

        if "frame_out" in kwargs:
            putEnv("frame_out", kwargs["frame_out"])

        if "frame_count" in kwargs:
            putEnv("frame_count", kwargs["frame_count"])

        return True

    #
    # returns a list of unresolved files in a scene
    def list_unresolved(self):
        self.log_output("searching for unresolved references")
        refs = cmds.file(query = True, list = True, unresolvedName = True)

        self.log_output("searching for unresolved references {}".format(refs))
        return refs

    #
    #
    # Exports the scene in layout format
    #
    # Source: Chainsaw002.py
    # Author: Miruna D. Mateescu
    # Last Modified: 2021/04/05
    #
    def export_to_csv(csv_filename, file_prefix = "hby_204_", shot_start = 10, shot_step = 10):
        all_shots = cmds.ls(type="shot")
        shot_no = shot_start        
        with open(csv_filename, 'w') as csv_file:
            writer = csv.writer(csv_file)            
            for crt_shot in all_shots:
                shot_start = cmds.getAttr(crt_shot+".startFrame")
                shot_end = cmds.getAttr(crt_shot+".endFrame")
                shot_cam = cmds.listConnections(crt_shot+".currentCamera")                
                cmds.playbackOptions(animationStartTime=shot_start, minTime=shot_start, animationEndTime=shot_end, maxTime=shot_end)
                cmds.lookThru(shot_cam)
                cmds.currentTime(shot_start)                
                if "shot_" in crt_shot:
                    if shot_no < 100:
                        padding = "0"
                    else:
                        padding = ""                    
                    shot_name = "SH"+padding+str(shot_no)
                    cmds.rename(crt_shot, shot_name)
                    cmds.file(rn=file_prefix+shot_name+".ma")
                    cmds.file(save=True)                    
                    writer.writerow([shot_name, shot_start, shot_end, shot_cam])
                    shot_no += shot_step

    # tries to import the file specified in source into the currently open scene
    def load_file(self, **kwargs):
        source = kwargs["source"]
        force = kwargs["force"]
        working_dir = kwargs["working_dir"]

        self.log_output("load_file:: {0} to {1}".format(source, working_dir))
        self.log_output("Source  {0}".format(working_dir))
        self.log_output("Working Dir {0}".format(working_dir))

        filename, file_extension = os.path.splitext(source)

        if file_extension in MayaStudioHandler.SUPPORTED_TYPES:
            prompt_val = cmds.file(prompt=True, q=True)
            try:
                if not force and cmds.file(q = True, modified = True):
                    if QtWidgets.QMessageBox.question(maya_main_window(), 'Unsaved changes', 'Current scene has unsaved changes. Continue?') == QtWidgets.QMessageBox.StandardButton.Yes:
                        force = True
                    else:
                        self.log_output("Aborted load file")
                        return

                cmds.file(source, open = True, ignoreVersion = True, prompt = False, force = force)
            except:
                traceback.print_exc(file=sys.stdout)
                self.log_error("Error processing importing reference {}".format(source))
                return False
            finally:
                cmds.file(prompt = prompt_val)

        else:
            self.log_error("File extension not valid {0}".format(file_extension))                

        write_log("load_file complete")
        return True    

    # tries to import the file specified in source into the currently open scene
    def import_file(self, **kwargs):
        source = kwargs["source"]
        working_dir = kwargs["working_dir"]

        self.log_output("import_file:: {0} to {1}".format(source, working_dir))
        self.log_output("Source  {0}".format(working_dir))
        self.log_output("Working Dir {0}".format(working_dir))

        filename, file_extension = os.path.splitext(source)

        if file_extension in MayaStudioHandler.SUPPORTED_TYPES:
            self.log_output("Loading file {}".format(source))
            try:
                pm.system.importFile(source)
                self.log_output("importFile {} successfully".format(filename))
            except:
                traceback.print_exc(file=sys.stdout)
                self.log_error("Error processing load file {}".format(source))
                return False
        else:
            self.log_error("File extension not valid {0}".format(file_extension))                

        write_log("load_file complete")
        return True  

    # tries to import the file specified in source into the currently open scene
    def import_reference(self, **kwargs):
        source = kwargs["source"]
        working_dir = kwargs["working_dir"]
        namespace = kwargs["namespace"]

        self.log_output("load_reference:: {0}".format(source, working_dir))
        self.log_output("Source  {0}".format(working_dir))
        self.log_output("Working Dir {0}".format(working_dir))
        self.log_output("Namespace {0}".format(namespace))

        filename, file_extension = os.path.splitext(source)

        if file_extension in MayaStudioHandler.SUPPORTED_TYPES:
            self.log_output("Importing file {}".format(source))

            prompt_val = cmds.file(prompt=True, q=True)
            try:
                cmds.file(source, prompt = False, reference = True, ignoreVersion = True, namespace = namespace, options = "v=0;")
                self.log_output('cmds.file({0}, prompt = False, reference = True, ignoreVersion = True, namespace = {1}, options = "v=0;"'.format(source, namespace))
            except:
                traceback.print_exc(file=sys.stdout)
                self.log_error("Error processing importing reference {}".format(source))
                return False
            finally:
                cmds.file(prompt = prompt_val)

        else:
            self.log_error("File extension not valid {0}".format(file_extension))

        write_log("import_reference complete")
        return True      


    def create_folder(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)  

    #
    # Swing API Handlers
    #

    # create a new maya project file
    def on_show_swing(self):
        SwingGUI.show_dialog(self)

    def on_create(self, **kwargs):
        parent = kwargs["parent"]

        task_info = kwargs["task_info"]
        task_dir = task_info["project_dir"]
        task = task_info["task"]
        
        working_file = friendly_string("_".join(self.get_task_sections(task)).lower())    

        #add software
        working_file_name = "{}.ma".format(working_file)
        self.createDialog = SwingCreateDialog(parent = parent, task_id = task["id"], entity_id = task["entity"]["id"])

        existingFile = None
        if os.path.exists(task_dir):
            if os.path.exists(os.path.join(task_dir, working_file_name)):
                existingFile = os.path.join(task_dir, working_file_name)
                self.createDialog.checkBoxLoadExisting.setVisible(True)

        result = self.createDialog.exec_()
        if result:
            working_dir = self.createDialog.get_working_dir()
            file_name = self.createDialog.get_file_name()

            if existingFile and not self.createDialog.checkBoxLoadExisting.isChecked():

                if QtWidgets.QMessageBox.question(maya_main_window(), 'Warning: Existing file found', 'If you continue, this file will be lost, are you sure?') != QtWidgets.QMessageBox.StandardButton.Yes:
                    self.log_output("Aborted load file")
                    return

            if existingFile and self.createDialog.checkBoxLoadExisting.isChecked():
                self.load_file(source = existingFile, working_dir = working_dir, force = True)
            else:
                frame_in = self.createDialog.get_start_frame()
                frame_out = self.createDialog.get_end_frame()
                frame_rate = self.createDialog.get_frame_rate()

                project_file = os.path.join(working_dir, file_name)

                #directory = self.createDialog.working_dir        
                self.log_output("on_create {} [{}]".format(working_dir, file_name))
                self.log_output("on_create frame_in [{}]".format(frame_in))
                self.log_output("on_create frame_out [{}]".format(frame_out))
                self.log_output("on_create frame_rate [{}]".format(frame_rate))

                #self.log_output("Source  {0}".format(kwargs["source"]))
                #self.log_output("Working Dir {0}".format(kwargs["working_dir"]))
                #self.log_output("Namespace {0}".format(kwargs["namespace"]))

                fn, fext = os.path.splitext(file_name)

                if fext in MayaStudioHandler.SUPPORTED_TYPES:
                    self.log_output("Creating file {}".format(project_file))

                    prompt_val = cmds.file(prompt=True, q=True)
                    try:
                        self.create_folder(working_dir)
                        
                        cmds.file(new = True, force = True)
                        cmds.file(rename = project_file)

                        self.log_output("setting frame rate to {}".format(frame_rate))
                        frame_rate = self.set_frame_rate(frame_rate)

                        self.log_output("setting animation range from {} to {}".format(frame_in, frame_out))
                        cmds.playbackOptions(edit=True, animationStartTime = frame_in, animationEndTime = frame_out)

                        self.log_output("set frame rate to {}".format(frame_rate))
                        cmds.file(save = True)

                        self.log_output("on_create <-- {}".format(project_file))
                    except:
                        traceback.print_exc(file=sys.stdout)
                        self.log_error("Error processing creating new file {}".format(project_file))
                        return False
                    finally:
                        cmds.file(prompt = prompt_val)

                else:
                    self.log_error("File extension not valid {0}".format(fn))

            self.log_output("create_file complete")
        return True 

    def on_load(self, **kwargs):
        parent = kwargs["parent"]
        entity = kwargs["entity"]
        files = kwargs["files"]
        selected = kwargs["selected"]

        loaderDialog = LoaderDialogGUI(parent = parent, handler = self, entity = entity)
        loaderDialog.load_files(files)
        loaderDialog.set_selected(selected)
        loaderDialog.show()        

    def on_search(self, **kwargs):
        self.log_output("on_search::")
        project = kwargs["project"]

        if "text" in kwargs:
            text = kwargs["text"]
        else:
            text = ''

        if "task_types" in kwargs:
            task_types = kwargs["task_types"]
        else:
            task_types = None

        if "status_types" in kwargs:
            status_types = kwargs["status_types"]
        else:
            status_types = None
        
        self.searchDialog = SearchFilesDialog(parent = None, text = text, project = project, task_types = task_types, status_types = status_types)
        if len(text) > 0:
            self.searchDialog.process()
        result = self.searchDialog.exec_()

        if result:
            self.downloadDialog = DownloadDialogGUI(parent = None, handler = self, file_list = self.searchDialog.get_file_list())
            self.downloadDialog.show()       

    def scan_working_dir(self, directory, ext):
        print("Searching {} for {}".format(directory, ext))
        file_list = []
        file_list += filter(os.path.isfile, glob.glob(directory + '/{}'.format(ext)))

        print("Returning {}".format(len(file_list)))
        file_list = sorted(file_list, key = os.path.getmtime)
        return file_list

    def on_publish(self, **kwargs):
        task_info = kwargs["task_info"]
        task_dir = task_info["project_dir"]
        task = task_info["task"]

        if "task_types" in kwargs:
            task_types = kwargs["task_types"]
        else:
            task_types = None   

        self.publishDialog = PublishDialogGUI(task = task, task_types = task_types)            

        file_path = cmds.file(q = True, sn = True)
        self.publishDialog.set_working_file(file_path)        

        cached_dir = os.path.join(task_dir, 'cache')
        if os.path.exists(cached_dir):
            print("Checking alembics: {}".format(cached_dir))

            file_list = self.scan_working_dir(cached_dir, '*.abc')
            if len(file_list) > 0:
                self.publishDialog.add_reference_file(file_list[0], 'Alembic')
                self.publishDialog.load_reference_table()
            else:
                print("No alembic files found")

        playblast_dir = os.path.join(task_dir, 'playblasts')
        if os.path.exists(playblast_dir):
            print("Checking playblast_dir: {}".format(playblast_dir))
            file_list = self.scan_working_dir(playblast_dir, '*.mp4')
            if len(file_list) > 0:
                self.log_output("Adding playblast: {}".format(file_list[0]))
                self.publishDialog.set_output_file(file_list[0])

        self.publishDialog.show()        

    def on_export(self, **kwargs):
        try:
            task = kwargs["task"] 

            working_dir = self.get_scene_path()

            if "task_types" in kwargs:
                task_types = kwargs["task_types"]
            else:
                task_types = None        

            self.exportDialog = SwingExportDialog(handler = self, task = task, working_dir = working_dir)
            self.exportDialog.show()
        except:
            traceback.print_exc(file=sys.stdout)
        return True        

    def on_save(self, **kwargs):
        file_path = cmds.file(q = True, sn = True)
        file_base = os.path.basename(file_path)
        file_name, file_ext = os.path.splitext(file_base)

        request = {
            "source": file_base,
            "file_path": file_path,
            "file_name": file_name,
            "file_ext": file_ext,            
        }
        return request

    def on_entity_info(self, **kwargs):
        try:
            entity_id = kwargs["entity_id"]
            task_types = kwargs["task_types"]
            self.entityDialog = EntityInfoDialog(entity = entity_id, handler = self, task_types = task_types)
            self.entityDialog.show()              
        except:
            traceback.print_exc(file=sys.stdout)
            return False 

        return True            

    def on_playblast(self, **kwargs):
        task_info = kwargs["task_info"]
        task_dir = task_info["project_dir"]
        task = task_info["task"]

        working_file = friendly_string("_".join(self.get_task_sections(task)))

        playblast_count = 1
        if os.path.exists(task_dir):
            playblasts = os.path.join(task_dir, "playblasts")
            if os.path.exists(playblasts):
                playblast_count = fcount(playblasts)

        playblast_version ="{}".format(playblast_count).zfill(3)
        playblast_filename = "{}_v{}".format(working_file, playblast_version)
        playblast_target = os.path.join(task_dir, "playblasts", playblast_filename)

        self.log_output("open: {} {} {}".format(playblast_version, playblast_filename, playblast_target))
        try:
            dialog = SwingPlayblastUi()
            dialog.set_caption_text(" ".join(self.get_task_sections(task)))
            dialog.set_output_file_name(playblast_target)
            dialog.show()

            self.log_output("open: playblast")
        except:
            traceback.print_exc(file=sys.stdout)
            return False 

        return True
        # playblast  -format avi -sequenceTime 0 -clearCache 1 -viewer 1 -showOrnaments 1 -fp 4 -percent 50 -compression "none" -quality 70;


    def load_task(self, task_id):
        self.taskLoader = TaskFileInfoThread(parent = self, task = task_id, project_root=SwingSettings.get_instance().swing_root())
        return self.taskLoader.run()

'''
        # exports current selected
        source = kwargs["target"]
        working_dir = kwargs["working_dir"]
        selection = kwargs["selection"]

        target = os.path.join(working_dir, source)
        target = os.path.normpath(target)       

        if "All" in selection:
            # select all dag objects and all dependency nodes
            pm.select(all = True) 

        # https://tech-artists.org/t/solved-problem-exporting-fbx-from-maya-without-animation/8796        
        cmds.FBXResetExport()
        cmds.FBXExportHardEdges('-v', True)
        cmds.FBXExportSmoothingGroups('-v', True)
        cmds.FBXExportTangents('-v', True)
        cmds.FBXExportBakeComplexAnimation('-v', True)

        cmds.FBXExport('-file', target, '-s')

        self.log_output("fbx export {0} {1}".format(source, working_dir))        
        return True
'''