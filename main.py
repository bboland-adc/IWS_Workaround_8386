# This script is for clicking and typing in IWS as a temporary workaround due to WMS limitations.
# Requires IWS to be open on left, top screen and on Right, top screen.  Quit script using ctrl+c as needed.
# Brian Boland 2022-2023 for AutomationDirect

import pyautogui
import requests
# import exceptions

# WS = "12"
#
# # SUMMARY: chooses order cartons to drop in
# # run wms_node once at the beginning to initiate comms
# def load_next_carton():
#     # load.next_carton.self = None
#     # Loads the next available carton as filtered by the RCP
#     # Param is ws or workstation
#     url = "https://amrrcp.automationdirect.com/api/next-pick?pickStation=" + WS
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             print("Response for Next Pick:")
#             data_json = response.json()
#             print(data_json)
#             drop_location = str(data_json['location'])
#             print(drop_location)
#             carton_id = data_json['cartonId']
#             print(carton_id)
#         else:
#             print(f"Failed to retrieve data. Status code: {response.status_code}")
#     except requests.exceptions.RequestException as e:
#         print(f"An error occurred: {e}")
#         drop_loc = drop_location
#         drop_loc_final = "P12 " + drop_loc
#         print(drop_loc_final)


# def get_tote_id():
#     url = "http://amrrcp.automationdirect.com/api/picking/current-toteid/" + WS
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             print("Response for Tote in WS:")
#             tote_id = response.json()
#             print(tote_id)
#         else:
#             print(f"Failed to retrieve data. Status code: {response.status_code}")
#     except requests.exceptions.RequestException as e:
#         print(f"An error occurred: {e}")
#     return
#     print(tote_id)

# i = 1
# total_runs = 40
# while i < totalRuns:
#     print(i)
#     # run whenever an active drop location is empty:
#     rcp.load_next_carton(12)

# run any time a pick is complete or a new tote enters the WS:
# get_pick
#     "http://a-pw-wapp01.automationdirect.com:13107/pick/getToteContent/F023198B?stationID=12"

# run the following for each pick most of the time, except send_abort:
# create_task
# send_task
# send_drop
# send_abort
# validate_code
# complete_pick










# Initialize; try to activate top left corner failsafe
pyautogui.FAILSAFE = True
print(pyautogui.size())
print(pyautogui.position())

# Define all click locations on the screen for BOTH stations:
# Below are screen positions with 2 monitors attached to my laptop
P7L01_to_L06_pos_x = 437        # column on right is ONLY column for P7
P12L01_to_L06_pos_x = 2365      # column on right P12
P12L07_to_L12_pos_x = 2196      # column to the left (P12 only)

# Define Y pixel position for each column of locations for RHR (P7):
P7L01_L07_pos_y = 240
P7L02_L08_pos_y = P7L01_L07_pos_y + 84
P7L03_L09_pos_y = P7L02_L08_pos_y + 84
P7L04_L10_pos_y = P7L03_L09_pos_y + 84

# Define Y pixel position for each column of locations for RDEX (P12):
P12L01_L07_pos_y = 230
P12L02_L08_pos_y = P12L01_L07_pos_y + 84
P12L03_L09_pos_y = P12L02_L08_pos_y + 84
P12L04_L10_pos_y = P12L03_L09_pos_y + 84
P12L05_pos_y = P12L04_L10_pos_y + 84
P12L06_pos_y = P12L05_pos_y + 84

# Explicit definitions of all locations below:
P7L01 = (P7L01_to_L06_pos_x, P7L01_L07_pos_y)
P7L02 = (P7L01_to_L06_pos_x, P7L02_L08_pos_y)
P7L03 = (P7L01_to_L06_pos_x, P7L03_L09_pos_y)
P7L04 = (P7L01_to_L06_pos_x, P7L04_L10_pos_y)

P12L01 = (P12L01_to_L06_pos_x,P12L01_L07_pos_y)
P12L02 = (P12L01_to_L06_pos_x, P12L02_L08_pos_y)
P12L03 = (P12L01_to_L06_pos_x, P12L03_L09_pos_y)
P12L04 = (P12L01_to_L06_pos_x, P12L04_L10_pos_y)
P12L05 = (P12L01_to_L06_pos_x, P12L05_pos_y)
P12L06 = (P12L01_to_L06_pos_x, P12L06_pos_y)
P12L07 = (P12L07_to_L12_pos_x, P12L01_L07_pos_y)
P12L08 = (P12L07_to_L12_pos_x, P12L02_L08_pos_y)
P12L09 = (P12L07_to_L12_pos_x, P12L03_L09_pos_y)
P12L10 = (P12L07_to_L12_pos_x, P12L04_L10_pos_y)

# MANUAL LOAD step buttons to click (static location):
P7manual_load = (995, 974)            # [MANUAL LOAD] button
P12manual_load = P7manual_load + (3830, 0)
P7scan_carton = (1106, 571)           # > enter text input field
P12scan_carton = P7scan_carton + (3830, 0)
P7submit_manual_load = (914, 643)     # [Submit] button
P12submit_manual_load = P7submit_manual_load + (3830,0)
P7ok_button = (967, 637)              # [OK] button (ack the dialog msg after manual load)
P12ok_button = P7ok_button + (3830, 0)

pyautogui.PAUSE = 1
pyautogui.moveTo(P7L01)

# CartonID string from Invar data (from Rich via API):  ** NEEDS WORK!!! **

i = 1
totalRuns = 12                              # This one determines how many times to run through the loop
cartons = []
while i < totalRuns:
    print(i)
#     # nextPick_carton = 'ABC123'
    pyautogui.PAUSE = 1
    try:
        response = requests.get('https://amrrcp.automationdirect.com/api/next-pick?pickStation=12')
        response.raise_for_status()
    except exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    # access JSOn content
    nextPick = response.json()
    pyautogui.PAUSE = 1
    print(nextPick)
    nextPick_carton = nextPick['cartonId']
    nextPick_location = nextPick['location']
    
    nextPick_location = globals()['nextPick_location']
    print(nextPick_location)
#     # nextPick_carton: str = 'ABC123'
    if nextPick_carton == "null":
        exit("No picks available now")
    else:
        print(nextPick_carton)
    if nextPick_location == "null":
        exit("No locations available now)")
    else:
        print(nextPick_location)

#
#
#     # Drop Location for carton (dynamic location; retrieve drop info from Rich via API calls):  ** NEEDS WORK!!! **
#        # nextPick_location = globals()[pyautogui.prompt('Please enter drop carton location in format PSXXLXX')]
#      # cartons.append(nextPick_carton)
#     print(cartons)
#     # ***** Below marks the start of MOVEMENT. *****
    pyautogui.PAUSE = 1
#
    confirm_response = pyautogui.confirm('Cursor is at P7L01 AND ready to go?')
    if confirm_response == 'OK':
        print("Calibrated!")
    else:
        exit("Not aligned properly, check screen config")
#
    print("about to load")
#     # Clicks onto drop location (such as P7L01, for example):
    pyautogui.PAUSE = 1
    dropLocationFull = 'P12' + str(nextPick_location)
    print(dropLocationFull)
    location_click = globals()['P12' + nextPick_location]
    print("location_click is: ")
    print(location_click)
    pyautogui.PAUSE = 1
    pyautogui.click(location_click)

    # Below we will perform a manual load of a carton into the selected WS location:
    pyautogui.PAUSE = 1
    pyautogui.click(P12manual_load)
    pyautogui.click(P12scan_carton)
    # pyautogui.typewrite("B")
    pyautogui.typewrite(nextPick_carton)
    pyautogui.click(P12submit_manual_load)
    pyautogui.moveTo(P12ok_button, duration=0.1),
    pyautogui.click()
#     # HERE: Major exception handling if not successful load, use OCR and PNG recognition from screenshot if it will run...
    print('done')
#     pyautogui.PAUSE = 8
    print(pyautogui.position())

    # confirm_response = pyautogui.confirm('Ready to find the graphic?')
    # if confirm_response == 'OK':
    # print("Ready to find graphic")
    # else:
    # print(confirm_response)
    # exit("Exiting due to error")
    # button_found_location = pyautogui.locateOnScreen('graphic.png')
    # pyautogui.PAUSE = 2
    # print(button_found_location)
    # ** Opportunity to click where a match was located on the screen if needed: **
    # pyautogui.click(button_found_location)
    i += 1

# pyautogui.PAUSE = 0.5


# Below is for handling non-batch ship flags for completed cartons
# try:
#     responseShip = requests.get('https://amrrcp.automationdirect.com/api/ship-ready?pickStation=12')
#     response.raise_for_status()
#     # access JSON content
#     json_data_ship = responseShip.json()
#     # print("Entire JSON response")
#     print(json_data_ship)
#     # nextPick_carton = json_data_ship['cartonId']
#     # print(nextPick_carton)
#     ship_location = json_data_ship['location']
#     print(ship_location)
#
# except HTTPError as http_err:
#     print(f'HTTP error occurred: {http_err}')
# except Exception as err:
#     print(f'Other error occurred: {err}')

# def main():
    # run whenever an active drop location is empty:
    # load_next_carton()

    # run any time a pick is complete or a new tote enters the WS:
    # get_tote_id()
    # get_pick(tote_id,station_id)
    #
    # # run the following for each pick most of the time, except send_abort:
    # create_task()
    # send_task()
    # send_drop()
    # # send_abort()
    # validate_code()
    # complete_pick()



# if __name__ == "__main__":
#     main()