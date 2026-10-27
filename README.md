# Full Stack Development V8 — Assignment 13: Database Task

**Student Assignment:** Database Task  
**Database:** `inventoryDB`  
**Collection:** `items`  
**Environment:** MongoDB Shell (`mongosh`) / MongoDB Compass  

---

## 1. Assignment Overview

This assignment focuses on executing essential **CRUD (Create, Read, Update, Delete)** operations in **MongoDB** using official MongoDB shell commands or the MongoDB Compass interface.

According to the official assignment specifications:
- **Database-Only:** There is no backend server or API integration required.
- **Collection Setup:** All queries operate on the `items` collection inside `inventoryDB`.
- **Coverage:** Demonstrates 2 inserts, 2 reads, 2 updates, and 2 deletes using valid JSON/BSON documents.

---

## 2. Recommended Project Structure

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
├── queries.js               # Standalone, executable MongoDB script
└── README.md                # Project documentation and execution instructions
```

---

## 3. Database & Collection Setup

To initialize the database and collection in the MongoDB Shell (`mongosh`):

```javascript
// Switch to or create the database
use inventoryDB

// Create the target collection
db.createCollection("items")
```

---

## 4. Required CRUD Operations

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
* **Output:** `{ acknowledged: true, insertedId: ObjectId('671e7a40f1a9c802b1100001') }`
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
* **Output:** `{ acknowledged: true, insertedIds: { '0': ObjectId(...), '1': ObjectId(...), ... } }`
* **Evidence:** Saved in `screenshots/insertMany.png`.

---

### 4.2 Read Operations

#### 3. `find()`
Retrieves all documents matching specified filter criteria (`category: "Electronics"` and `inStock: true`).

```javascript
db.items.find({ category: "Electronics", inStock: true })
```
* **Output:** Returns array of 4 matching electronics items with full document fields.
* **Evidence:** Saved in `screenshots/find.png`.

---

#### 4. `findOne()`
Retrieves exactly one document matching the query condition (`name: "Mechanical Keyboard"`).

```javascript
db.items.findOne({ name: "Mechanical Keyboard" })
```
* **Output:** Returns the single document object for Mechanical Keyboard.
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
* **Output:** `{ acknowledged: true, matchedCount: 1, modifiedCount: 1, upsertedCount: 0 }`
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
* **Output:** `{ acknowledged: true, matchedCount: 4, modifiedCount: 4, upsertedCount: 0 }`
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
* **Output:** `{ acknowledged: true, deletedCount: 1 }`
* **Evidence:** Saved in `screenshots/deleteOne.png`.

---

#### 8. `deleteMany()`
Deletes all items belonging to `category: "Audio"`, verified via a follow-up `find()` query.

```javascript
db.items.deleteMany({ category: "Audio" })

// Verification query (returns 0 documents):
db.items.find({ category: "Audio" })
```
* **Output:** `{ acknowledged: true, deletedCount: 1 }`
* **Evidence:** Saved in `screenshots/deleteMany.png`.

---

## 5. Execution Instructions

### Option A: Running via MongoDB Shell (`mongosh`)
1. Open terminal / PowerShell and start `mongosh`:
   ```bash
   mongosh
   ```
2. Execute the entire script at once:
   ```bash
   load("queries.js")
   ```
   Or run directly from PowerShell:
   ```bash
   mongosh < queries.js
   ```

### Option B: Running via MongoDB Compass
1. Connect to your local MongoDB instance (`mongodb://localhost:27017`).
2. Select or create the database **`inventoryDB`**.
3. Create or select the collection **`items`**.
4. Use the **_MONGOSH** terminal bar at the bottom or the query filter bar to execute the operations.

---

## 6. Evaluation Rubric Alignment (Total 10 Marks)

| Skill / Component | Criteria for Full Marks | Status |
| :--- | :--- | :--- |
| **`insertOne` + `insertMany`** (2 Marks) | Both shown with valid JSON data | Demonstrated with valid BSON documents in `insertOne.png` & `insertMany.png` |
| **`find` + `findOne`** (2 Marks) | Both queries return expected documents | Filtered queries returning expected documents in `find.png` & `findOne.png` |
| **`updateOne` + `updateMany`** (2 Marks) | Correct field modifications confirmed | Verified field updates with `$set`, `$inc`, `$currentDate` in `updateOne.png` & `updateMany.png` |
| **`deleteOne` + `deleteMany`** (2 Marks) | Correct deletions confirmed via `find()` | Confirmed deletion via empty `find()` in `deleteOne.png` & `deleteMany.png` |
| **Results Documentation** (2 Marks) | All screenshots present, readable & consistent | All 8 required screenshots generated in `screenshots/` and embedded in `final_submission.docx` |

---

## 7. Submission Deliverables

As required by the assignment guidelines:
- **`screenshots/`**: Folder containing all 8 operation screenshots (`insertOne.png` through `deleteMany.png`).
- **`final_submission.docx`**: Completed assignment report with database name, collection name, query descriptions, queries, and embedded screenshots.
- **`queries.js`**: Clean, ready-to-run MongoDB query script.
