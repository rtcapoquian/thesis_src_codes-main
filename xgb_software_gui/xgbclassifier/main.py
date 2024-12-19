import flet as ft
import serial
import csv
import time
import pandas as pd
import random
import os

# Directory path for saving the csv
PREDEFINED_DIR = './data/'

if not os.path.exists(PREDEFINED_DIR):
    os.makedirs(PREDEFINED_DIR)

def gather_data(duration=5):
    ser = serial.Serial('COM4', 9600, timeout=1) # CHANGE THIS DEPENDING ON THE PORT USED
    time.sleep(3)
    filename = os.path.join(PREDEFINED_DIR, 'edible_oil_data.csv')
    
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["MQ2", "MQ3", "MQ4", "MQ5", "MQ6", "MQ7", "MQ8", "MQ9", "MQ135", "MQ137"])
        
        start_time = time.time()
        while (time.time() - start_time) < duration:
            line = ser.readline().decode('utf-8', errors='ignore').strip()
            if line:
                data = line.split(',')
                if len(data) == 10:
                    csvwriter.writerow(data)
    
    ser.close()
    return filename

# Placeholder classification logic since no model has been trained yet
def classify_oil():
    return random.choice(['Animal-Based', 'Plant-Based'])

# Main XGBClassifier Flet App
def main(page: ft.Page):
    page.title = "XGBClassifier - Edible Oil Detection"
    
    def show_main_menu(e=None):
        page.controls.clear()
        
        page.add(
            ft.AppBar(title=ft.Text("XGBClassifier"), center_title=True),
            ft.Text("Welcome to the XGBClassifier", size=40, text_align=ft.alignment.center),
            ft.ElevatedButton("Start", on_click=start_data_gathering, bgcolor=ft.colors.GREEN)
        )
        page.update()

    def start_data_gathering(e):
        page.controls.clear()
        
        cancel_btn = ft.ElevatedButton("Cancel", on_click=show_main_menu, bgcolor=ft.colors.RED)
        page.add(
            ft.Text("Gathering data...", size=20),
            ft.ProgressBar(width=400),
            cancel_btn
        )
        page.update()

        # Simulate Data Gathering & Preprocessing
        filename = gather_data(duration=5)
        
        # After data is gathered, go to decision screen
        page.controls.clear()
        page.add(
            ft.Text("Use data to train or classify?", size=30),
            ft.Row([
                ft.ElevatedButton("Train", on_click=lambda e: train_data(filename)),
                ft.ElevatedButton("Classify", on_click=classify_data),
            ], alignment=ft.MainAxisAlignment.CENTER),
            cancel_btn
        )
        page.update()

    def train_data(filename):
        page.controls.clear()
        page.add(ft.Text(f"Data has been saved to {filename} for training.", size=25), ft.ElevatedButton("Main Menu", on_click=show_main_menu))
        page.update()

    def classify_data(e=None):
        page.controls.clear()
        
        cancel_btn = ft.ElevatedButton("Cancel", on_click=show_main_menu, bgcolor=ft.colors.RED)
        page.add(ft.Text("Classifying...", size=20), ft.ProgressBar(width=400), cancel_btn)
        page.update()

        result = classify_oil()

        page.controls.clear()
        if result == 'Animal-Based':
            page.add(ft.Text("Animal-Based Edible Oil Detected", size=30))
        else:
            page.add(ft.Text("Plant-Based Edible Oil Detected", size=30))
        page.add(ft.ElevatedButton("Main Menu", on_click=show_main_menu))
        page.update()

    show_main_menu()

ft.app(target=main)
