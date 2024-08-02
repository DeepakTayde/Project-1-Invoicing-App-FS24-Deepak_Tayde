# Project-1-Invoicing-App-FS24-Deepak_Tayde
This repository hosts a comprehensive Invoice Management System designed to streamline invoice creation, management, and user authentication. The system features a user-friendly interface and a set of robust API endpoints for seamless operation.

# Invoice Management System

## Overview

This project is an Invoice Management System that provides a platform for users to create and manage invoices. The system includes user authentication, invoice creation, and a detailed view of invoices with itemized lists.

## Table of Contents

1. [UI Components](#ui-components)
2. [User Authentication](#user-authentication)
3. [API List](#api-list)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Contributing](#contributing)
7. [License](#license)

## UI Components

### 1. Create Invoice Page

- **BillDate input**: Allows the user to input the bill date.
- **Client name input**: Allows the user to input the name of the client.
- **Save Invoice button**: Saves the invoice with the selected client, bill date, and added items.

### 2. Invoice List Page

- **Invoice list table**: Displays invoice information, including InvoiceID, ClientName, and BillDate.
- **Items button**: Opens a detailed view of the invoice, including invoice items with Name, Quantity, Rate, and Total for each item, as well as the TotalAmount for the invoice.
- **New Item**: Opens a new form for users to add new items to the invoice.

### 3. User Authentication

- **User login page**: Allows users to log in and then continue with the application.
- **Secure routes**: If users are not logged in, they cannot access the page.

## API List

### 1. Invoice API

- **GET /invoices**: Retrieve a list of all invoices for the Invoice List Page.
- **POST /invoices/new**: Create a new invoice with the selected client, bill date, and added items.
- **GET /invoices/{id}**: Retrieve a specific invoice's information by its ID for the detailed view.

### 2. Invoice Items API

- **POST /invoices/{invoice_id}/items**: Saves a new item to the invoice.

### 3. User Login API

- **POST /user/login**: Takes email and password and returns a successful message or error.
- **POST /user/signup**: Takes name, email, and password and registers the user.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/DeepakTayde/Project-1-Invoicing-App-FS24-Deepak_Tayde.git
   ```
2. Navigate to the project directory:
   ```sh
   cd Project-1-Invoicing-App-FS24-Deepak_Tayde
   ```
3. Install dependencies:
   ```sh
   npm install
   ```
4. Set up the environment variables:
   - Create a `.env` file in the root directory.
   - Add the necessary environment variables (e.g., database credentials, API keys).

## Usage

1. Start the development server:
   ```sh
   npm start
   ```
2. Open your browser and navigate to `http://localhost:3000`.

## Contributing

We welcome contributions from the community! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature/your-feature-name`).
6. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

