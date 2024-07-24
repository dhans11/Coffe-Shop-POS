# Coffee Shop POS System
---

## Overview

This project, created by Ahmad Dani Rifai, is a Point of Sale (POS) system designed to manage and streamline the sales of a coffee shop, specifically Imigrasi Coffee. The system includes functionality for viewing, adding, updating, and deleting items in the store's inventory.

## Features

- **Display Inventory**: View a list of all items available in the coffee shop, along with their details.
- **Add New Items**: Add new items to the inventory, including their code, name, stock, price, and color.
- **Update Items**: Modify the details of existing items in the inventory.
- **Delete Items**: Remove items from the inventory.
- **Confirmations**: Ensure user actions with confirmation prompts to prevent accidental changes.

## Code Structure

The main components of the code are:

- **showdata(barang)**: Displays the list of items in the inventory.
- **checkExitRead()**, **checkExitcreate()**, **checkExitUpdate()**, **checkExitDelete()**: Functions to confirm exiting various menus.
- **inputKodeBarang()**, **inputNamaBarang()**, **inputStockBarang()**, **inputHargaBarang()**, **inputWarnaBarang()**: Input validation functions for different item attributes.
- **updateBarangBaru(data)**, **updateStockBaru(data)**, **updateHargaBaru(data)**, **updateWarnaBaru(data)**: Functions to update specific attributes of an item.
- **deleteData(data, kode)**: Function to delete a specific item.
- **menuRead()**, **menuCreate()**, **menuUpdate()**, **menuDelete()**: Menu functions for reading, creating, updating, and deleting items.
- **menuUtama()**: Main menu function.

## Usage

1. **Run the Program**: Execute the script to start the POS system.
   ```bash
   python main.py
   ```
2. **Main Menu**: You will be presented with the main menu with the following options:
   - **1. Menu Read Data Barang**: View the inventory.
   - **2. Menu Create Barang**: Add new items to the inventory.
   - **3. Menu Update Barang**: Update existing items in the inventory.
   - **4. Menu Delete Barang**: Delete items from the inventory.
   - **5. Exit**: Exit the program.

3. **Navigating Menus**: Enter the corresponding number to navigate through the menus and perform actions. Follow the prompts and enter the required information when asked.

## Example Usage

1. **Viewing Items**:
   - Select option `1` from the main menu to view the inventory.
   
2. **Adding a New Item**:
   - Select option `2` from the main menu.
   - Follow the prompts to enter the item code, name, stock, price, and color.

3. **Updating an Item**:
   - Select option `3` from the main menu.
   - Choose the item to update by entering its code.
   - Select the attribute to update (name, stock, price, or color).

4. **Deleting an Item**:
   - Select option `4` from the main menu.
   - Enter the code of the item to delete.

5. **Exiting the Program**:
   - Select option `5` from the main menu to exit.
