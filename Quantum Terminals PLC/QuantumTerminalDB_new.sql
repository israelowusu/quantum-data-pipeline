CREATE TABLE "Company" (
  "Company_ID" int PRIMARY KEY,
  "Company_Name" varchar
);

CREATE TABLE "Product" (
  "Product_ID" int PRIMARY KEY,
  "Product_Name" varchar
);

CREATE TABLE "Terminal" (
  "Terminal_ID" int PRIMARY KEY,
  "Terminal_Name" varchar
);

CREATE TABLE "StorageTank" (
  "Tank_ID" int PRIMARY KEY,
  "Tank_Number" int,
  "Capacity" decimal,
  "Product_ID" int,
  "Terminal_ID" int
);

CREATE TABLE "Order" (
  "Order_ID" int PRIMARY KEY,
  "Company_ID" int,
  "Product_ID" int,
  "Quantity" int,
  "Order_Date" datetime
);

ALTER TABLE "StorageTank" ADD FOREIGN KEY ("Product_ID") REFERENCES "Product" ("Product_ID");

ALTER TABLE "StorageTank" ADD FOREIGN KEY ("Terminal_ID") REFERENCES "Terminal" ("Terminal_ID");

ALTER TABLE "Order" ADD FOREIGN KEY ("Company_ID") REFERENCES "Company" ("Company_ID");

ALTER TABLE "Order" ADD FOREIGN KEY ("Product_ID") REFERENCES "Product" ("Product_ID");
