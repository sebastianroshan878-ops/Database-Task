/**
 * Full Stack Development V8 — Assignment 13: Database Task
 * 
 * Description:
 * Official MongoDB CRUD queries demonstrated on the 'items' collection
 * within the 'inventoryDB' database.
 * 
 * Execution:
 *   mongosh queries.js
 * Or execute each query interactively in mongosh / MongoDB Compass.
 */

// ==========================================
// 1. Database & Collection Setup
// ==========================================
console.log("=== 1. Database & Collection Setup ===");
// Switch to inventoryDB (script-compatible syntax)
db = db.getSiblingDB("inventoryDB");

// Reset collection for a clean demonstration run
db.items.drop();

// Explicitly create the collection
db.createCollection("items");
console.log("Database switched to: " + db.getName() + " | Created collection: items\n");

// ==========================================
// 2. Insert Operations
// ==========================================
console.log("=== 2. Insert Operations ===");

// 2.1 insertOne()
console.log("-> Executing: db.items.insertOne(...)");
const insertOneResult = db.items.insertOne({
  name: "Wireless Mouse",
  category: "Electronics",
  price: 25.99,
  quantity: 150,
  inStock: true,
  tags: ["accessories", "wireless", "computer"]
});
console.log(insertOneResult);

// 2.2 insertMany()
console.log("\n-> Executing: db.items.insertMany(...)");
const insertManyResult = db.items.insertMany([
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
console.log(insertManyResult);

// ==========================================
// 3. Read Operations
// ==========================================
console.log("\n=== 3. Read Operations ===");

// 3.1 find()
console.log("-> Executing: db.items.find({ category: 'Electronics', inStock: true })");
const findResults = db.items.find({ category: "Electronics", inStock: true }).toArray();
console.log(findResults);

// 3.2 findOne()
console.log("\n-> Executing: db.items.findOne({ name: 'Mechanical Keyboard' })");
const findOneResult = db.items.findOne({ name: "Mechanical Keyboard" });
console.log(findOneResult);

// ==========================================
// 4. Update Operations
// ==========================================
console.log("\n=== 4. Update Operations ===");

// 4.1 updateOne()
console.log("-> Executing: db.items.updateOne({ name: 'Wireless Mouse' }, ...)");
const updateOneResult = db.items.updateOne(
  { name: "Wireless Mouse" },
  {
    $set: { price: 22.99, quantity: 140 },
    $currentDate: { lastModified: true }
  }
);
console.log(updateOneResult);

// Verification query for updateOne
console.log("Verification via findOne():");
console.log(db.items.findOne(
  { name: "Wireless Mouse" },
  { name: 1, price: 1, quantity: 1, lastModified: 1 }
));

// 4.2 updateMany()
console.log("\n-> Executing: db.items.updateMany({ category: 'Electronics' }, ...)");
const updateManyResult = db.items.updateMany(
  { category: "Electronics" },
  {
    $set: { onSale: true },
    $inc: { quantity: 10 }
  }
);
console.log(updateManyResult);

// Verification query for updateMany
console.log("Verification via find():");
console.log(db.items.find(
  { category: "Electronics" },
  { name: 1, quantity: 1, onSale: 1 }
).toArray());

// ==========================================
// 5. Delete Operations
// ==========================================
console.log("\n=== 5. Delete Operations ===");

// 5.1 deleteOne()
console.log("-> Executing: db.items.deleteOne({ name: 'Desk Mat Extended' })");
const deleteOneResult = db.items.deleteOne({ name: "Desk Mat Extended" });
console.log(deleteOneResult);

// Verification query for deleteOne
console.log("Verification via find():");
const checkDeleteOne = db.items.find({ name: "Desk Mat Extended" }).toArray();
console.log("Remaining matching documents: " + checkDeleteOne.length + " (Confirmed deleted)");

// 5.2 deleteMany()
console.log("\n-> Executing: db.items.deleteMany({ category: 'Audio' })");
const deleteManyResult = db.items.deleteMany({ category: "Audio" });
console.log(deleteManyResult);

// Verification query for deleteMany
console.log("Verification via find():");
const checkDeleteMany = db.items.find({ category: "Audio" }).toArray();
console.log("Remaining matching documents: " + checkDeleteMany.length + " (Confirmed deleted)");

console.log("\n=== Demonstration Completed Successfully! ===");
