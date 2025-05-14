CREATE EXTERNAL TABLE IF NOT EXISTS stock_data (
    Date DATE,
    Open DOUBLE,
    High DOUBLE,
    Low DOUBLE,
    Close DOUBLE,
    Adj_Close DOUBLE,
    Volume INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
LOCATION 's3://stock-market-data-demo-maryam-gen/processed/'
TBLPROPERTIES ('skip.header.line.count'='1');

SELECT * FROM stock_data;