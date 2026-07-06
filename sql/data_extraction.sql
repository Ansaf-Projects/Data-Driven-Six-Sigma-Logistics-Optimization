CREATE DATABASE IF NOT EXISTS logistics_db;
USE logistics_db;

CREATE TABLE orders (
    order_id VARCHAR(20) PRIMARY KEY,
    operational_date DATE,
    shift CHAR(1),
    picking_time_seconds DECIMAL(10,2)
);

CREATE TABLE packing_quality (
    order_id VARCHAR(20),
    packing_accuracy_status INT,
    FOREIGN KEY(order_id) REFERENCES orders(order_id)
);

SELECT 
    o.order_id,
    o.operational_date,
    o.shift,
    o.picking_time_seconds,
    q.packing_accuracy_status
FROM orders o
INNER JOIN packing_quality q 
    ON o.order_id = q.order_id;