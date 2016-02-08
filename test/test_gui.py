"""
Tests GUI
"""

import pytest
import pyautogui
import os
import multiprocessing
import time

@pytest.fixture
def App():
    import wx
    return wx.App()

@pytest.fixture
def Dedup_obj():
    from gui.gui import Deduplicator
    return Deduplicator

@pytest.fixture(scope="module")
def gui_elements():
    testdir = os.path.dirname(os.path.abspath(__file__))
    guidir = os.path.join(testdir, 'gui_elements')
    return lambda x: os.path.join(guidir, x)

def test_file_quit(App, Dedup_obj, gui_elements):
    Dedup_obj(None)
    p = multiprocessing.Process(target=App.MainLoop)
    p.start()

    time.sleep(2)   # needs time to launch the gui

    assert p.is_alive() == True     # checking if the GUI process is running

    file_menu_location = pyautogui.locateOnScreen(gui_elements('filemenu.png'))
    file_menu_x, file_menu_y = pyautogui.center(file_menu_location)

    t0 = time.clock()
    while not file_menu_location:
        #pyautogui.moveTo(10, 10)
        file_menu_location = pyautogui.locateOnScreen(gui_elements('filemenu.png'))
        if file_menu_location:
            file_menu_x, file_menu_y = pyautogui.center(file_menu_location)
            break

        # timeout 5secs
        if time.clock() - t0 > 5:
            break

    pyautogui.click(file_menu_x, file_menu_y)    # click on &file

    quit_location = pyautogui.locateOnScreen(gui_elements('quit.png'))
    quit_x, quit_y = pyautogui.center(quit_location)

    print quit_x, quit_y

    t0 = time.clock()
    while not quit_location:
        #pyautogui.moveTo(10, 10)
        quit_location = pyautogui.locateOnScreen(gui_elements('quit.png'))
        if quit_location:
            quit_x, quit_y = pyautogui.center(quit_location)
            break

        # timeout
        if time.clock() - t0 > 5:
                break

    pyautogui.click(quit_x, quit_y)

    assert p.is_alive() == False     # checking if the GUI process has stopped
    p.join()
