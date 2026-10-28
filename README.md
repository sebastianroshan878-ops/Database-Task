# Full Stack Development V8 — Assignment 13: Database Task (JavaScript)

**Student Assignment:** Database Task  
**Technology Stack:** Pure JavaScript / MongoDB (`mongosh`)  
**Database:** `inventoryDB`  
**Collection:** `items`  
**Environment:** MongoDB Shell (`mongosh`) / MongoDB Compass  

---

## 1. Assignment Overview

This assignment focuses on executing essential **CRUD (Create, Read, Update, Delete)** operations in **MongoDB** using official MongoDB JavaScript shell commands or the MongoDB Compass query interface.

According to the official assignment specifications:
- **Database-Only:** There is no backend server or API integration required.
- **Collection Setup:** All queries operate on the `items` collection inside `inventoryDB`.
- **Pure JavaScript:** All commands, queries, and execution scripts are 100% JavaScript.
- **Coverage:** Demonstrates 2 inserts, 2 reads, 2 updates, and 2 deletes using valid JSON/BSON documents.

---

## 2. Project Structure

```text
Database Task/
├── screenshots/
│   ├── insertOne.png        # Input query & output result for insertOne()
│   ├── insertMany.png       # Input query & output result for insertMany()
│   ├── find.png             # Input query & output result for find()
│   ├── findOne.png          # Input query & output result for findOne()
│   ├── updateOne.png        # Input query & output result for updateOne()
│   ├── updateMany.png       # Input query & output result for updateMany()
│   ├── deleteOne.png        # Input query & output result for deleteOne()
│   └── deleteMany.png       # Input query & output result for deleteMany()
├── final_submission.docx    # Formatted Word submission report with screenshots
├── queries.js               # Standalone, executable MongoDB JavaScript script
├── run_assignment.js        # Pure JavaScript interactive runner
├── package.json             # Project configuration and npm scripts
└── README.md                # Project documentation and execution instructions
```

---

## 3. Database & Collection Setup (JavaScript)

To initialize the database and collection in the MongoDB Shell (`mongosh`):

```javascript
// Switch to or create the database
use inventoryDB

// Create the target collection
db.createCollection("items")
```

---

## 4. Required CRUD Operations (JavaScript)

### 4.1 Insert Operations

#### 1. `insertOne()`
Inserts a single document representing an inventory item into the collection.

```javascript
db.items.insertOne({
  name: "Wireless Mouse",
  category: "Electronics",
  price: 25.99,
  quantity: 150,
  inStock: true,
  tags: ["accessories", "wireless", "computer"]
})
```
* **Evidence:** Saved in `screenshots/insertOne.png`.

---

#### 2. `insertMany()`
Inserts multiple inventory records (5 diverse products) in a single batch operation.

```javascript
db.items.insertMany([
  {
    name: "Mechanical Keyboard",
    category: "Electronics",
    price: 89.99,
    quantity: 75,
    inStock: true,
    tags: ["gaming", "rgb"]
  },
  {
    name: "Gaming Monitor 27-inch",
    category: "Electronics",
    price: 299.99,
    quantity: 30,
    inStock: true,
    tags: ["display", "144hz"]
  },
  {
    name: "USB-C Hub Multiport",
    category: "Electronics",
    price: 34.50,
    quantity: 120,
    inStock: true,
    tags: ["adapter", "usb-c"]
  },
  {
    name: "Noise-Cancelling Headphones",
    category: "Audio",
    price: 149.99,
    quantity: 45,
    inStock: true,
    tags: ["audio", "bluetooth"]
  },
  {
    name: "Desk Mat Extended",
    category: "Office Supplies",
    price: 19.99,
    quantity: 200,
    inStock: true,
    tags: ["desk", "pad"]
  }
])
```
* **Evidence:** Saved in `screenshots/insertMany.png`.

---

### 4.2 Read Operations

#### 3. `find()`
Retrieves all documents matching specified filter criteria (`category: "Electronics"` and `inStock: true`).

```javascript
db.items.find({ category: "Electronics", inStock: true })
```
* **Evidence:** Saved in `screenshots/find.png`.

---

#### 4. `findOne()`
Retrieves exactly one document matching the query condition (`name: "Mechanical Keyboard"`).

```javascript
db.items.findOne({ name: "Mechanical Keyboard" })
```
* **Evidence:** Saved in `screenshots/findOne.png`.

---

### 4.3 Update Operations

#### 5. `updateOne()`
Updates a single document (`"Wireless Mouse"`), modifying its price and quantity using `$set` and updating the `lastModified` timestamp with `$currentDate`.

```javascript
db.items.updateOne(
  { name: "Wireless Mouse" },
  {
    $set: { price: 22.99, quantity: 140 },
    $currentDate: { lastModified: true }
  }
)

// Verification query confirming modification:
db.items.findOne(
  { name: "Wireless Mouse" },
  { name: 1, price: 1, quantity: 1, lastModified: 1 }
)
```
* **Evidence:** Saved in `screenshots/updateOne.png`.

---

#### 6. `updateMany()`
Modifies multiple documents matching `category: "Electronics"` by setting an `onSale: true` flag and incrementing `quantity` by 10 using `$inc`.

```javascript
db.items.updateMany(
  { category: "Electronics" },
  {
    $set: { onSale: true },
    $inc: { quantity: 10 }
  }
)

// Verification query confirming changes:
db.items.find(
  { category: "Electronics" },
  { name: 1, quantity: 1, onSale: 1 }
)
```
* **Evidence:** Saved in `screenshots/updateMany.png`.

---

### 4.4 Delete Operations

#### 7. `deleteOne()`
Deletes a single item (`"Desk Mat Extended"`) from the collection, verified via a follow-up `find()` query.

```javascript
db.items.deleteOne({ name: "Desk Mat Extended" })

// Verification query (returns 0 documents):
db.items.find({ name: "Desk Mat Extended" })
```
* **Evidence:** Saved in `screenshots/deleteOne.png`.

---

#### 8. `deleteMany()`
Deletes all items belonging to `category: "Audio"`, verified via a follow-up `find()` query.

```javascript
db.items.deleteMany({ category: "Audio" })

// Verification query (returns 0 documents):
db.items.find({ category: "Audio" })
```
* **Evidence:** Saved in `screenshots/deleteMany.png`.

---

## 5. Execution Instructions (JavaScript Only)

### Option 1: Execute via MongoDB Shell (`mongosh`)
```powershell
mongosh queries.js
```
*Or using npm:*
```powershell
npm start
```

### Option 2: Execute via Node.js
```powershell
node run_assignment.js
```
*Or using npm:*
```powershell
npm run run
```

### Option 3: Interactive in MongoDB Compass
1. Open **MongoDB Compass** and click **Connect** (`mongodb://localhost:27017`).
2. Select database **`inventoryDB`** and collection **`items`**.
3. Open the **`>_MONGOSH`** tab at the bottom to execute queries.

---

## 6. Submission Deliverables

- **`final_submission.docx`**: Completed assignment report with database name, collection name, query descriptions, queries, and embedded screenshots.
- **`screenshots/`**: Folder containing all 8 operation screenshots (`insertOne.png` through `deleteMany.png`).
- **`queries.js`**: Pure JavaScript MongoDB query file.
- **`run_assignment.js`**: Pure JavaScript runner script.
