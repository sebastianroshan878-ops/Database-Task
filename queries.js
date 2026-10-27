/**
 * Full Stack Development V8 — Assignment 13: Database Task
 * 
 * Description:
 * Official MongoDB CRUD queries demonstrated on the 'items' collection
 * within the 'inventoryDB' database.
 * 
 * Instructions:
 * Run this file in MongoDB Shell (mongosh):
 *   mongosh < queries.js
 * Or execute each query interactively in mongosh or MongoDB Compass.
 */

// ==========================================
// 1. Database & Collection Setup
// ==========================================

// Switch to or create the database
use inventoryDB;

// Explicitly create the collection
db.createCollection("items");

// ==========================================
// 2. Insert Operations
// ==========================================

// 2.1 insertOne()
// Inserts a single document representing an inventory item
db.items.insertOne({
  name: "Wireless Mouse",
  category: "Electronics",
  price: 25.99,
  quantity: 150,
  inStock: true,
  tags: ["accessories", "wireless", "computer"]
});

// 2.2 insertMany()
// Inserts multiple documents across various categories in a single batch
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
]);

// ==========================================
// 3. Read Operations
// ==========================================

// 3.1 find()
// Retrieves multiple documents matching filter: category 'Electronics' and inStock true
db.items.find({ category: "Electronics", inStock: true });

// 3.2 findOne()
// Retrieves a single document matching the specified name
db.items.findOne({ name: "Mechanical Keyboard" });

// ==========================================
// 4. Update Operations
// ==========================================

// 4.1 updateOne()
// Updates price and quantity for 'Wireless Mouse' and records timestamp
db.items.updateOne(
  { name: "Wireless Mouse" },
  {
    $set: { price: 22.99, quantity: 140 },
    $currentDate: { lastModified: true }
  }
);

// Verification query for updateOne:
db.items.findOne(
  { name: "Wireless Mouse" },
  { name: 1, price: 1, quantity: 1, lastModified: 1 }
);

// 4.2 updateMany()
// Adds 'onSale: true' and increments quantity by 10 for all Electronics items
db.items.updateMany(
  { category: "Electronics" },
  {
    $set: { onSale: true },
    $inc: { quantity: 10 }
  }
);

// Verification query for updateMany:
db.items.find(
  { category: "Electronics" },
  { name: 1, quantity: 1, onSale: 1 }
);

// ==========================================
// 5. Delete Operations
// ==========================================

// 5.1 deleteOne()
// Deletes a single document named 'Desk Mat Extended'
db.items.deleteOne({ name: "Desk Mat Extended" });

// Verification query for deleteOne (should return 0 documents):
db.items.find({ name: "Desk Mat Extended" });

// 5.2 deleteMany()
// Deletes all documents in category 'Audio'
db.items.deleteMany({ category: "Audio" });

// Verification query for deleteMany (should return 0 documents):
db.items.find({ category: "Audio" });
